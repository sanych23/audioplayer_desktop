import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog,QLabel
from PySide6.QtGui import (QAction,QFont,QIcon)
from Lib.Interface.MusicWindow import MusicWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime, QSize
from PySide6.QtGui import QIcon


class MusicWidget(QMainWindow):
    def __init__(self, song_info):
        super().__init__()

        self.muted = True

        self.ui = MusicWindow()
        self.ui.setupUi(self, song_info['somg_name'], song_info['album_name'])
        self.setWindowTitle('Music Player Application')

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audioVolumeLevel = 15
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(self.audioVolumeLevel/100)
        self.song_name = 1
        self.file_path = f"file/music/{self.song_name}.mp3"

        self.player.setSource(QUrl.fromLocalFile(self.file_path))

        self.ui.toolButtonPlay.clicked.connect(self.play_music)
        self.ui.horizontalSliderVolume.sliderMoved.connect(self.volume_slider_changed)
        self.ui.horizontalSliderVolume.setValue(self.audioVolumeLevel)
        self.ui.horizontalSliderPlay.sliderMoved.connect(self.play_slider_changed)
        self.ui.toolButtonPause.clicked.connect(self.pause_btn)
        self.ui.toolButtonStop.clicked.connect(self.stop_btn)
        self.ui.toolButtonVolume.clicked.connect(self.volume_mute)

        #connect media player signals
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)


    def open_music(self):
        pass

    def play_music(self):
        print('Called play music')
        if self.player.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def position_changed(self, position):
        if(self.ui.horizontalSliderPlay.maximum() != self.player.duration()):
            self.ui.horizontalSliderPlay.setMaximum(self.player.duration())

        self.ui.horizontalSliderPlay.setValue(position)


        seconds = (position / 1000) % 60
        minutes = (position / 60000) % 60
        hours = (position / 2600000) % 24

        time = QTime(hours, minutes, seconds)
        self.ui.labelTimer.setText(time.toString())


    def duration_changed(self, duration):
        self.ui.horizontalSliderPlay.setRange(0, duration)


    def volume_slider_changed(self, position):
        self.audioVolumeLevel = position
        self.audio.setVolume(position/100)

    def play_slider_changed(self, position):
        self.player.setPosition(position)

    def pause_btn(self):
        self.player.pause()
    def stop_btn(self):
        self.player.stop()

    def volume_mute(self):
        if(self.muted):
            self.audio.setMuted(True)
            self.ui.horizontalSliderVolume.setValue(0)
            self.ui.toolButtonVolume.setIcon(QIcon(":/icons/mute.png"))
            self.muted = False
        else:
            self.audio.setMuted(False)
            self.ui.horizontalSliderVolume.setValue(self.audioVolumeLevel)
            self.ui.toolButtonVolume.setIcon(QIcon(":/icons/volume.png"))
            self.muted = True
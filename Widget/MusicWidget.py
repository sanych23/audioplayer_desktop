import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog,QLabel
from PySide6.QtGui import (QAction,QFont,QIcon)
from Lib.Interface.MusicWindow import MusicWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime, QSize
from Events import Events, EventMusicWidget
import os

class MusicWidget(QMainWindow, Events, EventMusicWidget):
    def __init__(self, parent, song_info):
        super().__init__()
        self.parent_window = parent
        self.muted = True
        self.ui = MusicWindow()
        self.artist = self.get_artist_list(song_info['song_id'])
        self.ui.setupUi(self, song_info['song_id'], song_info['song_name'], self.artist)
        self.setWindowTitle('Music Player Application')
        self.song_info = song_info
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audioVolumeLevel = 15
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(self.audioVolumeLevel/100)
        self.file_path = f"music/{self.song_info["hash_name"]}.mp3"
        self.ui.toolButtonPlay.clicked.connect(self.play_music)
        self.ui.horizontalSliderVolume.sliderMoved.connect(self.volume_slider_changed)
        self.ui.horizontalSliderVolume.setValue(self.audioVolumeLevel)
        self.ui.horizontalSliderPlay.sliderMoved.connect(self.play_slider_changed)
        self.ui.toolButtonPause.clicked.connect(self.pause_btn)
        self.ui.toolButtonPause.hide()
        self.ui.toolButtonStop.clicked.connect(self.stop_btn)
        self.ui.toolButtonVolume.clicked.connect(self.volume_mute)
        self.ui.delete_btn.clicked.connect(self.delete_song)

        #connect media player signals
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.setSource(QUrl.fromLocalFile(self.file_path))


    def play_music(self):
        print('Called play music')
        if self.parent_window.playing_music:
            self.parent_window.playing_music.stop_btn()
        # for widget in self.parent_window.music_widgets:
        #     widget.pause_btn()
        if self.player.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()
        self.parent_window.playing_music = self
        self.ui.toolButtonPlay.hide()
        self.ui.toolButtonPause.show()

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
        self.ui.toolButtonPause.hide()
        self.ui.toolButtonPlay.show()
        if self.parent_window.playing_music == self:
            self.parent_window.playing_music = None
        # self.ui.toolButtonPause.hide()

    def stop_btn(self):
        self.player.stop()
        if self.parent_window.playing_music == self:
            self.parent_window.playing_music = None
        self.ui.toolButtonPause.hide()
        self.ui.toolButtonPlay.show()
        

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
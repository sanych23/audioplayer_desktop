from vendor.database import DbORM

class Events:
    database = DbORM()

    def open_add_album(self):
        self.hide()
        self.add_album_wiget.show()

    def close_add_album(self):
        self.parent_window.show()
        self.hide()

    def add_album(self):
        name = self.input_name.text()
        description = self.input_description.toPlainText()
        release_date = self.input_release.text()

        self.database.add_album({
            "name": name,
            "description": description,
            "release_date": release_date,
        })


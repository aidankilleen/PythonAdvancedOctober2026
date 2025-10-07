# pyqt6_oo_application.py


import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QListWidget, QListWidgetItem, QTextEdit, QLabel
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtCore import QUrl


API_URL = "https://api.acodingtutor.com/users?_delay=5000"

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.counter = 0

        self.setWindowTitle("OO QT6")
        self.setGeometry(100, 100, 600, 400)
        self.btn_test = QPushButton("Press Me", self)
        self.btn_test.move(20, 20)
        self.btn_test.clicked.connect(self.on_click)

        self.lbl_info = QLabel(self)
        self.lbl_info.setText(f"Count:{self.counter}")
        self.lbl_info.setGeometry(100, 0, 100, 20)

        self.btn_fetch = QPushButton("Fetch", self)
        self.btn_fetch.move(150, 20)
        self.btn_fetch.clicked.connect(self.on_fetch_clicked)

        self.net = QNetworkAccessManager(self)

        self.user_list = QListWidget(self)
        self.user_list.move(50, 80)

    def on_fetch_clicked(self):
        reply = self.net.get(QNetworkRequest(QUrl(API_URL)))
        reply.finished.connect(lambda:self.on_done(reply))
        
    def on_done(self, reply):

        if reply.error() == QNetworkReply.NetworkError.NoError:
            text = reply.readAll().data().decode("utf-8", "replace")
            data = json.loads(text)
            print(data)
            for user in data:
                try:
                    self.user_list.addItem(QListWidgetItem(user['name']))
                except:
                    pass
                finally:
                    pass
                #self.user_list.addItem(QListWidgetItem(user["name"]))
        else:
            QMessageBox.information(self, "error", reply.errorString())
    
    def on_click(self):
        self.counter += 1
        self.lbl_info.setText(f"Count:{self.counter}")

if __name__ == "__main__":

    # instantiate the app
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
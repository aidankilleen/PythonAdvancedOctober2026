# pyqt6_hello_world.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QListWidget, QListWidgetItem

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QT6 Hello World")
window.setGeometry(100, 100, 600, 400)

button = QPushButton("Click Me", window)
button.move(50, 20)

name_list = QListWidget(window)
name_list.move(50, 80)

names = ["alice", "bob", "carol", "dan"]

for name in names:
    name_list.addItem(QListWidgetItem(name))
    
def on_item_clicked(item):
    print (item.text())
    QMessageBox.information(window, "You clicked item in list", item.text())

name_list.itemClicked.connect(on_item_clicked)

#def on_click():
#    QMessageBox.information(window, "You clicked", "You clicked the button")

#button.clicked.connect(on_click)
button.clicked.connect(lambda x:QMessageBox.information(window, "You clicked", "You clicked the button"))

window.show()
sys.exit(app.exec())


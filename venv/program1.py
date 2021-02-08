from design1 import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow
import requests
import os
import sys


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.xInp.setText('55.933290')
        self.yInp.setText('54.720718')
        self.sizeEdit.setText('0.002')
        self.showBtn.clicked.connect(self.getImage)

    def getImage(self):
        # Получаем изображение по запросу, сохраняем его в файл
        map_request = f"""http://static-maps.yandex.ru/1.x/?ll={self.xInp.text()},{self.yInp.text()}&spn={self.sizeEdit.text()},{self.sizeEdit.text()}&l=map"""
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code,
                  "(", response.reason, ")")
            sys.exit(1)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(self.map_file)
        self.mapLab.setPixmap(self.pixmap)

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
     app = QApplication(sys.argv)
     myapp = MyApplication()
     myapp.show()
     sys.exit(app.exec())
from design2 import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
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
        self.size = 5
        self.showBtn.clicked.connect(self.get_image)
        self.PgUp.clicked.connect(self.size_up)
        self.PgDown.clicked.connect(self.size_down)
        # показывает, был ли произведен поиск
        # если да, то при изменении размера автоматически будет произведен перезапрос
        # с новым размером
        self.found = False

    def get_image(self):
        self.found = True
        # Получаем изображение по запросу, сохраняем его в файл
        map_request = f"""http://static-maps.yandex.ru/1.x/?ll={self.xInp.text()},{self.yInp.text()}&spn={str(self.size * 0.0005)},{str(self.size * 0.0005)}&l=map"""
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
        print('Запрос выполнен успешно')  # для понимания, не зависла ли программа

    def closeEvent(self, event):
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.size_up()
        elif event.key() == Qt.Key_PageDown:
            self.size_down()

    def size_up(self):
        if self.size > 5:
            self.size -= 5
            if self.found:
                self.get_image()
        else:
            print('Достигнуто предельное значение')


    def size_down(self):
        if self.size < 100:
            self.size += 5
            if self.found:
                self.get_image()
        else:
            print('Достигнуто предельное значение')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApplication()
    myapp.show()
    sys.exit(app.exec())

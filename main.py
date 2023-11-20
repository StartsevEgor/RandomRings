import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Рисование')
        self.drawButton.clicked.connect(self.draw)

    def draw(self):
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        while True:
            x, y = [randint(1, 190), randint(1, 190)]
            random_size = randint(1, 190)
            if x + random_size < 200 or y + random_size < 200:
                break
        qp.drawEllipse(x, y, x + random_size, y + random_size)
        # Завершаем рисование
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

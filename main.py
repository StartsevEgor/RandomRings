import sys

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class Example(QMainWindow):
    def __init__(self):
        self.flag = False
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Рисование')
        self.drawButton.clicked.connect(self.test)

    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw(qp)
            # Завершаем рисование
            qp.end()

    def test(self):
        self.flag = True
        self.update()

    def draw(self, qp):
        x, y = [randint(1, self.size().width()), randint(1, self.size().height())]
        random_size = randint(1, 190)
        qp.setBrush(QColor("yellow"))
        qp.drawEllipse(QPoint(x, y), random_size, random_size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

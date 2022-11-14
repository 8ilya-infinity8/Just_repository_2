import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from random import randint, choice

from UI import Ui_Form

COLORS = (Qt.yellow, Qt.cyan, Qt.green, Qt.blue, Qt.black, Qt.red)


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('не Желтые окружности')

        self.flag = False
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        pen = QPen(choice(COLORS))
        pen.setWidth(5)
        self.qp.setPen(pen)
        size = randint(10, 150)
        x, y = randint(1, 382), randint(1, 269)
        self.qp.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

import sys
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 430, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Пуск"))


class Example(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.draw = True
        self.show()

    def run(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_ell(qp)
        qp.end()

    def draw_ell(self, qp):
        if self.draw:
            x, y = randint(0, 640), randint(0, 480)
            qp.setPen(QPen(Qt.yellow))
            r = randint(10, 240)
            qp.drawEllipse(x, y, 2 * r, 2 * r)
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

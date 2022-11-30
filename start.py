from PyQt5 import QtCore, QtGui, QtWidgets

from inst import Ui_Inst                                    # +++


class Ui_Start(object):
    def setupUi(self, Start):
        Start.setObjectName("Ui_Start")
        Start.resize(443, 293)

        self.lineEdit = QtWidgets.QLineEdit(Start)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 321, 51))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Start)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 421, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Start)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 210, 141, 58))
#        self.pushButton_2.setStyleSheet("font: 16pt \"Molot\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Start)
        self.pushButton.setGeometry(QtCore.QRect(50, 140, 321, 58))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Start)
        QtCore.QMetaObject.connectSlotsByName(Start)

    def retranslateUi(self, Start):                                       # v):   ???
        _translate = QtCore.QCoreApplication.translate
        Start.setWindowTitle(_translate("Start", "Start"))
        self.textEdit.setHtml(_translate("Start",  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">введите номер и букву класса класса :</span></p></body></html>"))


        self.pushButton_2.setText(_translate("Start", "инструкция"))
        self.pushButton.setText(_translate("Start", "1"))


class MyInst(QtWidgets.QWidget, Ui_Inst):                          # +++
    def __init__(self, parent=None):
        super(MyInst, self).__init__(parent)
        self.setupUi(self)


class Main(QtWidgets.QWidget, Ui_Start):                           #  +++
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.onClicked)

    def onClicked(self):
        self.inst = MyInst()
        self.inst.show()



StyleSheet = '''
QPushButton {
    font: bold italic 16pt 'Comic Sans MS';
    background-color: white;
    width: 75px ;
    height: 50px;
    border: none;
    text-align: center;
}
QPushButton:hover {
    background: #ff0000; 
}            
QPushButton:pressed {
    background-color: blue;
}

'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(StyleSheet)                          # +++

#    Start = QtWidgets.QWidget()
#    ui = Ui_Start()
#    ui.setupUi(Start)
#    Start.show()

    w = Main()
    w.show()

    sys.exit(app.exec_())

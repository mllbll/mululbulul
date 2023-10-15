from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Inst(object):
    def setupUi(self, Inst):
        Inst.setObjectName("Ui_Inst")
        Inst.resize(1111, 883)
        self.textEdit = QtWidgets.QTextEdit(Inst)                        # (v) ???
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 1111, 41))
        self.textEdit.setObjectName("textEdit")
        self.text_inctru = QtWidgets.QTextEdit(Inst)
        self.text_inctru.setGeometry(QtCore.QRect(20, 60, 1071, 811))
        self.text_inctru.setObjectName("text_inctru")

        self.retranslateUi(Inst)
        QtCore.QMetaObject.connectSlotsByName(Inst)                      # (v) ???

    def retranslateUi(self, Inst):
        _translate = QtCore.QCoreApplication.translate
        Inst.setWindowTitle(_translate("Inst", "Inst"))
        self.textEdit.setHtml(_translate("Inst", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Инструкция</span></p></body></html>"))

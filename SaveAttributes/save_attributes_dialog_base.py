# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_attributes_dialog_base.ui'
#
# Created: Sun May 15 20:44:48 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SaveAttributesDialogBase(object):
    def setupUi(self, SaveAttributesDialogBase):
        SaveAttributesDialogBase.setObjectName(_fromUtf8("SaveAttributesDialogBase"))
        SaveAttributesDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(SaveAttributesDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.comboBox = QtGui.QComboBox(SaveAttributesDialogBase)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 181, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(SaveAttributesDialogBase)
        self.label.setGeometry(QtCore.QRect(50, 30, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SaveAttributesDialogBase)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(SaveAttributesDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(110, 80, 181, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(SaveAttributesDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(300, 80, 51, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(SaveAttributesDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), SaveAttributesDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), SaveAttributesDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveAttributesDialogBase)

    def retranslateUi(self, SaveAttributesDialogBase):
        SaveAttributesDialogBase.setWindowTitle(_translate("SaveAttributesDialogBase", "Save Attributes", None))
        self.label.setText(_translate("SaveAttributesDialogBase", "Select a layer", None))
        self.label_2.setText(_translate("SaveAttributesDialogBase", "Output file", None))
        self.pushButton.setText(_translate("SaveAttributesDialogBase", "...", None))


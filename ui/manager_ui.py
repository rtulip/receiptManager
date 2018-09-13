# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_v0.0.2.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_frame = QtGui.QFrame(self.centralwidget)
        self.btn_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.btn_frame.setObjectName(_fromUtf8("btn_frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.btn_frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.add_receipt_btn = QtGui.QPushButton(self.btn_frame)
        self.add_receipt_btn.setObjectName(_fromUtf8("add_receipt_btn"))
        self.verticalLayout.addWidget(self.add_receipt_btn)
        self.add_person_btn = QtGui.QPushButton(self.btn_frame)
        self.add_person_btn.setObjectName(_fromUtf8("add_person_btn"))
        self.verticalLayout.addWidget(self.add_person_btn)
        self.horizontalLayout.addWidget(self.btn_frame)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("background-color:white;"))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.add_receipt_btn.setText(_translate("MainWindow", "Add Receipt", None))
        self.add_person_btn.setText(_translate("MainWindow", "Add Person", None))
        self.label.setText(_translate("MainWindow", "People:", None))


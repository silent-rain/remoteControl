# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_server.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from bin.logic.server.server import Server, ServerConnect
from lib import settings
from lib.communicate import communicate
from lib.logger import logger


class Ui_Form(object):
    def __init__(self):
        # self.server = Server()
        self.server_connect = ServerConnect()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(501, 355)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 100, 80, 26))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)

        # self.server.start()
        self.server_connect.setup_ui()

    def start(self, event: bool):
        """
        启动服务
        :return:
        """
        communicate.start_server.emit(True)

    def stop(self, event: bool):
        """
        停止服务
        :return:
        """
        communicate.start_server.emit(False)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "启动"))
        self.pushButton_2.setText(_translate("Form", "停止"))

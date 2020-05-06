# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_tree.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(767, 528)
        self.dockWidget = QtWidgets.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(20, 0, 271, 481))
        self.dockWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dockWidget.setWindowTitle("")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 451))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        # self.treeWidget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        # self.treeWidget.setHeaderHidden(False)
        # self.treeWidget.setObjectName("treeWidget")

        # asdasd
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)

        # asdasd
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)

        # asd
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)

        # self.treeWidget.header().setVisible(True)


        self.horizontalLayout.addWidget(self.treeWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(340, 10, 401, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "在线主机"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "1"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("Form", "192.168.0.1"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "2"))
        self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("Form", "192.168.0.2"))

        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "分组12"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "1"))
        self.treeWidget.topLevelItem(1).child(0).setText(1, _translate("Form", "192.168.11.2"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Form", "2"))
        self.treeWidget.topLevelItem(1).child(1).setText(1, _translate("Form", "192.168.11.3"))

        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "下线主机"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Form", "1"))
        self.treeWidget.topLevelItem(2).child(0).setText(1, _translate("Form", "127.0.0.1"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Form", "2"))
        self.treeWidget.topLevelItem(2).child(1).setText(1, _translate("Form", "127.0.0.2"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("Form", "3"))
        self.treeWidget.topLevelItem(2).child(2).setText(1, _translate("Form", "127.0.0.3"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

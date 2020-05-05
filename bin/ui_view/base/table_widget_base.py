# -*- coding: utf-8 -*-
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem
from PyQt5.QtCore import Qt, QCoreApplication

_translate = QCoreApplication.translate

"""
QTableWidget 基类模块
"""


class TableWidgetBase(QTableWidget):
    def __init__(self):
        super().__init__()
        # self.headers_us = ["Id", "Date", "Level", "Message"]
        # noinspection PyArgumentList
        self.headers = [
            _translate("TableWidgetBase", "Id"),
            _translate("TableWidgetBase", "日期"),
            _translate("TableWidgetBase", "告警"),
            _translate("TableWidgetBase", "信息"),
        ]
        self.header_width = [60, 150, 80]

    def setup_ui(self) -> None:
        # self.setMinimumHeight(100)
        self.options()
        self.set_headers()

    def retranslate_ui(self) -> None:
        pass

    def options(self) -> None:
        """
        设置表格属性
        :return:
        """
        # self.setEnabled(True)
        self.setMouseTracking(True)  # 跟踪鼠标一定要先设的值
        self.setLineWidth(0)

        # 表头设置
        self.horizontalHeader().setVisible(True)  # 显示行表头
        # self.horizontalHeader().setHighlightSections(False)  # 防止表头塌陷
        self.horizontalHeader().setFixedHeight(22)  # 设置表头高度
        self.horizontalHeader().setFocusPolicy(Qt.NoFocus)  # 设置表头不可选

        self.horizontalHeader().setDefaultSectionSize(120)  # 设置tableview所有列的默认列宽
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setSortIndicatorShown(False)
        self.horizontalHeader().setStretchLastSection(True)  # 最后一栏自适应长度

        self.verticalHeader().setVisible(False)  # 隐藏列表头
        self.verticalHeader().setCascadingSectionResizes(False)
        self.verticalHeader().setSortIndicatorShown(False)
        # self.verticalHeader().setStretchLastSection(False)  # 最后一栏自适应长度

        self.setSelectionBehavior(QAbstractItemView.SelectRows)  # 按行选中
        self.setSelectionMode(QAbstractItemView.SingleSelection)  # 选中单行
        self.setShowGrid(False)  # 隐藏表格线

        # self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不允许编辑
        self.verticalHeader().setDefaultSectionSize(18)  # 设置tableview所有列的默认行高

        self.setSortingEnabled(self.isSortingEnabled())  # 排序

        self.setRowCount(0)  # 设置表格行数

        # 设置字体
        font = QFont()
        # font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(9)  # 括号里的数字可以设置成自己想要的字体大小
        self.setFont(font)

    def set_headers(self) -> None:
        """
        表头设置
        :return:
        """
        # 表头长度
        self.setColumnCount(len(self.headers))

        # 表头宽度
        for i, value in enumerate(self.header_width):
            self.setColumnWidth(i, value)

        # 表头设置
        for column, header in enumerate(self.headers):
            item = QTableWidgetItem()
            self.setHorizontalHeaderItem(column, item)
            item = self.horizontalHeaderItem(column)
            # item.setBackground(QBrush(QColor(255, 255, 255, 0)))  # 透明白，表头
            # item.setTextAlignment(Qt.AlignHCenter)  # 居中
            # noinspection PyArgumentList
            item.setText(_translate("LogInfoUI", header))

    def communicate_connect(self) -> None:
        pass

    # *************************************************

    def get_row_count(self) -> int:
        """
        获取存在数据的行数
        以ID进行检索, 遇到空行而终止
        :return:
        """
        row_count = self.rowCount()  # 获取已存在所有行
        if row_count == 0:
            return 0
        for row in range(row_count):
            id_index = self.item(row, 0)
            if id_index is None:
                row_count = row
                break
        return row_count

    def add_data(self, data_info: list) -> None:
        """
        写入数据到表格
        :param data_info:
        :return:
        """
        row = self.get_row_count()
        self.setRowCount(row + 1)

        data_info_length = len(data_info)
        headers_length = len(self.headers)
        if data_info_length < headers_length:
            data_info += ["" for _ in range(headers_length- data_info_length)]

        for column, value in enumerate(data_info):
            item = QTableWidgetItem()
            # item.setTextAlignment(Qt.AlignCenter)  # 居中
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 居左
            self.setSortingEnabled(False)
            if column == 0:
                # ID
                item.setCheckState(Qt.Unchecked)  # 设置复选框

                self.setItem(row, column, item)
                item = self.item(row, column)
                # 从1开始
                item.setText(str(row + 1))
            else:
                self.setItem(row, column, item)
                item = self.item(row, column)
                item.setText(str(value))

    def check_all_or_null(self, flag=True):
        """
        全选与全不选
        :param flag: bool
        :return:
        """
        row_count = self.get_row_count()
        if not row_count:
            # noinspection PyArgumentList
            logger_emit(logger.info(_translate("Logger", "列表为空")))
            return None

        data_count = 0
        if flag:
            for row in range(row_count):
                check = self.item(row, 0)
                check.setCheckState(Qt.Checked)
                data_count += 1
        else:
            for row in range(row_count):
                check = self.item(row, 0)
                check.setCheckState(Qt.Unchecked)
                data_count += 1
        logger_emit(logger.info(_translate("Logger", "处理: %s 条数据" % data_count)))

    def check_reverse(self):
        """
        反选
        :return:
        """
        row_count = self.get_row_count()
        if not row_count:
            # noinspection PyArgumentList
            logger_emit(logger.info(_translate("Logger", "列表为空")))
            return None
        data_count = 0
        for row in range(row_count):
            check = self.item(row, 0)
            if check.checkState() == Qt.Checked:
                check.setCheckState(Qt.Unchecked)
            else:
                check.setCheckState(Qt.Checked)
                data_count += 1
        logger_emit(logger.info(_translate("Logger", "处理: %s 条数据" % data_count)))

    def del_check(self):
        """
        删除已选信息
        :return:
        """
        row_count = self.get_row_count()
        if not row_count:
            # noinspection PyArgumentList
            logger_emit(logger.info(_translate("Logger", "列表为空")))
            return None

        data_count = 0
        for row in range(row_count - 1, -1, -1):
            check = self.item(row, 0)
            if check.checkState() == Qt.Checked:
                self.removeRow(row)
                data_count += 1
        logger_emit(logger.info(_translate("Logger", "处理: %s 条数据" % data_count)))
        # 重置编号
        self.reset_number()

    def empty_all(self):
        """
        清空列表
        :return:
        """
        row_count = self.get_row_count()
        if not row_count:
            return None

        # 方案一：
        # j = 0
        # while True:
        #     if self.rowCount() == 0:
        #         break
        #     self.removeRow(row_count - j)
        #     j += 1
        del_count = 0
        for row in range(row_count - 1, -1, -1):
            self.removeRow(row)
            del_count += 1
        self.setRowCount(20)
        logger_emit(logger.info(_translate("Logger", "处理: %s 条数据" % del_count)))

    def get_all_data(self):
        """
        获取所有数据 [[],[]]
        :return: list
        """
        row_count = self.get_row_count()
        if not row_count:
            return None

        data_info = []
        for row in range(row_count):
            column_list = []
            for column in range(len(self.headers)):
                text = self.item(row, column).text()
                column_list.append(text)
            data_info.append(column_list)
        return data_info

    def get_check_data(self):
        """
        获取选中的数据
        ["id", "username", "password", "cookies", "status"]
        :return: list [[],]
        """
        row_count = self.get_row_count()
        if not row_count:
            return []
        data_info = []
        for row in range(row_count):
            check = self.item(row, 0)
            if check.checkState() == Qt.Checked:
                column_list = []
                for column in range(len(self.headers)):
                    try:
                        text = self.item(row, column).text()
                        column_list.append(text)
                    except AttributeError:
                        column_list.append("")
                data_info.append(column_list)
        logger_emit(logger.info(_translate("Logger", "处理: %s 条数据" % len(data_info))))
        return data_info

    def add_data1(self, data_info):
        """
        写入数据到表格
        :param data_info: list
        :return:
        """
        row_count = self.get_row_count()
        self.setRowCount(row_count + 1)

        row = row_count
        for column, value in enumerate(data_info):
            item = QTableWidgetItem()
            # item.setTextAlignment(Qt.AlignCenter)  # 居中
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 居左
            __sortingEnabled = self.isSortingEnabled()
            self.setSortingEnabled(False)
            if column == 0:
                item.setCheckState(Qt.Unchecked)  # 设置复选框

                self.setItem(row, column, item)
                item = self.item(row, column)
                item.setText(_translate("InfoTableWidget", str(row + 1)))

            else:
                self.setItem(row, column, item)
                item = self.item(row, column)
                item.setText(_translate("InfoTableWidget", str(value)))
            self.setSortingEnabled(__sortingEnabled)

    def add_data_no_check(self, data_info):
        """
        写入数据到表格
        :param data_info: list
        :return:
        """
        row_count = self.get_row_count()
        self.setRowCount(row_count + 1)

        if len(data_info) < len(self.headers):
            data_info += ["" for _ in self.headers[:len(self.headers) - len(data_info)]]

        row = row_count
        for column, value in enumerate(data_info):
            item = QTableWidgetItem()
            # item.setTextAlignment(Qt.AlignCenter)  # 居中
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 居左
            self.setSortingEnabled(False)
            if column == 0:
                self.setItem(row, column, item)
                item = self.item(row, column)
                item.setText(_translate("InfoTableWidget", str(row + 1)))
            else:
                self.setItem(row, column, item)
                item = self.item(row, column)
                item.setText(_translate("InfoTableWidget", str(value)))

    def reset_number(self):
        """
        重置编号
        :return:
        """
        # 获取行数
        row_count = self.get_row_count()
        if not row_count:
            return None

        for row in range(row_count):
            item = self.item(row, 0)
            item.setText(str(row + 1))

    def get_data_index(self, row):
        """
        获取指定行的数据
        :param row: index
        :return: list
        """
        row_count = self.get_row_count()
        if not row_count:
            return None

        data_info = []
        for column, value in enumerate(self.headers_us):
            text = self.item(row, column).text()
            data_info.append(text)
        return data_info

    def update_data_index(self, data_info, row):
        """
        更新数据
        :param data_info: list []
        :param row: 行索引
        :return:
        """
        for column, value in enumerate(data_info):
            if column == 0:
                continue
            item = self.item(int(row), column)
            if not value:
                continue
            item.setText(str(value))

    def del_data_index(self, row):
        """
        索引删除数据
        :param row:
        :return:
        """
        self.removeRow(int(row))

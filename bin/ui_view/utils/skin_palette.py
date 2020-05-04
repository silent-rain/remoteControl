# -*- coding: utf-8 -*-
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGroupBox, QWidget, QGridLayout, QLabel, QSlider, QFrame, QPushButton, QDialog
from PyQt5.QtCore import Qt, QRect, QMetaObject
from PyQt5.QtCore import QCoreApplication

_translate = QCoreApplication.translate

"""
皮肤调色模块
"""


class HSB(object):
    def __init__(self, grid_layout_widget: QWidget, grid_layout: QGridLayout):
        self.grid_layout_widget = grid_layout_widget
        self.grid_layout = grid_layout

        self.hsb = QGroupBox(self.grid_layout_widget)
        self.hsb_grid_layout_widget = QWidget(self.hsb, Qt.WindowFlags())
        self.hsb_grid_layout = QGridLayout(self.hsb_grid_layout_widget)

        self.hue = QLabel(self.hsb_grid_layout_widget)
        self.saturation = QLabel(self.hsb_grid_layout_widget)
        self.brightness = QLabel(self.hsb_grid_layout_widget)
        self.hue_slider = QSlider(self.hsb_grid_layout_widget)
        self.saturation_slider = QSlider(self.hsb_grid_layout_widget)
        self.brightness_slider = QSlider(self.hsb_grid_layout_widget)

    def setup_ui(self) -> None:
        self.hsb.setObjectName("hsb")
        self.hsb_grid_layout_widget.setObjectName("hsb_grid_layout_widget")
        self.hsb_grid_layout.setObjectName("hsb_grid_layout")

        self.hue.setObjectName("hue")
        self.saturation.setObjectName("saturation")
        self.brightness.setObjectName("brightness")
        self.hue_slider.setObjectName("hue_slider")
        self.saturation_slider.setObjectName("saturation_slider")
        self.brightness_slider.setObjectName("brightness_slider")

        # self.hsb_grid_layout_widget.setGeometry(QRect(0, 20, 320, 120))
        self.hsb_grid_layout.setContentsMargins(5, 5, 5, 5)
        self.hsb.setLayout(self.hsb_grid_layout)

        self.hue_slider.setOrientation(Qt.Horizontal)
        self.saturation_slider.setOrientation(Qt.Horizontal)
        self.brightness_slider.setOrientation(Qt.Horizontal)

        self.hsb_grid_layout.addWidget(self.hue, 0, 0, 1, 1)
        self.hsb_grid_layout.addWidget(self.saturation, 1, 0, 1, 1)
        self.hsb_grid_layout.addWidget(self.brightness, 2, 0, 1, 1)

        self.hsb_grid_layout.addWidget(self.hue_slider, 0, 1, 1, 1)
        self.hsb_grid_layout.addWidget(self.saturation_slider, 1, 1, 1, 1)
        self.hsb_grid_layout.addWidget(self.brightness_slider, 2, 1, 1, 1)

        self.grid_layout.addWidget(self.hsb, 0, 0, 1, 1)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.hsb.setTitle(_translate("SkinPaletteView", "HSB调整"))
        self.hue.setText(_translate("SkinPaletteView", "色相:"))
        self.saturation.setText(_translate("SkinPaletteView", "饱和:"))
        self.brightness.setText(_translate("SkinPaletteView", "亮度:"))


class Aero(object):
    def __init__(self, grid_layout_widget: QWidget, grid_layout: QGridLayout):
        self.grid_layout_widget = grid_layout_widget
        self.grid_layout = grid_layout

        self.aero = QGroupBox(self.grid_layout_widget)
        self.aero_grid_layout_widget = QWidget(self.aero, Qt.WindowFlags())
        self.aero_grid_layout = QGridLayout(self.aero_grid_layout_widget)

        self.alpha = QLabel(self.aero_grid_layout_widget)
        self.shadow_size = QLabel(self.aero_grid_layout_widget)
        self.shadow_sharp = QLabel(self.aero_grid_layout_widget)
        self.alpha_slider = QSlider(self.aero_grid_layout_widget)
        self.shadow_size_slider = QSlider(self.aero_grid_layout_widget)
        self.shadow_sharp_slider = QSlider(self.aero_grid_layout_widget)

    def setup_ui(self) -> None:
        self.aero.setObjectName("aero")
        self.aero_grid_layout_widget.setObjectName("aero_grid_layout_widget")
        self.aero_grid_layout.setObjectName("aero_grid_layout")

        self.alpha.setObjectName("alpha")
        self.shadow_size.setObjectName("shadow_size")
        self.shadow_sharp.setObjectName("shadow_sharp")
        self.alpha_slider.setObjectName("alpha_slider")
        self.shadow_size_slider.setObjectName("shadow_size_slider")
        self.shadow_sharp_slider.setObjectName("shadow_sharp_slider")

        # self.aero_grid_layout_widget.setGeometry(QRect(0, 20, 321, 121))
        self.aero_grid_layout.setContentsMargins(5, 5, 5, 5)

        self.alpha_slider.setOrientation(Qt.Horizontal)
        self.shadow_size_slider.setOrientation(Qt.Horizontal)
        self.shadow_sharp_slider.setOrientation(Qt.Horizontal)

        self.aero_grid_layout.addWidget(self.alpha, 0, 0, 1, 1)
        self.aero_grid_layout.addWidget(self.shadow_size, 1, 0, 1, 1)
        self.aero_grid_layout.addWidget(self.shadow_sharp, 2, 0, 1, 1)

        self.aero_grid_layout.addWidget(self.alpha_slider, 0, 1, 1, 1)
        self.aero_grid_layout.addWidget(self.shadow_size_slider, 1, 1, 1, 1)
        self.aero_grid_layout.addWidget(self.shadow_sharp_slider, 2, 1, 1, 1)

        self.aero.setLayout(self.aero_grid_layout)
        self.grid_layout.addWidget(self.aero, 0, 1, 1, 1)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.aero.setTitle(_translate("SkinPaletteView", "Aero 调整"))
        self.alpha.setText(_translate("SkinPaletteView", "Alpha:"))
        self.shadow_size.setText(_translate("SkinPaletteView", "暗影大小"))
        self.shadow_sharp.setText(_translate("SkinPaletteView", "暗影锐利"))


class Shadow(object):
    def __init__(self, grid_layout_widget: QWidget, grid_layout: QGridLayout):
        self.grid_layout_widget = grid_layout_widget
        self.grid_layout = grid_layout
        self.shadow_adjustment = QGroupBox(self.grid_layout_widget)
        self.shadow_grid_layout_widget = QWidget(self.shadow_adjustment, Qt.WindowFlags())
        self.shadow_grid_layout = QGridLayout(self.shadow_grid_layout_widget)

        self.shadow_dark = QLabel(self.shadow_grid_layout_widget)
        self.shadow_color_r = QLabel(self.shadow_grid_layout_widget)
        self.shadow_color_b = QLabel(self.shadow_grid_layout_widget)
        self.shadow_color_g = QLabel(self.shadow_grid_layout_widget)

        self.shadow_dark_slider = QSlider(self.shadow_grid_layout_widget)
        self.shadow_color_r_slider = QSlider(self.shadow_grid_layout_widget)
        self.shadow_color_b_slider = QSlider(self.shadow_grid_layout_widget)
        self.shadow_color_g_slider = QSlider(self.shadow_grid_layout_widget)

    def setup_ui(self) -> None:
        self.shadow_adjustment.setObjectName("shadow_adjustment")
        self.shadow_grid_layout_widget.setObjectName("shadow_grid_layout_widget")
        self.shadow_grid_layout.setObjectName("shadow_grid_layout")

        self.shadow_dark.setObjectName("shadow_dark")
        self.shadow_color_r.setObjectName("shadow_color_r")
        self.shadow_color_b.setObjectName("shadow_color_b")
        self.shadow_color_g.setObjectName("shadow_color_g")
        self.shadow_dark_slider.setObjectName("shadow_dark_slider")
        self.shadow_color_r_slider.setObjectName("shadow_color_r_slider")
        self.shadow_color_b_slider.setObjectName("shadow_color_b_slider")
        self.shadow_color_g_slider.setObjectName("shadow_color_g_slider")

        # self.shadow_grid_layout_widget.setGeometry(QRect(0, 0, 650, 130))
        self.shadow_grid_layout.setContentsMargins(5, 5, 5, 5)

        self.shadow_grid_layout.addWidget(self.shadow_dark, 0, 0, 1, 1)
        self.shadow_grid_layout.addWidget(self.shadow_color_r, 1, 0, 1, 1)
        self.shadow_grid_layout.addWidget(self.shadow_color_b, 1, 2, 1, 1)
        self.shadow_grid_layout.addWidget(self.shadow_color_g, 0, 2, 1, 1)

        self.shadow_dark_slider.setOrientation(Qt.Horizontal)
        self.shadow_color_r_slider.setOrientation(Qt.Horizontal)
        self.shadow_color_b_slider.setOrientation(Qt.Horizontal)
        self.shadow_color_g_slider.setOrientation(Qt.Horizontal)

        self.shadow_grid_layout.addWidget(self.shadow_color_r_slider, 1, 1, 1, 1)
        self.shadow_grid_layout.addWidget(self.shadow_dark_slider, 0, 1, 1, 1)
        self.shadow_grid_layout.addWidget(self.shadow_color_g_slider, 0, 3, 1, 1)
        self.shadow_grid_layout.addWidget(self.shadow_color_b_slider, 1, 3, 1, 1)

        self.shadow_adjustment.setLayout(self.shadow_grid_layout)
        self.grid_layout.addWidget(self.shadow_adjustment, 1, 0, 1, 2)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.shadow_adjustment.setTitle(_translate("SkinPaletteView", "阴影调整"))
        self.shadow_dark.setText(_translate("SkinPaletteView", "暗影黑暗:"))
        self.shadow_color_b.setText(_translate("SkinPaletteView", "阴影色 B"))
        self.shadow_color_g.setText(_translate("SkinPaletteView", "阴影色 G:"))
        self.shadow_color_r.setText(_translate("SkinPaletteView", "阴影色 R:"))


class Other(object):
    def __init__(self, grid_layout_widget: QWidget, grid_layout: QGridLayout):
        self.grid_layout_widget = grid_layout_widget
        self.grid_layout = grid_layout

        self.frame = QFrame(self.grid_layout_widget, Qt.WindowFlags())
        self.reset = QPushButton(self.frame)
        self.save = QPushButton(self.frame)

    def setup_ui(self) -> None:
        self.frame.setObjectName("frame")
        self.reset.setObjectName("reset")
        self.save.setObjectName("save")

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.reset.setGeometry(QRect(400, 30, 80, 30))
        self.save.setGeometry(QRect(500, 30, 80, 30))
        self.grid_layout.addWidget(self.frame, 2, 0, 1, 2)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.reset.setText(_translate("SkinPaletteView", "重置"))
        self.save.setText(_translate("SkinPaletteView", "保存"))


class SkinPaletteView(object):
    def __init__(self, main_window):
        # self.widget_window = QDialog(main_window)
        self.widget_window = main_window
        self.gridLayoutWidget = QWidget(self.widget_window, Qt.WindowFlags())
        self.gridLayout = QGridLayout(self.gridLayoutWidget)

        self.ui_view_list = []

    def add_ui_view(self, view: object) -> None:
        if view not in self.ui_view_list:
            self.ui_view_list.append(view)

    def setup_ui(self) -> None:
        self.widget_window.setObjectName("Form")
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout.setObjectName("gridLayout")

        self.widget_window.setFixedSize(650, 300)
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 650, 300))
        self.gridLayout.setContentsMargins(5, 5, 5, 5)

        # noinspection PyArgumentList,PyCallByClass
        QMetaObject.connectSlotsByName(self.widget_window)

        font = QFont()
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)

        self.add_ui_view(HSB(self.gridLayoutWidget, self.gridLayout))
        self.add_ui_view(Aero(self.gridLayoutWidget, self.gridLayout))
        self.add_ui_view(Shadow(self.gridLayoutWidget, self.gridLayout))
        self.add_ui_view(Other(self.gridLayoutWidget, self.gridLayout))

        for view in self.ui_view_list:
            view.setup_ui()
            view.retranslate_ui()

        # 背景色
        self.set_window_background()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.widget_window.setWindowTitle(_translate("SkinPaletteView", "皮肤调色板"))

    def set_window_background(self) -> None:
        """
        设置背景: 背景色
        :return:
        """
        # 导航栏透明(linux无效): border-top-color: transparent;
        # 背景透明(linux背景漆黑): background:transparent;
        # 边框透明(linux无效果): border: transparent;
        # 背景色: background-color: rgb(100, 200, 255);

        # 整体背景
        # 如果设置背景色,透明失效
        # self.main_window.setStyleSheet("background-color: rgb(100, 200, 255);")
        self.widget_window.setStyleSheet("background-color: rgb(107, 173, 246);")

        # 不显示标题栏，亦无边框
        # 无法移动
        # self.main_window.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)

        # 设置背景（全透明）
        # 如果设置背景色,透明失效
        # 效果为一般为漆黑
        # self.main_window.setAttribute(Qt.WA_TranslucentBackground, True)

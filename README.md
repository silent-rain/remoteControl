# 部署
## windows 10 
- 安装 python3.7
- 安装库
    - pyaudio 需要编译环境才能安装
    - 安装编译好的pyaudio： 
        - 下载地址：[pyaudio](https://download.lfd.uci.edu/pythonlibs/s2jqpv5t/PyAudio-0.2.11-cp38-cp38-win_amd64.whl)
        - pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl
    - 安装其他库:
        - pip install -r requirements.txt
- 运行：
    python run.py


# 程序模块
## 菜单栏
### 选项
- [ ] 程序设置
- [ ] 创建客户端
- [x] 皮肤调节
- [x] 退出程序
### 查看
- [x] 分组信息
- [x] 工具扩展
- [x] 工具导航
- [x] 状态栏
### 帮助
- [x] 关于

## 工具导航栏
- [x] 服务器开关
- [ ] 文件管理
- [ ] 远程终端
- [ ] 远程控制
- [ ] 视频监控
- [ ] 语音监控
- [ ] 键盘记录
- [ ] 创建客户端
- [ ] 服务管理
- [x] 退出程序

## 主机信息
### 分组信息
- [x] 默认两个分类
- [x] 上线主机(count)
- [x] 下线主机(count)
- [x] 选中分组,信息展示刷新数据
### 分组信息右键菜单
- [x] 增加分组
- [x] 修改分组
- [x] 删除分组

### 信息展示
- [x] Id
- [x] 外网
- [x] 内网
- [x] 计算机
- [x] 操作系统
- [x] 处理器 win
- [x] 内存 win
- [x] 硬盘容量 win
- [x] 显卡 Y/N
- [x] 视频 Y/N
- [x] 语音 Y/N
- [x] 开机时间
- [ ] 服务版本
- [ ] 分组
- [x] 区域
- [x] 备注
### 列表右键菜单
服务器开关
文件管理
远程终端
远程控制
视频监控
语音监控
键盘记录
创建客户端
服务管理
进程管理
远程交谈
弹窗信息

## 工具扩展
- [x] 日志模块
- [ ] 批量操作

## 状态栏
- [x] 显示当前时间
- [x] 网络上传/下载速度
- [ ] 监听端口  与设置同步
- [x] 上线主机台数

# 更新日志
## 2020.05.10
- 客户端上线信息完善
- 客户端生成配置
- 只允许运行一个客户端

## 2020.05.09
- 皮肤window下窗口阻塞bug修复
- window下背景颜色bug，已经注销，待处理
- window下肤色调节优化

## 2020.05.08
- 添加客户端,服务端模块,解决粘包问题
- 主机上下线模块完善

## 2020.05.07
- 分组信息-状态栏信号完善
- about 窗口完善
- 皮肤调节信息完善
- 添加数据库模块
- 主机下线模块完善

## 2020.05.06
- 添加工具栏组件框架
- 工具扩展子类信号修改
- 工具导航栏-退出程序,完善
- 配置处理,新增配置文件保存本地注释不丢失,配置文件在线更新
- 添加分组信息模块,信息展示模块
- 分组节点完善
- 分组信息右键菜单
- 分组信息 -> 信息展示
- 添加音频模块

## 2020.05.05
- 皮肤模块完善
- 颜色bug修复
- 日志模块
- 日志模块-qt数据传输
- 皮肤窗口关闭信号,销毁窗口
- 加载效果模块(透明度)
- 皮肤窗口加载效果
- 程序启动效果
- UI 重定义

## 2020.05.04
- 创建三个显示模块:主窗口,菜单栏,工具栏,状态栏
- 设置信息模块
- 修复配置文件转换bug
- 优化单例模式
- 模块名优化
- 添加皮肤模块,尚未引用
- 添加扩展模块框架: 日志模块,批量操作模块
- 添加菜单栏框架
- 添加状态栏框架
- 完善菜单栏中的显示模块信号机制
- 添加显示日志模块
- 日志待解析


# 报错集合
## qt.qpa.xcb: QXcbConnection: XCB error: 8 (BadMatch), sequence: 770, resource id: 136314920, major code: 130 (Unknown), minor code: 3
sudo apt-get install qt5-default qtbase5-dev qttools5-dev-tools

## warning: LF will be replaced by CRLF in
### 简介
- 问题出在不同操作系统所使用的换行符是不一样的，下面罗列一下三大主流操作系统的换行符：
- Uinx/Linux采用换行符LF表示下一行（LF：LineFeed，中文意思是换行）；
- Dos和Windows采用回车+换行CRLF表示下一行（CRLF：CarriageReturn LineFeed，中文意思是回车换行）；
- Mac OS采用回车CR表示下一行（CR：CarriageReturn，中文意思是回车）。
### 解决
- 为true时，Git会将你add的所有文件视为文本问价你，将结尾的CRLF转换为LF，而checkout时会再将文件的LF格式转为CRLF格式。
- 为false时，line endings不做任何改变，文本文件保持其原来的样子。
- 为input时，add时Git会把CRLF转换为LF，而check时仍旧为LF，所以Windows操作系统不建议设置此值。
git config --global core.autocrlf true


# HTML颜色:
- 导航栏透明(linux无效): 
    border-top-color: transparent;
- 背景透明(linux背景漆黑): 
    background:transparent;
- 边框透明(linux无效果): 
    border: transparent;
- 背景色: 
    background-color: rgb(100, 200, 255);
- 图片背景: 
    background-image: url(:/images/background.png);
- 背景颜色,渐变色：
    background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgba(255, 255, 255, 100%),stop: 1 rgba(10, 144, 255, 100%));
- 按钮颜色: 
    QPushButton { background-color: rgb(255, 85, 0); color: rgb(85, 255, 0); };


# 窗口调节
## setWindowOpacity(0.6)
- 窗体的透明度
- 透明度的有效范围从1.0(完全不透明)到0.0(完全透明的)
- 这个特性可以在嵌入式Linux、Mac OS X、Windows、和X11平台上使用
- 此功能不可用在Windows CE
- 注意：
    - 半透明的windows更新和调整明显慢于不透明的窗口（透明窗体的刷新速度会变慢）
    - QDockWidget：悬浮后 window下会失效


# 资料备份
## 背景色的使用，以及窗口事件
```
class MainWindowUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        主窗口
        :param main_window:
        """
        self.main_window = main_window

        # 创建调色板
        self.palette = QPalette()
        # 颜色初始化
        # self.color_init = QColor(107, 173, 246)
        self.color_init = QColor(*settings.SKIN_COLOR)

    def setup_ui(self) -> None:
        self.main_window.setObjectName("main_window")
        self.main_window.resize(850, 500)

        # noinspection PyArgumentList,PyCallByClass
        QMetaObject.connectSlotsByName(self.main_window)

        self.set_window_icon()
        # self.set_window_background()
        # self.set_window_background4()
        self.center()
        # self.main_window.resizeEvent = self.resize_event
        # self.main_window.closeEvent = self.close_event  # 放在信号区

        # 隐藏工具栏上的右键菜单
        # self.main_window.setContextMenuPolicy(Qt.NoContextMenu)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.main_window.setWindowTitle(_translate("MainWindowUI", "远程协助"))

    def set_window_icon(self) -> None:
        """
        设置窗口的图标
        引用资源 qtResource.py
        :return:
        """
        self.main_window.setWindowIcon(QIcon(settings.MAIN_UI["app"]))

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
        # self.main_window.setStyleSheet("background-color: rgb(107, 173, 246);")
        self.main_window.setStyleSheet("background-color: rgb{};".format(self.color_init.getRgb()[:3]))

        # 不显示标题栏，亦无边框
        # 无法移动
        # self.main_window.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)

        # 设置背景（全透明）
        # 如果设置背景色,透明失效
        # 效果为一般为漆黑
        # self.main_window.setAttribute(Qt.WA_TranslucentBackground, True)

        #  设置透明用
        # self.main_window.setWindowOpacity(0.5)

    def set_window_background2(self) -> None:
        """
        设置背景: 填充图片
        :return:
        """
        # 图片背景: background-image: url(:/images/background.png);
        self.main_window.setStyleSheet("background-image: url({0});".format(settings.MAIN_UI["background"]))
        # 自动填充背景
        # self.main_window.setAutoFillBackground(False)

    def set_window_background3(self, event: QResizeEvent = None) -> None:
        """
        设置背景: 平铺图片
        :return:
        """
        palette = QPalette()
        # 需要png格式，jpg失败！
        # pix = QPixmap("../src/image/background.jpg")  # 直接使用
        pix = QPixmap(settings.MAIN_UI["background"])  # 打包资源
        # pix = pix.scaled(self.main_window.width(), self.main_window.height())
        if event:
            # 窗口变化,重新获取窗口大小
            pix = pix.scaled(event.size())
        else:
            # 平铺
            pix = pix.scaled(self.main_window.size())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.main_window.setPalette(palette)

    def set_window_background4(self) -> None:
        """
        使用调色板
        :return:
        """
        # self.main_window.setAutoFillBackground(True)
        self.main_window.setWindowOpacity(0.5)
        # self.main_window.setAttribute(Qt.WA_TranslucentBackground)
        # self.color_init.setAlpha(0.3)
        # # https://blog.csdn.net/addfourliu/article/details/6730688?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1
        self.palette.setColor(QPalette.Background, self.color_init)  # 给调色板设置颜色
        # self.palette.setColor(QPalette.Background, Qt.transparent)  # 给调色板设置颜色
        self.main_window.setPalette(self.palette)  # 给控件设置颜色

    def center(self) -> None:
        """
        控制窗口显示在屏幕中心
        :return:
        """
        # 获得窗口
        qr = self.main_window.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.main_window.move(qr.topLeft())

    def resize_event(self, event: QResizeEvent) -> None:
        """
        重置窗口事件
        :param event:
        :return:
        """
        self.set_window_background3(event)

        # noinspection PyArgumentList

    def close_event(self, event: QCloseEvent) -> None:
        """
        重置退出事件
        退出消息提示框
        直接继承main_window的背景色
        :param event:
        :return:
        """
        # self.message_box = QMessageBox(self.main_window)
        # 标题图标
        # msg.setWindowIcon(QIcon(settings.mainUi["confirm"]))

        # 设置背景图片
        # 背景图片： "background-image: url(:/image/mainUi/background.png);"
        # msg.setStyleSheet("background-image: url({0});".format(settings.mainUi["background"]))
        message_box = QMessageBox(self.main_window)
        # noinspection PyArgumentList
        reply = message_box.information(
            self.main_window,
            _translate("MainWindowUI", "温馨提示"),
            _translate("MainWindowUI", "您确认要退出???"),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            # self.communicate.server_status.emit(False)  # 程序退出后关闭服务器
            # self.communicate.log_info.emit(self.logger.info("正在关闭服务器..."))
            # self.communicate.log_info.emit(self.logger.info("程序退出..."))
            event.accept()
        else:
            event.ignore()

```

# -*- coding: utf-8 -*-
import os
from lib.basePath import BASE_PATH
from lib import qtResource  # 资源文件
from lib import fix_qt_import_error  # Qt打包错误解决

# 系统图标
MAIN_UI = {
    "app": ':/images/mainUi/app.png',
    "background": ':/images/mainUi/background.png',
    "confirm": ':/images/mainUi/confirm.png',
}

# 菜单图标
MENUBAR_UI = {
    "about": ':/images/menubar/about.png',
    "save": ':/images/menubar/save.png',
    "exit": ':/images/menubar/exit.png',
}

# 工具导航栏
TOOLBAR_UI = {
    "host": ':/images/toolsMain/host.png',
    "startServer": ':/images/toolsMain/startServer.png',
    "file": ':/images/toolsMain/file.png',
    "desktop": ':/images/toolsMain/desktop.png',
    "video_monitor": ':/images/toolsMain/videoMonitor.png',
    "voice_monitor": ':/images/toolsMain/voiceMonitor.png',
    "keyboard": ':/images/toolsMain/keyboard.png',
    "terminal": ':/images/toolsMain/terminal.png',
    "DDos": ':/images/toolsMain/DDos.png',
    "client": ':/images/toolsMain/client.png',
    "filtrate": ':/images/toolsMain/filtrate.png',
    "service_manage": ':/images/toolsMain/serviceManage.png',
    "registry": ':/images/toolsMain/registry.png',
    "exit": ':/images/toolsMain/exit.png',
    "stopServer": ':/images/toolsMain/stopServer.png',
}

# 设置
options = {
    "release_dir": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "release")),  # 编译文件目录
    # {{client打包配置
    "client_icon": os.path.abspath(os.path.join(BASE_PATH, "src/images/app.ico")),  # 程序图标
    "client_dir": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "release/client")),  # 客户端存放目录
    "client_make": os.path.abspath(os.path.join(BASE_PATH, "core/logicalCode/client/client.py")),  # 客户端文件
    "client_temp": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "release/client/temp")),  # 临时文件夹
    "client_dist_path": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "release/client")),  # 编译存放位置
    "client_name": "suchost",
    # }}

    # {{server打包配置
    "server_icon": os.path.abspath(os.path.join(BASE_PATH, "src/images/app.ico")),  # 程序图标
    "server_dir": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "release/server")),  # 服务端存放目录
    "server_make": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "server/run.py")),  # 服务端文件
    "server_temp": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "release/server/temp")),  # 临时文件夹
    "server_dist_path": os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), "release/server")),  # 编译存放位置
    "server_name": "远程控制",
    # }}
}

# 日志配置
LOG_DIR = os.path.abspath(os.path.join(BASE_PATH, "logs"))  # 日志文件夹
os.mkdir(LOG_DIR) if not os.path.exists(LOG_DIR) else None  # 初始化日志文件夹

# 系统配置
CONF_DIR = os.path.abspath(os.path.join(BASE_PATH, "conf"))  # 配置文件夹
os.mkdir(CONF_DIR) if not os.path.exists(CONF_DIR) else None  # 初始化配置文件夹
CONFIG_FILE = os.path.abspath(os.path.join(BASE_PATH, "conf", "config.ini"))  # 外部配置文件

# 资源配置
SRC_DIR = os.path.abspath(os.path.join(BASE_PATH, "src"))  # 资源文件夹
os.mkdir(SRC_DIR) if not os.path.exists(SRC_DIR) else None  # 初始化资源文件夹
DATA_DB = os.path.abspath(os.path.join(BASE_PATH, "src", "data.db"))  # 数据库

# 语音配置
SOUND_DIR = os.path.abspath(os.path.join(BASE_PATH, "src", "sound"))  # 音频资源文件夹
os.mkdir(SOUND_DIR) if not os.path.exists(SOUND_DIR) else None  # 初始化音频资源文件夹
SOUND_OFFLINE = os.path.abspath(os.path.join(BASE_PATH, "src", "sound", "offline.wav"))  # 下线
SOUND_ONLINE = os.path.abspath(os.path.join(BASE_PATH, "src", "sound", "online.wav"))  # 上线
SOUND_SETTING = os.path.abspath(os.path.join(BASE_PATH, "src", "sound", "setting.wav"))  # 自动上线设置

# 调试模式
DEBUG = False

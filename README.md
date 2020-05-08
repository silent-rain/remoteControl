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
- [ ] 服务器开关
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
Id
外网
内网
计算机
操作系统
处理器
内存
硬盘容量
视频
语音
开机时间
服务版本
区域
备注
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
- [ ] 监听端口
- [x] 上线主机台数

# 更新日志
## 2020.05.09
- 皮肤window下窗口阻塞bug修复
- window下背景颜色bug，已经注销，待处理

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


## 报错集合
### qt.qpa.xcb: QXcbConnection: XCB error: 8 (BadMatch), sequence: 770, resource id: 136314920, major code: 130 (Unknown), minor code: 3
sudo apt-get install qt5-default qtbase5-dev qttools5-dev-tools

## HTML颜色:
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

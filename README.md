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



# 更新日志
## 20200504
- 创建三个显示模块:主窗口,菜单栏,工具栏,状态栏
- 设置信息模块
- 修复配置文件转换bug
- 优化单例模式
- 模块名优化
- 添加皮肤模块,尚未引用
- 添加扩展模块框架: 日志模块,批量操作模块
- 添加菜单栏框架



def loading():
    """
    :return:
    """
    splash = QSplashScreen()
    # splash.setPixmap(QPixmap(":/images/loading.png"))
    splash.setPixmap(QPixmap(settings.MAIN_UI["loading"]))
    splash.show()
    top_right = Qt.AlignRight | Qt.AlignTop
    splash.showMessage("正在启动中", top_right, Qt.white)

    # QSplashScreen * splash = new QSplashScreen;
    # splash->setPixmap(QPixmap(“: / images / start.png”));
    # splash->show();

    # Qt::Alignment
    # top_right = Qt::AlignRight | Qt::AlignTop;
    # splash->showMessage(“正在启动中”, top_right, Qt::white);
    # mainWindows
    # window;
    # window.show();
    # splash->finish( & window);
    # delete
    # splash

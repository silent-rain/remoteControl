import base64


def file_to_py(filename: str, py_name: str) -> None:
    """
    将文件转化为py文件变量
    :param filename: 传入文件
    :param py_name: 输出文件
    :return:
    """
    # new_filename = filename.replace('.', '_')
    new_filename = "DATA"
    open_pic = open("%s" % filename, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    data = '%s = "%s"\n' % (new_filename, b64str.decode())

    with open(py_name, 'w', encoding='utf-8') as f:
        f.write(data)


def py_to_file(filename: str, content: str) -> None:
    """
    解密内容
    :param filename: 文件
    :param content: 内容
    :return:
    """
    with open(filename, "wb") as f:
        f.write(base64.b64decode(content))


if __name__ == '__main__':
    # 保存文件
    # path = "../conf/config.ini"
    # file_to_py(path, 'initConfig.py')

    # 恢复文件
    path = "../conf/config555.ini"
    from lib.config.config_init import CONFIG_DATA
    py_to_file(path, CONFIG_DATA)

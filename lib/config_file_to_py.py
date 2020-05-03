import base64


def file_to_py(filename, py_name):
    # new_filename = filename.replace('.', '_')
    new_filename = "CONFIG_DATA"
    open_pic = open("%s" % filename, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    data = '%s = "%s"\n' % (new_filename, b64str.decode())

    with open(py_name, 'w', encoding='utf-8') as f:
        f.write(data)


def config_py_to_file(filename, filename_text):
    with open(filename, "wb") as f:
        f.write(base64.b64decode(filename_text))


if __name__ == '__main__':
    # 保存文件
    # path = "../conf/config.ini"
    # file_to_py(path, 'initConfig.py')

    # 恢复文件
    path = "../conf/config.ini"
    from lib.config_init import CONFIG_DATA
    config_py_to_file(path, CONFIG_DATA)

# -*- coding: utf-8 -*-
import configparser

"""
读取本地配置文件
"""


class NewConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr


class ReadConfig(object):
    _instance = None

    def __init__(self, config_path):
        self.config = NewConfigParser()
        self.config_path = config_path
        # self.config_path = settings.options.get("config", "config.ini")

    def file_encoding(self):
        """
        编码格式
        :return:
        """
        config_path = self.config_path
        try:
            self.config.read(config_path, encoding="utf-8")
        except UnicodeDecodeError:
            self.config.read(config_path, encoding="gbk")
        
    def read(self):
        """
        读取配置文件
        :return:
        """
        section_values = {}
        sections = self.config.sections()
        for section in sections:
            options = self.config.options(section)
            # print(section)
            # print(options)
            option_values = {}
            for option in options:
                value = self.config.get(section, option)
                option_values[option] = value
            section_values[section] = option_values

        # print(option_values)
        return section_values

    def start(self):
        self.file_encoding()
        return self.read()


class WriterConfig(object):
    _instance = None

    def __init__(self, config_path):
        self.config = NewConfigParser()
        self.config_path = config_path
        # self.config_path = settings.options.get("config", "config.ini")

    def file_encoding(self):
        """
        编码格式
        :return:
        """
        config_path = self.config_path
        try:
            self.config.read(config_path, encoding="utf-8")
        except UnicodeDecodeError:
            self.config.read(config_path, encoding="gbk")

    def writer(self, section_values):
        """
        保存配置文件
        :param section_values: dict
        :return:
        """
        for section in section_values:
            self.config.add_section(section)
            option_values = section_values[section]
            for option in option_values:
                self.config.set(section, option, option_values[option])

    def save(self):
        """
        保存
        :return:
        """
        with open(self.config_path, "w") as f:
            self.config.write(f)

    def start(self, section_values):
        """
        开始运行
        :param section_values: dict
        :return:
        """
        # self.file_encoding()
        self.writer(section_values)
        self.save()


if __name__ == '__main__':
    read = ReadConfig("../conf/config.ini").start()
    print(read)
    writer = WriterConfig("test1.ini")
    writer.start(read)

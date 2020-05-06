# -*- coding: utf-8 -*-
import os
import chardet
# import configparser
# from configparser import ConfigParser
from lib.configparser3 import ConfigParser

"""
读取本地配置文件
"""


# class NewConfigParser(ConfigParser):
#     def optionxform(self, optionstr):
#         return optionstr

# class WriterConfig(object):
#     def __init__(self, config_path):
#         self.config = ConfigParser()
#         self.config_path = config_path
#         # self.config_path = settings.options.get("config", "config.ini")
#
#         self.open(self.config_path)
#
#     def open(self, filename: str) -> None:
#         """
#         读取文件
#         :param filename: 文件
#         :return:
#         """
#         self.config.read(filename, encoding="utf-8")
#
#     def writer(self, section_values):
#         """
#         写入配置文件
#         :param section_values: dict
#         :return:
#         """
#         for section in section_values:
#             self.config.add_section(section)
#             option_values = section_values[section]
#             for option in option_values:
#                 self.config.set(section, option, option_values[option])
#         self.save()
#
#     def save(self):
#         """
#         保存
#         :return:
#         """
#         with open(self.config_path, "w") as f:
#             self.config.write(f)

class ReadConfig(object):
    def __init__(self, config_path):
        self.config = ConfigParser()
        self.config_path = config_path
        # self.config_path = settings.options.get("config", "config.ini")

        self.open(self.config_path)

    @staticmethod
    def file_encoding(filename: str) -> str:
        """
        读取编码
        :param filename:
        :return:
        """
        with open(filename, 'rb') as f:
            encoding = chardet.detect(f.read(2000))['encoding']  # 当前文件编码
            return encoding

    def open(self, filename: str) -> None:
        """
        读取文件
        :param filename: 文件
        :return:
        """
        filename = os.path.abspath(filename)
        encoding = self.file_encoding(filename)
        # self.config.read(self.config_path, encoding="utf-8")
        self.config.read(filename, encoding=encoding)

        # 保存注释
        with open(self.config_path, "r", encoding=encoding) as f:
            self.config.read_file(f)

    def read_to_dict(self) -> dict:
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

    def update_config(self, sections: dict) -> None:
        """
        写入配置文件
        :param sections: dict
        :return:
        """
        for section in sections:
            if not self.config.has_section(section):
                self.config.add_section(section)
            options = sections[section]
            for option in options:
                if self.config.has_option(section, option):
                    print(option, options[option])
                    self.config.set(section, option, options[option])

    def save_dict(self, section_values: dict) -> None:
        """
        保存
        :return:
        """
        # self.update_config(section_values)
        self.config.read_dict(section_values)  # 解析输入的数据,并更新数据
        with open(self.config_path, "w") as f:
            self.config.write(f)


if __name__ == '__main__':
    # 读取
    read = ReadConfig("../test/config3.ini")
    data = read.read_to_dict()
    # 修改数据
    data["address"]["ip"] = "192.168.30.1111"
    # 写入文件
    # writer = WriterConfig("../test/test111.ini")
    # writer.writer(read)
    # read.save_dict(data)

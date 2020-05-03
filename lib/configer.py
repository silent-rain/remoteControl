# -*- coding: utf-8 -*-
import configparser


class NewConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr


class ReadConfig(object):
    _instance = None

    def __init__(self, config_path, config_text=''):
        self.config = NewConfigParser()
        self.config_path = config_path
        self.config_text = config_text
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

    def open(self):
        """
        :return:
        """
        sections = self.config.sections()
        section_item = {}
        for section in sections:
            options = self.config.options(section)
            # print(options)
            option_item = {}
            for option in options:
                value = self.config.get(section, option)
                option_item[option] = value
            section_item[section] = option_item
        # print(section_item)
        return section_item

    def start(self):
        self.file_encoding()
        return self.open()


if __name__ == '__main__':
    from libs import settings
    config = ReadConfig(settings.CONFIG_FILE).start()
    print(config)

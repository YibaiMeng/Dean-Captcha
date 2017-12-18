# External libraries
import sqlite3

import constants

is_data_base_connected = False

conn = sqlite3.connect


class Captcha:
    conn = sqlite.connect(constans.database_dir)
    def __init__(self, captcha_file_id, char_num):
        self.id = captcha_file_id
        self.char_num = CHAR_NUM
        self.conn = sqlite3.connect(database = constants.database_dir)
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

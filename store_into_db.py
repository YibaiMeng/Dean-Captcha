# External libraries
import sqlite3
import base64

#Project Libraries
import img2vec
import show_char
import utils

database_dir = "new_training.db"
captchas_dir = "example_captchas/"

#ALTER TABLE table_name ADD column_name datatype: This datatype is to add a column.
conn = sqlite3.connect(database=database_dir)
cursor = conn.cursor()
array_list = list()
for i in range(0, 10000, 1):
    for j in range(4):
        array_list.append(img2vec.captcha2char_vectors(example_captchas+str(i).zfill(5)+".gif", False, True)[j])
    info = (i,array_list[0],array_list[1], array_list[2],array_list[3], 0)
    cursor.execute('INSERT INTO captchas (id, char1, char2, char3, char4, is_verified) VALUES (?,?,?,?,?,?)',info)
conn.commit()
conn.close()

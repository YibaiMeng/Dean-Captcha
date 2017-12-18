#External
import sqlite3
import json
import utils

to_whom = "naiqing"

conn = sqlite3.connect(database="/home/mengyibai/training_data.db")
cursor = conn.cursor()

cursor.execute('SELECT * FROM captchas WHERE is_verified=2 AND true_value!="aaaa" AND true_value!="AAAA"')
# all data that is verified, and which people are sure of its validity
infos = cursor.fetchall()
i = 0

shits = list()
walala = dict()

for pics in infos:
    if to_whom =="huiyu":
        for i in range(4):
            walala[utils.b642array(str(pics[i+1]), one_long_string=True)] = pics[5][i].capitalize()
    elif to_whom == "naiqing":
        shit = dict()
        shit["id"] = pics[0]
        for i in range(4):
            shit["char_"+str(i+1)] = utils.b642array(str(pics[i+1]), one_long_string=True)
        shit["true_value"] = pics[5].upper()
        shits.append(shit)
print(json.JSONEncoder().encode(shits))

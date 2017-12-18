#! /usr/bin/python3
import sqlite3
from random import randint

# absolute dir of database! Note that an relative dir could cause problem! I have no idea why!
database_dir="/home/mengyibai/GitHub/DeanCaptcha/my_web/cgi-bin/training_data.db"

def check_text_value(text_value):
    # TODO: use try and catch.
    # QUESTION: where to check for similarities?
    acceptable_chars = ['A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e' ,'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4','5','6','7','8','9']

    if text_value.__len__() != 4:
        return False
    for i in range(4):
        if text_value[i] not in acceptable_chars:
            return False
    return True

def get_next_captchas():
    '''
    return the next ids of the pics to show
    '''
    conn = sqlite3.connect(database=database_dir)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM captchas WHERE is_verified=0 OR is_verified=1') # get two random captchas that has not been filled or is only filled once.
    next_captcha_ids = cursor.fetchall()
    id1 = randint(0,len(next_captcha_ids)-1)
    id2 = randint(0,len(next_captcha_ids)-1)
    conn.close()
    return next_captcha_ids[id1][0], next_captcha_ids[id2][0]

def store_value_into_db(ID, text_value):
    conn = sqlite3.connect(database=database_dir)
    cursor = conn.cursor()

    ID_as_tuple = (ID,)
    cursor.execute('SELECT is_verified, true_value FROM captchas WHERE id=?',ID_as_tuple)
    verification_stat = cursor.fetchall()
    current_true_value = verification_stat[0][1]
    verification_stat = verification_stat[0][0]
    # the true value stored in it

    if check_text_value(text_value) == False:
        return False
    if current_true_value:
        if current_true_value != text_value:
            text_value = "aaaa"
    value_update = (text_value, verification_stat+1, ID)
    cursor.execute('UPDATE captchas SET true_value=?, is_verified=? WHERE id=?', value_update)
    conn.commit()# very important!
    conn.close()
if __name__ == "__main__":
    #print(get_next_captchas())
    #store_value_into_db(ID=1,text_value="4823")

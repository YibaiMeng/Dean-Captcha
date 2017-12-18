def show_char(array, use_special_char=True):
    for i in range(12):
        for k in range(4):
            for j in range(10):
                if array[k][i*10 + j] == 0:
                        print("  ", end='')
                elif array[k][i*10 + j] == 1:
                    if use_special_char==True:
                        print("\u2588\u2588", end='')
                        # Unicode character FULL BLOCK
                    else:
                        print("##", end='')
            print("   ", end='')
        print("")
    print(" ")

def show_captcha(id):
    conn = sqlite3.connect(database="training_data.db")
    cursor = conn.cursor()
    id = int(id)
    if id < 0 or id > 10000:
        return
    Id = id,

    cursor.execute('SELECT vec1,vec2,vec3,vec4 FROM captchas WHERE id=?', Id)
    infos = cursor.fetchone()
    conn.close()
    captcha_img = list()
    for i in range(0,4,1):
        captcha_img.append(b642array(infos[i]))
    show_char.show_char(captcha_img)

import json
import numpy

training_data_dir = "data_12-18.json"

def str_to_numpy(string):
    ka = list()
    for char in string:
        ka.append(int(char))
    ga =numpy.array(ka)
    return ga
def char_to_int(ch):
    shit = ['0', '1', '2', '3', '4','5','6','7','8','9','A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if ch.capitalize() in shit:
        return shit.index(ch.capitalize())

def get_trainging_data():
    jsonDat = open(training_data_dir)

    traning_data = jsonDat.read()
    jsonDat.close()

    data = json.JSONDecoder().decode(traning_data)
    training_data = list()
    for datum in data:
        tp1 = (str_to_numpy(datum["char_1"]), char_to_int(datum["true_value"][0]))
        tp2 = (str_to_numpy(datum["char_2"]), char_to_int(datum["true_value"][1]))
        tp3 = (str_to_numpy(datum["char_3"]), char_to_int(datum["true_value"][2]))
        tp4 = (str_to_numpy(datum["char_4"]), char_to_int(datum["true_value"][3]))
        training_data.append(tp1)
        training_data.append(tp2)
        training_data.append(tp3)
        training_data.append(tp4)
    t_data = training_data[:2000]
    v_data = training_data[2001:2100]
    test_data = training_data[2101:]
    return t_data, v_data, test_data

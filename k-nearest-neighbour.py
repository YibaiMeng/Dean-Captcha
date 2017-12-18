import json
import img2vec

def diff_value(char_vector,key):
    '''
    char_vector is an array of 120 characters which is either '0' or '1'
    key is a key of one json object in injson
    calculate the numbers of differences between char_vector and key
    '''
    ans = 0
    for i in range(120):
        if str(char_vector[i]) != str(key[i]):
            # 注意JSON天生读进来的是char
            ans = ans + 1
    return ans


def char2index(ch):
    shit = ['0', '1', '2', '3', '4','5','6','7','8','9','A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if ch.capitalize() in shit:
        return shit.index(ch.capitalize())

def index2char(ind):
    '''
    establish a map between a char and an index
    '0'-'9' to 0-9
    'A'-'Z' to 10-35
    '''
    shit = ['0', '1', '2', '3', '4','5','6','7','8','9','A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return shit[ind]


def knn(file_path):
    with open('test.txt','r') as fr:
        injson = json.load(fr)
    '''
    input test.txt as known data
    injson is json format
    '''
    for i in injson.keys():
        print(i,injson[i])

    char_vectors = img2vec.captcha2char_vectors(file_path, False)
    '''
    assume char_vectors has four elements
    every element is an array with 120 characters which is either '0' or '1'
    '''

    k = 20
    '''
    k represents we will get the top k records that have the least differences
    '''
    answer = list()
    for i in range(4):
        pair_diff_chara = list()
        for j in injson.keys():
            diff = diff_value(char_vectors[i],j)
            pair_diff_chara.append((int(diff),char2index(injson[j])))
        pair_diff_chara.sort()
        print(pair_diff_chara)
        rec = list()
        for p in range(36):
            rec.append(0)
        for p in range(0,k,1):
            rec[pair_diff_chara[p][1]] = rec[pair_diff_chara[p][1]] + 1
        Max, maxi = 0, 0
        for p in range(36):
            if rec[p] > Max :
                Max = rec[p]
                maxi = p
        answer.append(index2char(maxi))
    print(answer)
    '''
    answer reserves the answer of knn algorithm
    answer has four elements
    '''
knn(file_path="example_captchas/00020.gif")

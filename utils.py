# External libraries
import base64

def array2b64(array):
    '''
    Encode a character of a captcha image in base64 format
    Takes a array for the character as input. A single array, not a nested array for the whole captcha! Returns a string.
    '''
    string = ""
    for char in array:
        string += str(char)
    int_rep = int(string,2)
    bytes_rep = int_rep.to_bytes(15, byteorder='big', signed=False)
    b64 = str(base64.b64encode(bytes_rep))
    return b64[2:-1]
def b642array(b64, one_long_string=False):
    '''Decodes the base64 encoding of a single character in a captcha image
    Takes in a string, returns a array. All the elements are in integer format.
    '''
    byte_rep = base64.b64decode(b64)
    int_rep = int.from_bytes(byte_rep, byteorder='big', signed=False)
    string_rep = bin(int_rep)
    real_string_rep = string_rep[2:].zfill(120)
    if one_long_string==True:
        return real_string_rep
    array = list()
    for char in real_string_rep:
        if char == "1":
            array.append(1)
        elif char == "0":
            array.append(0)
    return array

# External Libraries
from PIL import Image
# note: PIL is no longer in use. The name of the library is actually Pillow
import numpy


def captcha2char_imgs(file_path):
    '''Turns a captcha into a list of its consisting characters, i.e. partitioning.
    Read gif file from file path, extract the four individual characters from the image and return four individual pictures, as a list of pillow image objects. Note the size (width * height) of the image is NOT CHANGED, meaning lots of background pixels remains. Also, the RGB color information is stripped.

    The algorithm is naive: just get the four most used colors (excluding the background color, which is of course the most used, by a wide margin), and put all the pixels of each color in a picture, respectively. Of course, the assumption that a character is made of a single color is not vaild, but practically it matters little(I hope so).
    '''

    im = Image.open(file_path)
    colors = im.getcolors()
    list.sort(colors,reverse=True)
    char_colors = list()
    for i in range(4):
        char_colors.append(colors[i+1][1])
    char_imgs = list()
    for j in range(4):
        char_imgs.append(im.point(lambda i: i == int(char_colors[j])))
    # a simple algorithm: pick the four most common colors, apart from the background. Vola! pick all pixels of each color, thus getting the four images.
    return char_imgs
def remove_background_resize(char_img):
    '''removes redunant background and resize image of individual characters

    Removes background and turns the size of the img into 10*12, width times height. Returns a pillow image object. 120 bit per character.
    '''
    colors = char_img.getcolors()
    list.sort(colors)
    background_color = colors[1][1]
    char_color= colors[0][1]
    width, height = char_img.size
    pixel_values = list(char_img.getdata())

    left, right, up, down = 0, 0, 0, 0

    for i in range(height):
        flag = 1
        for j in range(width):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            up = i
            break
    for i in range(height - 1, -1, -1):
        flag = 1
        for j in range(width):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            down = i
            break
    for j in range(width):
        flag = 1
        for i in range(height):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            left = j
            break
    for j in range(width - 1, -1, -1):
        flag = 1
        for i in range(height):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            right = j
            break

    # let the resulting size be height = 12 and width = 10
    if (up > 0) and ((up + 10) < height):
        up = up -1
        down = up + 11
    elif up == 0:
        down = 11
    else:
         up = down - 11

    if (left > 0) and ((left)+8 < width):
        left = left - 1
        right = left + 9
    elif (left == 0):
        right = left + 9
    else:
        left = right -9

    box = (left, up, right + 1, down + 1)
    transformed_img = char_img.crop(box)

    return left, transformed_img

def char_img2numpy_str(img, return_numpy=True, return_binary=False):
    '''Turns an individual char img to numpy str
    '''
    if return_numpy == True:
        n_array = numpy.array(img.getdata())
        return n_array
    if return_binary == True:
        return bytes(img.getdata())
    else:
        array = list(img.getdata())
        return array


def captcha2char_vectors(file_path, return_numpy=True, return_binary=False):
    '''Calls all the above functions and do the thing!
    '''
    char_imgs = captcha2char_imgs(file_path)
    resized_char_imgs = list()
    char_vectors = list()
    for i in range(4):
        resized_char_imgs.append(remove_background_resize(char_imgs[i]))
    list.sort(resized_char_imgs) # note the ordering of the characters.

    for i in range(4):
        char_vectors.append(char_img2numpy_str(resized_char_imgs[i][1], return_numpy, return_binary))
    return char_vectors

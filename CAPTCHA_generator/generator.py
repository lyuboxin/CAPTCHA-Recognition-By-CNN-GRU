from captcha.image import ImageCaptcha
from random import sample

char_list = "abcdefghijklmnopqrstuvwxyz1234567890"

image = ImageCaptcha()

def captcha_generator(length, path, total):
    num = 0 
    while num < total:
        ran_list = sample(char_list, length)
        ran_list = ''.join(ran_list)
        _ = image.generate(ran_list)
        image.write(ran_list, path+ran_list+".png")
        num += 1
 
captcha_generator(4, "../CAPTCHA_pic/", 5000)
print "generate length 4"
captcha_generator(5, "../CAPTCHA_pic/", 5000)
print "generate length 5"
captcha_generator(6, "../CAPTCHA_pic/", 5000)
print "generate length 6"
captcha_generator(7, "../CAPTCHA_pic/", 5000)
print "generate length 7"
captcha_generator(8, "../CAPTCHA_pic/", 5000)
print "generate length 8"


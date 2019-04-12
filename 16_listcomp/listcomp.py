# Michelle Tang
# SoftDev2 pd6
# K#16 -- Do You Even List?
# 2019-04-11

def validate (password):
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = uppers.lower()
    numbers = "0123456789"

    upper = [x for x in password if x in uppers]
    lower = [x for x in password if x in lowers]
    number = [x for x in password if x in numbers]

    if len(upper) and len(lower) and len(number):
        return True
    return False

#expecting false
print validate("jasladkfjdsalk")
print validate("ASDKFJSDKLF")
print validate("ASDKFJ1342SDKLF")

#expecting true
print validate ("AS3341AaadfsdFD")
print validate("A1a")

def sum(list):
    total = 0
    for element in list:
        total += element
    return total

def scale(password):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    specials =".?!&#,;:-_*"
    if validate(password):
        character = [.4   for x in password if x in characters]
        specials = [.5   for x in password if x in specials]
        total = sum(character) + sum(specials)
        if total > 10 :
            return 10
        # print total
        return int(round(total))
    return "Your password does not meet the minimum threshold."


print scale ("ZJEjdib3!@#$@iou#$#@dfsJIdFD")  # great password
print scale("A1a") # my password tbh
print scale("1abc13A") #mediocre password

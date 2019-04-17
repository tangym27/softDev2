# to the lighthouse: Clara Mohri & Michelle Tang
# SoftDev pd6
# K #20: wee
# 2019-04-17

from functools import reduce

def open_file(file):
    file = open(file, "r")
    text = file.read().split()
    file.close()
    return text

def strip(text):
    return [x.strip(".?!;,-").lower() for x in text]

def single_freq(word, text):
    word = word.lower()
    list = [1 for x in text if x == word]
    if not len(list):
        return 0
    return reduce((lambda x,y: x+y), list)

def mult_freq(words, text):
    words = strip(words.split())
    list = [1 for x in text if x == word]
    if not len(list):
        return 0
    return reduce((lambda x,y: x+y), list)

# ["hi","there"]
text = open_file("hi.txt")
text = strip(text)
print(single_freq("there", text))
print(single_freq("i", text))
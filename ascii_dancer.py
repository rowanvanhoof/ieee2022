# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

bodyMovement = {
    "left hand to head": [3,')'],
    "left hand to hip" : [3,'>'],
    "left hand to start": [3,'\\'],
    "right hand to head": [1,'('],
    "right hand to hip" : [1,'<'],
    "right hand to start": [1,'/'],
    "right leg out":[4,"/"],
    "right leg in":[4,"<"],
    "left leg in":[5,">"],
    "left leg out":[5,"\\"]
}

person = ["o", "/", "|", "\\", "/", "\\" ]

get_word()
get_word()
x = input.split(" ")
while x != None:
    print(x)
    x = input.split(" ")

def move(person, movement):

    change_index, change_val = bodyMovement[movement]
    person[change_index] = change_val
    return person
    
def print_person(person):
    print(f" {person[0]}")
    temp = "".join(person[1:4])
    print(f"{temp}")
    temp = "".join([person[4], " ", person[5]])
    print(f"{temp}")



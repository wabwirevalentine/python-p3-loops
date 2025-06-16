#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(f"{i}")
        if i == 1:            
            print("Happy New Year!")
        i -= 1
    pass

def square_integers(int_list):
    # code goes here!
    return [num ** 2 for num in int_list]
    pass

def fizzbuzz():
    # code goes here!
    n = 100
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (i)
    pass

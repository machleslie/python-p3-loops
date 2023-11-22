#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    i = 10
    while i > 0:
        print(i)
        if i == 1:
            print('Happy New Year!')
        i -= 1
           

def square_integers(int_list):
    # code goes here!
    squared_array = list()
    for i in int_list:
        squared_array.append(i**2)
    
    return squared_array

def fizzbuzz():
    # code goes here!
    n = 1
    while n <= 100:
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%3==0:
            print('Fizz')
        elif n%5==0:
            print('Buzz')
        else:
            print(n)
            
        n += 1
        
    
fizzbuzz()

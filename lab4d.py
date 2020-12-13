#!/usr/bin/env python3
# Strng1

# Author: Sama Koleini
# Author ID: skoleini1



str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(theString):
    # Place code here - refer to function specifics in section below

	first = theString[0:5]
	return first



def last_seven(theString):
    # Place code here - refer to function specifics in section below

	last = theString[-7:]
	return last




def middle_number(theInteger):
    # Place code here - refer to function specifics in section below
	
	theString = str(theInteger)
	mid = theString[1:3]
	return mid



def first_three_last_three(str1,str2):
    # Place code here - refer to function specifics in section below

	res_a = str1[0:3]
	res_b = str2[-3:]
	return res_a+res_b
	



if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))


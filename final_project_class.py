# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:32:51 2017

@author: Chad S. Caron

This script contains a class Blardy which combines previous work. 
The command line inputs are the iris dataset filename in the cwd and the column number to play with.
ie: python iris.data 2

"""
import sys
import csv
import io
import numpy as np

class Blardy():

    def __init__(self):
        print("Welcome to Blardy!")
        
#function to read in file
    def read_in_file():
        try:
            f = io.open(sys.argv[1],"r", encoding="utf-8")
        except IOError:
            print("can't read the file.")
            raise IOError
        else:
            my_file = csv.reader(f)
#        my_file = 0 #test value to test exception handling
        #my_file = pd.read_csv(f)
        return my_file

#find min & max value and element of each list, multiply the column by 24 and report the max value of the new list
    def min_max(col_number):
        col_list = []
        mult_list = []
        my_file = Blardy.read_in_file()
        try:
            for row in my_file:
                col_list.append(float(row[col_number]))
        except ValueError:
            print("integer of column please.")
            raise ValueError 
        else: 
            max_no = np.max(col_list)
            min_no = np.min(col_list)
        for i in col_list:
            mult_list.append(24 * i)
        max_mult = np.max(mult_list)
        return min_no, max_no, max_mult

#check the passed column input value, if not an integer, let them try again
    def input_chk():
        allowed_inp = [0,1,2]
        first_inp = sys.argv[2]
        try:
            while int(first_inp) not in allowed_inp:
                print("please input integer of column desired")
                first_inp = input("Try 0, 1, or 2:")
        except ValueError:
            print("{} isn't allowed, let's just say you typed 0.".format(first_inp))
            first_inp = 0
        column_no = first_inp
        return column_no

column_no = Blardy.input_chk()    
Col_min = Blardy.min_max(int(column_no))[0]
Col_max = Blardy.min_max(int(column_no))[1] 
Col_mult_max = Blardy.min_max(int(column_no))[2] 

print("The max of column {} is {}. 24 times this value is {}\n".format(column_no,Col_max,Col_mult_max))
#print(Col_mult_max)

#counts the number of instances of each value in column 4 of the input file
def species_dict():
    my_dict = {}
    my_file = Blardy.read_in_file()
    for row in my_file:
        key = row[4]
        if key not in my_dict:
            my_dict[key] = 1
        else:
            my_dict[key] += 1
    return my_dict

dict_out = species_dict()
print(dict_out)

f = open("final.txt", "w")
f.write("The min of column {} is {}.\n".format(column_no,Col_min))
f.close()


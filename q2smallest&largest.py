'''
Created on Aug 2, 2019

@author: Rupesh
Write a python code to find the largest 
and smallest number in the given array of integer elements 
'''
number=[5,4,2,6,2,1,8,5,7]
smallest=[]
largest=[]

number.sort()
print(f'smallest number is: {number[0]}')
print(f'smallest number is: {number[-1]}')
'''
Created on Aug 2, 2019

@author: Rupesh
Write a python code to read file content and display the content in the console
'''
f = open('example.txt', 'r')
file_contents = f.read()


print (file_contents)


f.close()
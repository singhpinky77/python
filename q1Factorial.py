'''
Created on Aug 2, 2019

@author: Rupesh
'''

def factorial (n):
    return 1 if n==1 or 0 else n * factorial(n-1)
          

number=5
print ("Factorial of",number,"is", 
      factorial(number))
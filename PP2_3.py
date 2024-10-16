'''

    Lesson: Else If
    Author: Jonisa Shanmuganantham
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024

'''

def q1(): 
  word = input("In: ")
  if word [-2:] == "ey":
    print("-eys")
  elif word [-1] == "y":
    print("-ies")
  elif word [-3:] == "ife":
    print("-ives")
  else:
    print("-s")

def q2(): 
  num = int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  if num < 0: 
    print(f"{num} is negative")

def q3():
  num1 = float(input("Input a number: "))
  num2 = float(input("Input a number: "))
  num3 = float(input("Input a number: "))

#Do not alter the following code
#Comment out the following code when running your tests

'''
q1()
q2()
q3()

'''
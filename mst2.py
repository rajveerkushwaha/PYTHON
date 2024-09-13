# import math 
# import random
# a=196
# print(int(math.sqrt(a)))
# print(dir(math))
# 
# from datetime import datetime
# print(datetime.now())
# 
# for i in range (1,100):
    # print("it will print random number between the 1 to 100 and the number will be integer :-   ",random.randint(1,100))
    # print(i)
   
   
# import matplotlib.pyplot as plt

# x_values = [0, 1, 2, 3, 4, 5]
# y_values = [0, 1, 2, 3, 4, 5]

# plt.plot(x_values, y_values)

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Line Graph')

# plt.show()




# MOST COMMON PROGRAM OF REGULAR EXPRESSIONS
"""import re

# Matching a specific word "hello"
pattern1 = r'hello'
text1 = "hello world"
result1 = re.match(pattern1, text1)  # Output: Match found at the beginning of the string

# Matching any single character
pattern2 = r'.'
text2 = "abc"
result2 = re.fullmatch(pattern2, text2)  # Output: Match found at position 0

# Matching digits
pattern3 = r'\d'
text3 = "123"
result3 = re.findall(pattern3, text3)  # Output: List of digits ['1', '2', '3']

# Matching whitespace
pattern4 = r'\s'
text4 = "hello world"
result4 = re.split(pattern4, text4)  # Output: List of strings ['hello', 'world']

# Matching word characters (letters, digits, and underscores)
pattern5 = r'\w'
text5 = "hello123_world"
result5 = re.findall(pattern5, text5)  # Output: List of word characters ['h', 'e', 'l', 'l', 'o', '1', '2', '3', '_', 'w', 'o', 'r', 'l', 'd']

# Matching a specific number of characters (5 word characters)
pattern6 = r'\w{5}'
text6 = "hello123_world"
result6 = re.findall(pattern6, text6)  # Output: List of strings ['hello', '123_w']

# Matching beginning of a string "hello"
pattern7 = r'^hello'
text7 = "hello world"
result7 = re.match(pattern7, text7)  # Output: Match found at the beginning of the string

# Matching end of a string "world"
pattern8 = r'world$'
text8 = "hello world"
result8 = re.search(pattern8, text8)  # Output: Match found at position 6

# Matching optional characters "colour" or "color"
pattern9 = r'colou?r'
text9 = "color"
result9 = re.fullmatch(pattern9, text9)  # Output: Match found at position 0

# Matching any character in a set of vowels
pattern10 = r'[aeiou]'
text10 = "hello"
result10 = re.findall(pattern10, text10)  # Output: List of vowels ['e', 'o']
  
# Print results
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
print("Result 4:", result4)
print("Result 5:", result5)
print("Result 6:", result6)
print("Result 7:", result7)
print("Result 8:", result8)
print("Result 9:", result9)
print("Result 10:", result10)

"""


# filename = "example.txt"


# file = open(filename, 'r')
# content=file.read()
# file.close()
# print(content)
# import tkinter as tk 
# root=tk.Tk()
# label = tk.Label(root, text="Hello, World!")
# label.pack()
# root.mainloop()


filename="example.txt"
file=open(filename,'r') 
content=file.read()
file.close()
print(content)
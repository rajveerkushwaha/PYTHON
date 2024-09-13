# 
# text="welcome to dell inspiron 14 5430 i7  processor"
# try:
    # with open('example.txt','w')as file:
        # file.write(text)
        # print('file written sucessfully')
# 
# except:
    # print('try something else yarr ab kitna glti karoge')
    # 
    # 
#  program to read the file 
 # file=open('example.txt','r')
 # content=file.read()
 # file.close()
 # print(content)



# import tkinter as tk
# root = tk.Tk()
# label = tk.Label(root, text="Hello, World!")
# label.pack()
# root.mainloop()


# import pandas as pd

# import numpy as np
# array=np.array([1,2,3,4,5,6,7,8])
# reshaped=array.reshape(2,2,2)
# print (reshaped)

# list=[1,2,3,4,5,6,7,8,9]
# hell=pd.DataFrame(list)
# print(hell)
import numpy as np
a=np.arange(1,28).reshape(3,3,3)
print(a)
b=np.identity(4)
print(b)


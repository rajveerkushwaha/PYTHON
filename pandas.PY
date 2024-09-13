import pandas as pd

# List 
marks_list = [12, 14, 56, 78, 90, 98, 76]
s1_list = pd.Series(marks_list)
print("Series from list:")
print(s1_list)

# Tuple 
marks_tuple = (12, 14, 56, 78, 90, 98, 76)
s1_tuple = pd.Series(marks_tuple)
print("\nSeries from tuple:")
print(s1_tuple)

# Dict 
marks_dict = {'maths': 12, 'physics': 14, 'chem': 56, 'hindi': 78, 'english': 90}
s1_dict = pd.Series(marks_dict)
print("\nSeries  dict:")
print(s1_dict)

# Sort 
s2_sorted = s1_tuple.sort_values()
print("\nSorted Series:")
print(s2_sorted)

# Head
print("\nFirst 5 Series:")
print(s1_tuple.head())

# NaN
marks_with_nan = [12, 14, None, 78, 90, 98, 76]
s1_nan = pd.Series(marks_with_nan)
print("\nSeries with NaN:")
print(s1_nan)
#######################################################################################################################################
# DATAFRAME

import pandas as pd

marks = [100, 19, 90, 67, 68, 45, 34]
si = pd.Series(marks)
print(si)

marks = (40, 56, 43, 56, 3, 67, 34)
si = pd.Series(marks)
print(si)

marks = (40, 56, 43, 56, 3, 67, 34)
subjects = ["Maths", "English", "Hindi", "EVS", "OOPS", "Sats", "IF"]
si = pd.Series(marks, index=subjects)
print(si)

marks = {"English": 100, "Hindi": 20, "Maths": 30, "EVS": 40}
si = pd.Series(marks)
print(si)

print(si.head())
print(si.sort_values())
print(si.sort_values(ascending=False))

df = pd.DataFrame(si)
print(df)

df = df.rename(columns={0: "Marks"})
print(df)

df.reset_index(inplace=True)
print(df)

df = df.rename(columns={"index": "Subjects"})
print(df)

print(df.isnull().sum())

df['School name'] = "Rayat Bharat"
print(df)

df['Teacher name'] = ['Mr.X', 'Mr.Y', 'Mr.I', 'Mr.C']
print(df)

print(df.iloc[2:5]['Teacher name'])
print(df.iloc[2:5]['Subjects'])

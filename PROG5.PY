import pandas as pd

data = {'Name': ['John', 'Emily', 'Michael'],
        'Age': [30, 25, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

excel_file = 'data.xlsx'
df.to_excel(excel_file, index=False)
print("Data written to Excel file:", excel_file)

read_df = pd.read_excel(excel_file)
print("\nData read from Excel file:")
print(read_df)

import pandas as pd

data = {
    'Product': ['Kannan', 'Choy', 'Rabeka', 'We love powerbi'],
    'Sales': [100, 150, 200, 130],
    'Date': pd.date_range('2024-01-01', periods=4, freq='ME')
}

df = pd.DataFrame(data)
print(df)
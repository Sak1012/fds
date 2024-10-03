import pandas as pd

data = {
    'Element': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron'],
    'Atomic Number': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
print(df)

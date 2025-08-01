"""
import pandas as pd  # pandas kutubxonasini chaqirish

# Oddiy DataFrame yaratish
data = {
    'Ism': ['Ali', 'Vali', 'Gulbahor'],
    'Yosh': [25, 30, 22],
    'Kasb': ['Dasturchi', 'O‘qituvchi', 'Talaba']
}

df = pd.DataFrame(data)

print(df)

import pandas as pd  
data =  ['Ali', 'Vali', 'Gulbahor']
df=pd.Series(data)
print(df) 


import pandas as pd

data={
    'Ismlar': ['Aziza', 'Baxtiyor', 'Sanjar'],
    'Yoshlari': [21, 28, 35],
    'Kasblari': ['Talaba', 'Muhandis', 'Boshqaruvchi']
}

df=pd.DataFrame(data)

print(df[['Ismlar','Kasblari']]) #2 ta ustunni oladi


import pandas as pd

data={
    'Ismlar': ['Aziza', 'Baxtiyor', 'Sanjar'],
    'Yoshlari': [21, 28, 35],
    'Kasblari': ['Talaba', 'Muhandis', 'Boshqaruvchi']
}

df=pd.DataFrame(data)
print(df.iloc[0]) #faqat 1-rowni oladi


import pandas as pd

data={
    'Ismlar': ['Aziza', 'Baxtiyor', 'Sanjar'],
    'Yoshlari': [21, 28, 35],
    'Kasblari': ['Talaba', 'Muhandis', 'Boshqaruvchi']
}

df=pd.DataFrame(data)
print([df['Yoshlari']>25])


import pandas as pd

data={
    'Ismlar': ['Aziza', 'Baxtiyor', 'Sanjar'],
    'Yoshlari': [21, 28, 35],
    'Kasblari': ['Talaba', 'Muhandis', 'Boshqaruvchi']
}

df=pd.DataFrame(data)
df['Maosh']=[0,8000,12000] # yangi ustun qo'shish
print(df)


import pandas as pd

data={
    'Ismlar': ['Aziza', 'Baxtiyor', 'Sanjar'],
    'Yoshlari': [21, 28, 35],
    'Kasblari': ['Talaba', 'Muhandis', 'Boshqaruvchi']
}

df=pd.DataFrame(data)
df['Yosh*100']=df['Yoshlari']*100  # qo'shish
print(df)


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)


import pandas as pd

df=pd.read_csv('data.csv')
print(df.to_string())    # boshidan oxirgacha


import pandas as pd

print(pd.options.display.max_rows)

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()


with open("data.csv") as f:
    for x in f:
        print(x)
"""
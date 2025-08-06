"""
words = ["tree", "sky", "river", "cloud", "stone"]
new_word=[]
for a in words:
    if "e" in a:
        new_word.append(a)
print(new_word)        


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kvadrat=[]
for a in numbers:
    if a%2==0:
        x=a**2
        kvadrat.append(x)
print(kvadrat)        

words = ["apple", "banana", "kiwi", "cherry", "fig", "grapes"]
words1=[]
for a in words:
    if len(a)>5:
       words1.append()
print(words1)

"""
a=sum(range(2,101,2))
print(a)
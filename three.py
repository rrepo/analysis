import nltk
import re
import collections
import seaborn as sns
import matplotlib.pyplot as plt


f = open('code.txt', 'r', encoding='UTF-8')

data = f.read()

f.close()

sentence = data
a = nltk.word_tokenize(sentence.lower())

# print(a)

x =[]

index = 0
for item in a:
    
    b = a[index]
    # print(b[0])

    if len(b) >= 3 :
        x.append(b[0] + b[1] + b[2])


    index += 1

# print(x)

c = collections.Counter(x)
print(c.most_common(100))

sns.set(context="talk")
fig = plt.subplots(figsize=(8, 8))

sns.countplot(y=x,order=[i[0] for i in c.most_common(30)])

plt.savefig("three.png")
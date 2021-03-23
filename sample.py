#最初の一文字の頻度解析
#予測変換でよく使うような頻度の高いキーを調べる

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

#print(a)

x = []


index = 0
for item in a:
    
    b = a[index]
    # print(b[0])

    x.append(b[0])
    index += 1

#print(x)

c = collections.Counter(x)
print(c.most_common(100))

sns.set(context="talk")
fig = plt.subplots(figsize=(8, 8))

sns.countplot(y=x,order=[i[0] for i in c.most_common(30)])

plt.savefig("first_one.png")

print(c)
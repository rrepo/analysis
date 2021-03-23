#文字の頻度解析

import collections
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re


f = open('code.txt', 'r', encoding='UTF-8')

data = f.read()

f.close()

c = collections.Counter(data.lower())
print(c.most_common(100))


d = list(data)

sns.set(context="talk")
fig = plt.subplots(figsize=(8, 8))

sns.countplot(y=d,order=[i[0] for i in c.most_common(30)])

plt.savefig("seaborntest.png")
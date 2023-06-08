import re

def avg_word_len(s):
    words = s.split(' ')
    words = [re.sub(r'[^\w\s]','',w) for w in words]
    return sum(len(w) for w in words)/float(len(words))


s = "I need to work very hard to learn more about algorithms in Python!"
print(avg_word_len(s))




from collections import defaultdict

words = "apple banana apple strawberry banana lemon"

d = defaultdict(int)
for word in words.split():
    d[word] += 1



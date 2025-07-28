names = ["Alice", "Bob", "Charlie"]
scores1 = [85, 90, 88]
scores2 = [80, 85, 91]

list_2 = map((lambda s: (s[0] + s[1]) / 2),(zip(scores1,scores2)))
list_3 = list(zip(names,list_2))
print(list_3)



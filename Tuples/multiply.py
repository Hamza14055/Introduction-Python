def tuple_product(tup):
 product = 1
 for num in tup:
    product *= num
 return product
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)
print("the product of tup1 are",tuple_product(tup1))
print("the product of tup2 are",tuple_product(tup2))
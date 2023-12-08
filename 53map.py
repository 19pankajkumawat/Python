# map
# def mad(x):
#  return x*2
# print(mad(8))
#
# m = [5,4,7,2,7,2,5,6,8,9,3,1,4]

# newlst = list(map(mad,m))
# print(newlst)
# newlst = list(map(lambda x:x*x*x , m)       this is the lambda sentext
# print(newlst)


# filter
# def fil(a):
#  return a>4
# newnl =list(filter(fil,m))
# print(newnl)

# Reduce
# it show the final result as an output
from functools import reduce
m = [5,4,7,2,20]
sum = reduce(lambda x,y : x+y ,m)
print(sum)


num1 = [2,7,11,15]
tar1 = 9
num2 = [3,2,4]
tar2 = 6
num3 = [3,3]
tar3 = 6

def twosum(x,y):
    index_z = {}
    for index, num in enumerate(x):
        if y-num in index_z:
            return index_z[y - num], index
        index_z[num] = index

print(twosum(num1,tar1))
print(twosum(num2,tar2))
print(twosum(num3,tar3))
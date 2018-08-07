array = [5,1,2,4,3]

v = []
for i in range(len(array)-1, -1, -1):
    v.append(array[i])
print("O inverso é: ", v)
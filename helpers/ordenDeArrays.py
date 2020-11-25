arrayElem = [5,8,2,1,10,25,32,45,3,8,12,7]

n = 0
i = 0
while n == 0:
    n = 1
    print(arrayElem)
    for x in range (len(arrayElem)-i):
        if x > 0:
            if arrayElem[x] < arrayElem[x-1]:
                a = arrayElem[x]
                b = arrayElem[x-1]
                arrayElem[x-1] = a
                arrayElem[x] = b
                n = 0

    i += 1
#num = 600851475143
num = 100

#prime factors
pf = [2]

for a in range (3,num+1):
    flag = 1
    for x in pf :
        if a % x == 0 :
            flag = 0
            break
    if flag :
        pf.append(a)



print("**********")
print(pf[-1])


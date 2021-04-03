#num = 600851475143
num = 30

pf = [2]

for a in range (3,num+1):
    for x in pf :
        if a % x == 0 :
            pf.append(x)

print(pf)
print("**********")
print(pf[-1])


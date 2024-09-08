for c in range(0,21):
    print(c)
million=[]
for m in range(0,1000001):
    million.append(m)

min(million)
max(million)
sum(million)

print(min(million),max(million),sum(million))

odd= list(range(1,21,2))
print(odd)

three=[]
for value in range(3,30):
    three.append(value*3)

print(three)

cube=[]
for cubes in range(1,11):
    cube.append(cubes**3)

print(cube)

cuber=[c**3 for c in range(1,11)]
print(cuber)

square=[s**2 for s in range(1,100000000000000000)]
print(square)
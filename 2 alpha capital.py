d = " "
n = int(input("No of elements you want in 1 string : "))

for i in range(n) :
    x = input("Enter : ")
    d = x
    z = list(d)
    q = z.pop(1)
    a = q.upper()
    p = z.insert(1,a)
    e = "".join(z)
    print(e)

m = int(input("No of elements you want in 2 string : "))
l = " "
for i in range(m) :
    y = input("Enter : ")
    l = y
    c = list(l)
    j = c.pop(1)
    b = j.upper()
    u = c.insert(1,b)
    f = "".join(c)
    print(f)
    
o = []
o.append(e)
o.append(f)
print(o)
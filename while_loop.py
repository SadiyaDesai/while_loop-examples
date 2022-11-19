# odd =[]
# even =[]
# num = 10
# while num > 0:
#     if num %2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
#     num-=1
# print('Addition of Odd list:',sum(odd))
#
# print('Addition of Even list:',sum(even))

"""
l1=[-2,8,-7,9,0]
c=0
s=len(l1)

while (c <= s):
    for i in l1:
        if i < 0:
            print("no is negative", i)
        elif i > 0:
            print("no is positive", i)
        elif i == 0:
            print("no entered is zero", i)
        c=c+1
...

n=["sadiya","10123","khadija","789"]
c=0
s=len(n)

while(c < s):
    for i in n[c]:
        if i.isnumeric():
            print("value is numeric:",i)
        elif i.isalpha():
            print("char value:",i)

    c=c+1
    .................................................

.....................................................
index= 0
k = ['se','fm12','#$']
while index < len(k):
    print(index)
    print(k[index])
    for i in k[index]:
        if i.isalpha():
            print(i, 'is char')
        elif i.isdigit():
            print(i, 'is a number')
        else:
            print(i, 'is special character')
    index+=1
..............................
n=["sadiya","10123","khadija","789"]
c=0
s=len(n)

while(c < s):
    for i in n[c]:
        if i.isnumeric():
            print("value is numeric:",i)
        elif i.isalpha():
            print("char value:",i)

    c=c+1
    index = 0
    k = ['se', 'fm12', '#$']
    while index < len(k):
        print(index)
        print(k[index])
        for i in k[index]:
            if i.isalpha():
                print(i, 'is char')
            elif i.isdigit():
                print(i, 'is a number')
            else:
                print(i, 'is special character')
        index += 1
        ..........................
        num=10
while(num>0):

    print(num)
    num = num - 1
    ...........................
    res=0
num=1
while num<11:
    print(num)
    num=num+1
    res=res+num
print("addition is",res)
..................................
e=[]
o=[]
num=1
while num<11:
    if num%2==0:
        print("even no",num)
        e.append(num)
    else:
        print("odd no",num)
        o.append(num)
    num=num+1
print("even list:",e)
print("odd list:",o)
print("addition of even no:",sum(e))
print("addition of odd no:",sum(o))
...............................
while c<len(s):
    if s[c].isalpha()==True:
            print("valus is char",s[c])
            ch.append(s[c])
            c=c+1
    elif s[c].isnumeric()==True:
            print("value is no",s[c])
            n.append(s[c])
            ch=ch+1
    else:
            print("it is special char")


    c=c+1
print(n)
print(c)
..............



s="sadiya12467"
c=0
cn=0
n=[]
ch=[]
..................
s="sadiya1234"
c=0
while c<len(s):
    if s[c].isalpha()==True:
        print("value is char",s[c])
    elif s[c].isdigit()==True:
        print("value is number",s[c])
    else:
        print("value is special char")
    c=c+1




l=["sadiya",123,"rabiya",548,"$","sadiya123"]
index=0
while index<len(l):
    for i in l[index]:

        #print(l[c])
        if i.isalpha():
            print("value is char", i)
        elif i.isdigit():
            print("value is number", i)
        elif i.isalnum():
            print("char+num",i)
        else:
            print("value is special char")
    index=index+ 1
............................
index= 0
k = ['se','fm12','#$']
while index < len(k):
    #print(c)
    #print(k[index])
    for i in k[index]:
        if i.isalpha():
            print(i, 'is char')
        elif i.isdigit():
            print(i, 'is a number')
        else:
            print(i, 'is special character')
    index+=1


"""


count=0
l=["sadiya",123,"rabiya",548,"$","sadiya123"]

while count<len(l):
    for i in l[count]:
        print(l[count])

        #print(l[c])
        if i.isalpha():
            print("value is char", i)
        elif i.isdigit():
            print("value is number", i)
        elif i.isalnum():
            print("char+num",i)
        else:
            print("value is special char")
    count=count+ 1
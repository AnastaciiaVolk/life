__author__ = 'Анастасия'


#n=input()
#k=input()

f=open("1.txt","r")
n = f.readline()
k=f.readline()
sw=f.readline()
s = sw.split(" ")
n=int(n)
k=int(k)
#s=int(s)
a=[n]
i=0
for i in range(len(s)):
    a.append(s[i])
    a[i]=int(a[i])
print(n,k)


   # print(line, end='')

#a=[n]
#a=[7,3,10,8,1,9]



a.sort()
for i in range(n):
      print(a[i])

a.reverse()
i=0
c=0
for i in range(k):
    print(a[i])
    c=c+a[i]
print(c)












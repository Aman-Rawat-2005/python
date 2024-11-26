f=open('file.txt','r')
data=f.read()
print(data,'\n')

f=open('file.txt','r')
data=f.read(10)
print(data,'\n')

f=open('file.txt','r')
data=f.readline()
data1=f.readline()
print(data)
print(data1)
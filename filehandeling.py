f=open('sample.txt','w')
f.write('hello world')
f.close()


f=open('sample.txt','w')
f.write('my name is pranjal singh')
l=['hellow','hai','ia','fine']
f.writelines(l)
f.close()
with open('sample.txt','r')as f:
    print(f.read())
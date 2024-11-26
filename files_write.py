f=open("new.txt",'w')
data=f.write("HELLO BRO PEHCHANA MUJHE APNE")
f.close()

f2=open("new.txt",'w')
data=f2.write("HELLO ji")
f2.close()

#FOR APPENDING IN THE FILE

f1=open("new.txt","a")
data=f1.write(" MERA NAAM HAI CHOOTA BHEEM")
f1.close()

#for new built in function

with open("example.txt", "w") as file:
    file.write("This text is flushed to disk.\n")
    file.flush() 

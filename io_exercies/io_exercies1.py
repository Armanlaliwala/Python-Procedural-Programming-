# f = open ('io_exercies\myfile2.txt','w')
# lines = ["line1\n","line2\n","line3\n","line4\n","line5\n",] 
# f.writelines(lines) 
# f.close
#this is linked with the myfile2

#here we mention \n after every iterable object but in a large dataset that is not possible for that we can use 

f = open ('io_exercies\myfile3.txt','w')
lines = ["line1","line2","line3","line4","line5",] 

for line in lines:
    f.write(line + '\n')
    
f.close #this is linked with the myfile3.txt

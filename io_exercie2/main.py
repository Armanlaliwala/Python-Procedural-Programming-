with open ('myfile.txt','r') as f :
    print(type(f))
    
    f.seek(1)#start index #therefore index 0&1 will not be included
    print(f.tell()) #tell function let you know what is the seek value 
    data = f.read(515)#end index 
    print(data)
    #we have taken 2 , eg1 : - this is the random text we are generating for the read file operation
    # eg2 :- 123456789

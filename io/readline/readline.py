
f = open ('io\myfile.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
#file reading and writing

file1 = open('test.txt',"r+")
print(file1.read(3))
print(file1.readline())
POS=file1.seek(0,0);
print(file1.readline())
file2 = open('test2.txt','a')
line2 = "This is second text from the program \n"
file2.write(line2)


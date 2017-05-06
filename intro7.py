tuple1 = ('python', 'ruby','c','java')
list1 = ['python','ruby','c','java']
print(tuple1)
print(list1)
# Let's include windows in the list and it works!
list1[1] = "windows"
print(list1)
# Windows does not work here!
tuple2 =tuple1[:1]+('windows',)+tuple1[2:] 
print(tuple2)

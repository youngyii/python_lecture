'''
my_set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1}
print(my_set)
print(setItem)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
print(*my_set)
'''
'''
my_set = set([5, 8, 3, 7, 1, "h"])
print(my_set)

set_tmp = set("hello")
print(set_tmp)
'''

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)
print(my_set.union(set_item))

print(my_set - set_item)
print(my_set.difference(set_item))

print(my_set & set_item)
print(my_set.intersection(set_item))

print(my_set)
my_set.add(9)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.update([5, 9, 7, 4])
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.clear()
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.remove(5)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.discard(2)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set)
my_set.difference_update(set_item)
print(my_set)

my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)
#print(my_str + 10) #에러
print(my_str + " hello")

my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int)
print(my_int + 10)
#my_int2 = int("ten") #에러
#print(my_int2)

'''
x = 10
y = 3
print(x + y)    
print(x - y)    
print(x * y)    
print(x / y)    
print(x % y)    
print(x // y)   
print(x ** y) 
'''  
'''
a = 0
print(a)
a += 2
print(a)
a -= 1
print(a)
a *= 4
print(a)
a /= 2
print(a)
a **= 3
print(a)
'''
'''
x = 10
y = 4
print(x > y)    
print(x < y)    
print(x >= y)   
print(x <= y)   
print(x == y)   
print(x != y)   
'''
'''
a = 1
b = 0
print(a and b)  
print(a or b)   
print(not a)    
print(not b)
x = True
y = False
print(x and y)  
print(x or y)   
print(not x)    
print(not y)
'''
'''
x = 10
y = 3
print(x & y)   
print(x | y)   
print(x ^ y)   
print(~x)      
print(x << 2)  
'''
'''
my_list = [9, 4, 3, 7, 8, 'hi']
print(4 in my_list)

print(2 in my_list)
print(2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print('k2' in my_dic)
'''
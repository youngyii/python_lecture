'''
my_var = 10
print(my_var)  

my_list = [1, 2, 3]
print(*my_list)

# 정수
my_int = 10
print(my_int)

# 부동 소수점
my_float = 3.14
print(my_float)

# 복소수
my_complex = 3 + 4j
print(my_complex)

my_character = 'A'
print(my_character)
my_char = "@"
print(my_char)

my_string = 'Hello, World!'
print(my_string)
str_name = "python"
print(str_name)

my_bool = True
print(my_bool)
bFlag = False
print(bFlag)
'''
'''
my_list = [1, 2, 'three', True]
print(my_list)
lsElement = [3.14, "b", 'two', False]
print(lsElement)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)
print(*my_list)
print(my_list.__len__())
print(my_list[3])
list_el = my_list[2]
print(list_el)
my_list[3] = 11
print(my_list)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)
n_add = my_list[3] + my_list[2]
print(n_add)

print(my_list[2:5])
print(my_list[:3])
print(my_list[4:])

my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]
print(my_list)
print(my_list[6][2:])
print(my_list[5][2])
'''
'''
my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
my_list.insert(2, 4)
print(*my_list)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list.index(3))
#print(my_list.index(4)) #에러

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
my_list.append(22)
print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list.count(8))
print(my_list.count(5))

print(my_list)
print(my_list.pop())
print(*my_list)

print(my_list)
my_list.sort()
print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
#my_list.sort() #에러
#print(*my_list)

my_list.reverse()
print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]
print(my_list, list_tmp)
my_list.extend(list_tmp)
print(*my_list)

list_tmp.clear()
print(list_tmp)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
my_list.remove(3)
print(*my_list)
#my_list.remove(2) #에러
#print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
del my_list[2]
print(*my_list)
'''
'''
my_tuple = (1, 2, 'three', True)
print(my_tuple)
tpItem = (3.14, "b", 'two', False)
print(tpItem)

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(*my_tup)
print(my_tup.__len__())

print(my_tup[2])
#my_tup[3] = 2 #에러
#print(*my_tup)

print(my_tup[2] + my_tup[0])
print(*my_tup)

n_add = my_tup[1] + my_tup[3]
print(n_add)

print(my_tup[2:5])
print(my_tup[1:4])
print(my_tup[:3])
print(my_tup[2:])

my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup)
print(my_tup[6][0])

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup.index(2, 0, 3))

print(my_tup.index("py", 3, 5))

#print(my_tup.index(1, 0, 3)) #에러
'''
'''
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(*my_dict)
dicData = {"name" : "python", "number" : 23564897}
print(dicData)

my_item = my_dict.items()
print(my_item)

idx = ("key1", "key2", "key3")
dicts = dict.fromkeys(idx, "0")
print(dicts)

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict["key1"])

my_str = my_dict.get("key2")
print(my_str)

print(my_dict.pop("key1"))
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}
my_dict["key3"] = "value3"
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.setdefault("key3")
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update({"key1": "v4"})
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
del my_dict["key2"]
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
print("key2" in my_dict)
print("key3" in my_dict)

my_list = list(my_dict.keys())
print(my_list)
my_list = list(my_dict.values())
print(my_list)

my_set = set(my_dict.keys())
print(my_set)

my_dict.clear()
print(my_dict)
'''
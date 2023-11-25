'''
# 식별 연산
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)

a = 5
b = 5
print(a is b)
print(a is not b)

3 == 3.0
3 is 3.0

a = 3
b = 3.0

print(a == b)
print(a is b)
print(a is not b)

a = [3 ,5, 1]
b = a
print(a is b)

a[0] = 2
print(a, b)
print(a is b)
'''
'''
# 연산자 우선순위
x = 2 ** 3 ** 2
print(x)    

x = 2 + 3 * 4
print(x)  

x = 10 / 5 / 2
print(x)  

x = 2 ** 3 ** 2
print(x)  

x = 2 ** (3 ** 2)
print(x)  

x = 10 % 3 % 2
print(x)  

x = 1 + 2 > 3
print(x)   

x = 4 - 1 < 2
print(x)  

x = not False and True
print(x) 

x = not True or False and True
print(x) 

x = 1 & 2 | 3 ^ 4
print(x) 

x = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
print(x) 

x = 2 * -3 // 2
print(x) 

x = 1 == 2 != 3
print(x)
'''
'''
# 조건문 if
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
'''    
'''
# 1
x = 3
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")
    
#2
x = 5
y = 3
if x == y:
    print("같다")
else:
    print("다르다")
    
#3
x = 'a'
if x == 'a':
    print("a이다")
elif x == 'b':
    print("b이다")
else:
    print("a도 b도 아니다")
'''  
'''
# for
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# 이중 for
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in my_list:
    for num in row:
        print(num)

# 0~9 출력
for i in range(10):
    print(i)
    
# 문자열 한 글자씩
for char in "Python":
    print(char)
    
# reversed
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)
    
# sorted
for fruits in sorted(fruits):
    print(fruits)

# 구구단
for i in range (1,10):
    for j in range (1,10):
        print(i, "x", j, "=", i * j)
'''
'''        
# for ~ else문
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
 
# 반복 종류후 실행할 코드
else: 
	print("end process")
'''
'''
# 반복문 제어
for i in range(10):
    if i == 7:
        print("break", i)
        break
    elif i == 1:
        print("continue", i)
        continue
    else:
        print("pass", i)
        pass

    print(i)
'''
'''
# while
i = 1

while i <= 5:
    print(i)
    i += 1
    
# 0 ~ 9
i = 0
while i <= 9:
    print(i)
    i += 1
    
# 문자열 한 글자씩
word = "python"
i = 0

while i < len(word):
    print(word[i])
    i += 1
    
# 1 ~ 10 총합
i = 1
result = 0

while i <= 10:
    result += i
    i += 1
    
print(result)

# 1 ~ 100 짝수, 홀수 출력
i = 1
while i <= 100: 
    if i % 2 == 0:
        print(i," : 짝수")
    else:
        print(i," : 홀수")
    i += 1    
    
# 7의 배수
i = 1
while i <= 100: 
    if i % 7 == 0:
        print(i)
    i += 1
'''
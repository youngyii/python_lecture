'''
# 1. 삼각형 출력
# 1번 역직각삼각형
for i in range(1, 6):
    print("*" * (6 - i))
'''
'''    
for i in range(5, 0, -1):
    print("*" * i)
'''
''' 
# 2번 직각삼각형 
for i in range(1, 6):
    print("*" * i)
'''
'''
# 3번 이등변삼각형
for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
'''
'''
# 4번 다이아몬드
for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
'''   
'''
# 2. 5x5 출력

# 정상출력
num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = []
'''
'''
# 세로출력
n = 0
line = []
for i in range(5):
    n += 1
    num = n
    for j in range(5):
        line.append(num)
        num += 5
    print(line)
    line = []
'''
'''
line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = []
'''    
'''
# 역순출력
num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = []
'''
'''
# 가위, 바위, 보 게임
import random

def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum :
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2')
    ) :
        print("승")
        return
    else : 
        print("패")
        return

print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요!")
chnum = input()
determine_winner(chnum)
'''
'''
# 파일 생성
#file = open("new.txt", "w")
file = open("temp.txt", "w")
file.close()
'''
'''
# 파일 쓰기
file = open("temp.txt", "w")

file.write("hello")
file.write("world")

file.close()
'''
'''
file = open("temp.txt", "w")

file.write("hello\n")
file.write("world")

file.close()
'''
'''
# 0~100
file = open("temp.txt", "w")

for i in range(101) :
    file.write(f"{i}\n")

file.close()
'''
'''
# C:\\Users\\Catholic\\temp.txt
f = open("C:\\Users\\Catholic\\temp.txt") 
for i in range(101) :
    f.write(f"{i}\n")
f.close()
'''
'''
# 추가 쓰기
file =open("temp.txt", "a")
file.write("hello\n")
file.write("world")
file.close()
'''
'''
# 파일 읽기
file = open("temp.txt", "r")
res = file.read()
print(res)
file.close()
'''
'''
# 다른경로 파일 읽기
file = open("C:\\Users\\Catholic\\temp.txt", "r")
res = file.read()
print(res)
file.close()
'''
'''
# readline
f = open("temp.txt", "r")
for i in range(110) :
    res = f.readline()
    print(res)
f.close
'''
'''
# readlines 읽기
f = open("temp.txt", "r")
res = f.readlines()
print(res)
f.close()
'''
'''
f = open("temp.txt", "r")
line = f.readlines()
for l in line :
    print(l)
f.close()
'''
'''
# file object
f = open("temp.txt", "r")
for line in f :
    print(line)
f.close()
'''
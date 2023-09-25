'''
# datetime 이용 함수

from datetime import datetime as dt
# 현재 시간 출력
print(dt.now())

# 특정 시간대의 현재 시간 출력
#from pytz import timezone
# tz = timezone('ASia/Seoul')
#tz = timezone('UTC')
#print("timezone : ", dt.now(tx))

# 문자열을 날짜로 변환
date_string = '2021-07-08'
date_object = dt.strptime(date_string, "%Y-%m-%d")
print(date_object)

# 날짜를 문자열로 변환
date_object = dt.now()
date_string =date_object.strftime('%Y-%m-%d')
print(date_string)
'''
'''
import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

#res = mu.cvt_str2time()
'''
'''
# os 모듈 확인
import os

# 현재 작업 디렉토리 출력
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')
print(os.getcwd())

# 파일 목록 출력
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())

# 디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())
'''
'''
import mod.utils as mu
import os

print(mu.get_curdir())

pname= "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())
'''
'''
import sys

print(sys.version)
print(sys.argv)
'''
'''
import numpy as np

np.array

np.zeros
np.ones

np.array([1, 2, 3])
np.array([4, 5, 6])
f = d + e
g = d - e
h = d * e
i = d / e
'''
'''
# stack
st = []

# 스택에 값 넣기
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

# 스택의 상태 확인
print(st) #[1, 2, 3]

# 스택에서 값 빼기
top = st.pop()
print(top) #3
print(st)
print(len(st))
'''
'''
# append, pop 이용한 queue
# 빈 큐 생성
queue = []

# 큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# 큐의 상태 확인
print(queue)

# 큐에서 값 빼기
front = queue.pop(0)
print(front)
print(queue)
print(len(queue))
'''
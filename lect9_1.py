'''
# 비동기처리1
import asyncio
import random as rd

async def tester(name):
    snum = rd.randint(10, 20)
    print(f"{name} - {snum}")
    for i in range(snum) :
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")

    print(f"end of {name}")

async def main():
    task1 = asyncio.create_task(tester("1test"))
    task2 = asyncio.create_task(tester("2test"))
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    await task1
    await task2
    await task3
    print("end")

if __name__ == '__main__':
    asyncio.run(main())
'''
'''
# 비동기처리2
import asyncio

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)

async def worker2():
    for i in range(1, 4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)

async def main():
    task1 = asyncio.create_task(worker1())
    task2 = asyncio.create_task(worker2())

    print("start task")
    await task1
    await task2
    print("end task")

if __name__ == '__main__':
    asyncio.run(main())
'''
'''
# 스케쥴
import time
import sched

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
    
    print(f"end of {name}")

def run():
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(5, 1, tester, ('4num',))
    s.enter(3, 1, tester, ('2num',))
    s.enter(7, 1, tester, ('3num',))
    s.run()
# endter{지연시간}, {우선순위}, {실행함수}, {전달인자}

if __name__ == "__main__":
    run()
    print("end")
'''
'''
# 문자열 비교
import diff_match_patch.diff_match_patch as dm
origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d)
'''
'''
# 테스트용 데이터 생성
from faker import Faker as fk

temp = fk("ko-KR")
print(temp.name())

print(temp.name() + "\n" + 
    temp.address() + "\n" + 
    temp.postcode() + "\n" + 
    temp.company() + "\n" + 
    temp.job() + "\n" + 
    temp.phone_number() + "\n" + 
    temp.email() + "\n" + 
    temp.user_name() + "\n" + 
    temp.ipv4_private() + "\n" + 
    temp.ipv4_public() + "\n" + 
    temp.catch_phrase() + "\n" + 
    temp.color_name() + "\n")
'''
'''
from faker import Faker as fk

temp = fk("ko-KR")
print(temp.name())

with open("fktemp.csv", "w", newline='') as f:
    for i in range(30):
        f.write(temp.name() + "\n" + 
            temp.address() + "\n" + 
            temp.postcode() + "\n" + 
            temp.company() + "\n" + 
            temp.job() + "\n" + 
            temp.phone_number() + "\n" + 
            temp.email() + "\n" + 
            temp.user_name() + "\n" + 
            temp.ipv4_private() + "\n" + 
            temp.ipv4_public() + "\n" + 
            temp.catch_phrase() + "\n" + 
            temp.color_name() + "\n")
'''
'''
#시스템명령어 사용
import subprocess as sp

res = sp.run(["cmd", "/c", "dir"], capture_output=True)
res2 = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=True)
print(res)
'''
'''
# 에러처리
import traceback as tb

def tester():
    return 1/0

def caller():
    tester()

def main():
    try:
        caller()
        
    except ZeroDivisionError:
        print("zde error")
        
    except ValueError:
        print("ve error")
        
    except Exception as ex:
        print("ex error", ex)
        
    else:
        print("ok")
        
    finally:
        print("end")

if __name__ == "__main__":
    main()
'''
'''
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

pres = res_html.find("h1")
print(pres)
print("\n1----------------------------------\n")
print(pres.get_text().strip())
print("\n2----------------------------------\n")
print(pres.next_element.get_text().strip())
print(pres.get_text())
print("\n6----------------------------------\n")

tres = res_html.find("title")
print(tres)
print("\n3----------------------------------\n")
print(tres.next_element)
print("\n4----------------------------------\n")
print(tres.get_text().strip())

fares = res_html.findAll("a")
for i in fares:
    print(i.get_text())
print("\n5----------------------------------\n")

clres = res_html.findAll(class_ = "doc-title")
print(clres)

print("\n6----------------------------------\n")
clrs = res_html.find(class_ = "head_top")
print(clrs)
print(clrs.get_text())
'''
'''
# 셀렉터로 찾기
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("body > div.container-doc > main > section > div > div.content-article > div.box_g.box_news_issue > ul > li:nth-child(1) > div > div > strong > a")

print(item)
print(item.get_text())
'''
'''
# select one 
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods.get_text())
'''
'''
# selct

from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")

print("\n-----------------------\n")

for i in iss :
    issue = i.get_text()
    print(issue)
    
print("\n-----------------------\n")
ct = res_html.select("a.warp_thumb")
for j in ct :
    c = j.attrs["data-tiara-custom"]
    print(c + "\n")
'''
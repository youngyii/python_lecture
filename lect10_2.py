'''
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)
'''
#print(df.name == "박지후")
#print(df.company == "심김")

#temp = df[df.postcode > 70000]
#print(temp)

#res = df[df.color == "Gold"].head(1)
#print(res)

#res = df[df.postcode > 70000][["name" , "postcode", "color"]]
#print(res)
#print(res.count())

#temp = df.postcode.mean()
#temp = df.postcode.sum()
#print(temp)

#temp = df[df.color == "Gold"].postcode.mean()
#print(temp)

#temp = df[df.color == "Gold"].postcode.sum()
#print(temp)

#temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
#temp = df[df.postcode > df.postcode.mean()]
#print(temp)

#결측확인
#temp = df.company.isnull()
#temp = df.company.empty
#temp = df[df.company.isnull()][["name", "postcode"]]
#print(temp)

'''
temp = df.company.isnull()
for el in temp:
    if el == False:
        print(el)
'''

#temp = df.name.empty
'''
#temp = df[(df.color == "Gold")]
temp = df[~(df.color == "Gold")][["name"]]
print(temp)
print(temp.count())
'''
'''
#and 연산
temp = df[(df.color == "Ivory") & (df.postcode > 70000)]
print(temp)
'''
'''
#or 연산
#temp = df[(df.color == "Beige") | (df.postcode > 70000)]
temp = df[(df.color == "Beige") | (df.postcode > 70000)][["name"]]
print(temp)
'''
'''
#정렬
#temp = df.sort_values("postcode")
#temp = df.sort_values("name", ascending=False)
temp = df.sort_values("name", ascending=True)
print(temp)
'''
'''
# 데이터 재배열
col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)

print(df)

print("\n------------------------------------\n");
print(df.pivot(index='Machine',columns='Country',values='Price'))
print(df.pivot(index='Brand',columns='Machine',values='Price'))
print(df.pivot(index='Country',columns='Machine',values='Price'))
print(df.pivot(index='Price',columns='Brand',values='Machine'))
'''
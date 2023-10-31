#첫별수를 입력하세요. 1
#끝별수를 입력하세요. 3
#*
#**
#***

def getStar(cnt):
    txt = ""
    for i in range(cnt):
        txt+="*"
    return txt   

#문자열
a = input("첫 별수를 입력하세요.")
b = input("끝 별수를 입력하세요.")

#정수형
aa = int(a)
bb = int(b)

for i in range(aa,bb+1):
    print(getStar(i))



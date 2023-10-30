#첫별수를 입력하세요. 1
#끝별수를 입력하세요. 3
#*
#**
#***


a = input("첫 별수를 입력하세요.")
b = input("끝 별수를 입력하세요.")

aa = int(a)
bb = int(b)

arr = range(aa,bb+1)

for i in arr:   
    print('*'*i)
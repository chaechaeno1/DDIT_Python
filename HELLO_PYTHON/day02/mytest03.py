# 첫수를 입력하시오. 1
# 끝수를 입력하시오. 4
# 1에서 4까지의 합은 10입니다.


a = input("첫수를 입력하시오.")
b = input("끝수를 입력하시오.")

#문자열을 정수형으로 변환
a = int(a)
b = int(b)


arr = range(a,b+1)
sum = 0;

for i in arr:
    sum += i
    
print("{}에서 {}까지의 합은 {}입니다.".format(a,b,sum))  


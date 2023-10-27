# 첫 수를 입력하시오. 1
# 끝 수를 입력하시오. 6
# 배수를 입력하시오. 3
# 1에서 6까지의 3의 배수의 합은 9입니다.


#문자열
a = input("첫 수를 입력하시오.")
b = input("끝 수를 입력하시오.")
c = input("배수를 입력하시오.")

#구분해서 정수형 만들기
aa = int(a)
bb = int(b)
cc = int(c)

arr = range(aa,bb+1)
sum = 0;

#arr[i] 아니고 i로 두어야 함
for i in arr:
    if i%cc==0 :
        sum += i 
        
         
print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(a,b,c,sum))
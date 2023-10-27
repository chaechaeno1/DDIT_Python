# 출력할 단수를 입력하세요. 5
# 5*1=5
# 5*2=10
# 5*3=15
# ...
# 5*9=45

dan = input("출력할 단수를 입력하세요.")
idan = int(dan)

for i in range(1, 9+1):
    print("{} * {} = {}".format(dan,i,i*idan))



print("{} * {} = {}".format(dan,1,1*idan))
print("{} * {} = {}".format(dan,2,2*idan))



# 직접푼 것
# a = input("출력할 단수를 입력하세요.")
# #문자열 -> 정수형으로 변환
# aa = int(a)
#
# arr = range(1,9+1)
#
# for i in arr:
#     res = aa*i
#
#     print("{} * {} = {}".format(aa,i,res))
#


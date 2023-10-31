

# 9,7,5,3단 순으로 출력하기
#9,8,2단 순으로 출력하기
# arr1 = range(9,7,-1) #단
# arr2 = range(1,9+1) # 1~9까지
# arr3 = range(2,3)
#
#
#
# for i in arr1:
#     for j in arr2:
#         print("{}*{}={}".format(i,j,i*j))
#
# for i in arr3:
#     for j in arr2:
#         print("{}*{}={}".format(i,j,i*j))       
        
        
# range범위 설정 
# range(A, B, C)
# A부터 B 숫자만큼의 간격으로 C-1 까지의 정수 범위를 반환합니다. 
# C까지가 아닌 C-1 이라는 것에 주의하세요.



def showDan(dan):
    print("{}*{}={}".format(dan,1,dan*1))
    print("{}*{}={}".format(dan,2,dan*2))
    print("{}*{}={}".format(dan,3,dan*3))
    print("{}*{}={}".format(dan,4,dan*4))
    #print("{}*{}={}".format(dan,5,dan*5))
    print("{}*{}={}".format(dan,6,dan*6))
    print("{}*{}={}".format(dan,7,dan*7))
    print("{}*{}={}".format(dan,8,dan*8))
    print("{}*{}={}".format(dan,9,dan*9))
    
showDan(9)
showDan(8)
showDan(2)









    
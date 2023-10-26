'''
Created on 2023. 10. 26.

@author: PC-09
'''


arr = ["홍길동", "전우치", "이순신"]
print(arr)
arr.append("홍범도")
print(arr)
arr.insert(len(arr), "도요토미") #insert 사용하여 append 기능까지 실행 가능
print(arr)

print(arr[0])
print(arr[-1]) #자바에서는 음수를 넣으면 오류 발생


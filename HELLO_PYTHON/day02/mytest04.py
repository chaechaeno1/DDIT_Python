# 홀/짝을 고르시오. 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리!
# (결과가 같은 경우에는 내가 이기는 게임)
from random import random


myNum = input("홀/짝을 고르시오.")
comNum = "";
res = "";

rnd = random()

if rnd > 0.5: comNum = "홀"
else : comNum = "짝"

if myNum==comNum : res = "승리!"
else : res = "패배.."

print("나 : "+myNum)
print("컴 : "+comNum)
print("결과 : "+res)     


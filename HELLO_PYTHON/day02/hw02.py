#업앤다운
#com = 1~99사이의 랜덤수 (화면X) - 50 이라 가정
#입력할 수를 넣으세요. 40
# 40 UP입니다.
# 입력할 수를 넣으세요.60
# 60 DOWN 입니다.
# 입력할 수를 넣으세요.50
# 50 정답입니다!
# 물어보는 횟수는 10번으로 제한
from random import random




mine = input("입력할 수를 넣으세요.")
intmine = int(mine)
com = int(random() * 100)

for i in range(1,10+1) :
    if intmine > com : print(mine + " DOWN 입니다.")
    elif intmine < com : print(mine + " UP 입니다.")
    else : print(mine + "정답 입니다.")
    

class Animal:
    
    def __init__(self): #생성자
        self.full = 1
        print("생성자")
        
    def eat(self, amount):
        self.full += amount #전역변수   
        
    def __del__(self):
        print("소멸자") 
        
class Human(Animal):
    
    def __init__(self):
        super().__init__() #Animal 호출
        self.flag_tool = False
    
    def momstouch(self):
        self.flag_tool = True
        
if __name__ == '__main__':
    ani = Human() #var ani = new Animal()
    print("ani.flag_tool",ani.flag_tool)
    print("ani.full",ani.full)    
    ani.eat(9)
    ani.momstouch()
    print("ani.flag_tool",ani.flag_tool)
    print("ani.full",ani.full)
    

#자바에는 소멸자가 따로 없음
    
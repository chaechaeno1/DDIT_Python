class xi:
    
    def __init__(self):
        self.cnt_nuclear = 1000;
        
    def dieDeveloper(self, count):
        self.cnt_nuclear += count
         
class LeeJY:
    
    def __init__(self):
        self.asset = 400
        self.factory = 20
        
    def buildFactory(self):
        self.asset -= 4
        self.factory += 1
         
class Musk:
    
    def __init__(self):
        self.cnt_sat = 20000
        
    def shootRocket(self):
        self.cnt_sat += 100
        

class LeeGunJung(xi,LeeJY,Musk):
    
    def __init__(self):
        xi.__init__(self)
        LeeJY.__init__(self)
        Musk.__init__(self)


lgj = LeeGunJung()
print(lgj.cnt_nuclear)      
print(lgj.asset)      
print(lgj.factory)      
print(lgj.cnt_sat)
lgj.dieDeveloper(1000)
lgj.buildFactory()
lgj.shootRocket()
print(lgj.cnt_nuclear)      
print(lgj.asset)      
print(lgj.factory)      
print(lgj.cnt_sat)  

        
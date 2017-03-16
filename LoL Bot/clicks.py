import win32com.client as client
from time import sleep
import time

#clicks has all functions that require keyboard or mouse input
class clicks:

    def __init__(self, au):
        self.autoit = au
        self.autoit.Sleep(2000)
        self.level = 0
        self.escape = False
  
    def aMove(self):
        self.autoit.MouseClick("middle", 231 , 828)
        
    def recall(self):
        self.autoit.Send("t")
        self.autoit.MouseClick("left", 1050, 962)
        
    def goBack(self, wait):
        self.autoit.MouseClick("right", 97, 961)
        if self.escape == True:
            self.autoit.MouseMove(self.placement[1][0], self.placement[1][1])
            self.autoit.Send("self.activespells[1]")
            self.cdescape = time.clock()
        #sleep delay, (miliseconds)
        sleep(wait)

    def shop(self):
        self.autoit.Send("b")
        self.autoit.MouseClick("left", 1616, 1032)
        sleep(0.5)
        self.autoit.MouseClick("left", 716, 260)
        for i in range(5):
            self.autoit.MouseClick("right", 1040 , 674)
            sleep(0.5)
        self.autoit.Send("b")
        self.autoit.MouseClick("left", 1649, 197)

    def ability(self, x, y, ability):
        self.autoit.MouseMove(x, y)
        self.autoit.Send(ability)

    def flash(self):
        self.autoit.MouseMove(97, 961)
        self.autoit.Send("d")

    def heal(self):
        self.autoit.Send("f")
        self.autoit.MouseClick("left", 1001, 961)

    #lvl up skills
    def skill(self, spell):
        if spell[self.level] == 1:
            self.autoit.Send("!q")
            self.autoit.MouseClick("left", 730, 904)
        elif spell[self.level] == 2:
            self.autoit.Send("!w")
            self.autoit.MouseClick("left", 783, 904)
        elif spell[self.level] == 3:
            self.autoit.Send("!e")
            self.autoit.MouseClick("left", 834, 904)
        elif spell[self.level] == 4:
            self.autoit.Send("!r")
            self.autoit.MouseClick("left", 889, 904)
        self.level += 1
        
        
    def champrotation(champ):
        self.spells, self.activespells, self.placement, self.cdq, self.cde = champ
        if time.clock() - cd > self.cdq[self.level-1]:
            self.autoit.MouseMove(self.placement[0][0], self.placement[0][1])
            self.autoit.Send("self.activespells[0]")
            cd = time.clock()
                        
        if len(self.activespells) == 2 and time.clock() - cd.escape > self.cde[self.level-1]:
            self.escape = True
        
        

from clicks import clicks
#from champs import champs
from scraper import scraper
from time import sleep
import win32com.client

if __name__=="__main__":
    count = 0
    stage = 0
    autoit = win32com.client.Dispatch("AutoItX3.Control")
    autoit.WinActivate("League of Legends (TM) Client")
    bot = clicks(autoit)
    sc = scraper(autoit)
   # ch = champs()
  #  ashe = ch.ashe()
  #  caitlyn = ch.caitlyn()
    bot.shop()
    #run = time.clock()
    
    # Main loop
    while (autoit.WinGetTitle("") == "League of Legends (TM) Client"):
        count += 1

        #check hp status
        if not sc.searchPixel(759, 1018, 759, 1018, 5613123):
            bot.flash()
            bot.goBack(5)
            bot.recall()
            sleep(9)
            bot.shop()
            stage = 0
        else:
            if sc.searchPixel(995, 1013, 995, 1013, 4821050):
                stage = 0
            elif sc.searchPixel(910, 1011, 910, 1011, 4688696):
                stage = 1
            else:
                stage = 2
                
            if stage == 0 and not sc.searchPixel(995, 1013, 995, 1013, 4821050):
                bot.goBack(2)
            elif stage == 1 and not sc.searchPixel(910, 1011, 910, 1011, 4688696):
                bot.goBack(2)

            if not sc.searchPixel(910, 1011, 910, 1011, 4688696):
                bot.heal()
        
        #A-move up the middle
        if count > 2:
            bot.aMove()
            count = 0

        #lvl up
        #if sc.searchPixel(931, 902, 931, 902, 1904896):
        #    bot.skill(champ[0])

        #use skills
        #if time.clock()-run > 20:
        #    bot.champrotation(caitlyn)
         
        
        
       
    

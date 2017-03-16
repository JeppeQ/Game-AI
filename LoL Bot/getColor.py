import win32com.client as client
from time import sleep

autoit = client.Dispatch("AutoItX3.Control")


while(True):
    raw_input()
    print autoit.PixelGetColor(autoit.MouseGetPosX(),autoit.MouseGetPosY())
    print autoit.MouseGetPosX(),autoit.MouseGetPosY()
    

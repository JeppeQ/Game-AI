import win32com.client as client




autoit = client.Dispatch("AutoItX3.Control")
while(True):
    raw_input("Current: ")
    print autoit.MouseGetPosX(),autoit.MouseGetPosY()
    
    

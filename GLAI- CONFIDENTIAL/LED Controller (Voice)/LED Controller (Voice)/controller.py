import pyfirmata

comport='COM9'

board=pyfirmata.Arduino(comport)

led1=board.get_pin('d:13:o')
led2=board.get_pin('d:12:o')
led3=board.get_pin('d:11:o')
led4=board.get_pin('d:10:o')
led5=board.get_pin('d:8:o')

def led(val):
    if val==1:
        led1.write(1)
    elif val==2:
        led1.write(0)
    elif val==3:
        led2.write(1)
    elif val==4:
        led2.write(0)
    elif val==5:
        led3.write(1)
    elif val==6:
        led3.write(0)
    elif val==7:
        led4.write(1)
    elif val==8:
        led4.write(0)
    elif val==9:
        led5.write(1)
    elif val==10:
        led5.write(0)
    elif val==11:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
   


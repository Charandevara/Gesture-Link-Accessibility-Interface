import pyfirmata

comport='COM6'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:8:o')

def led(total):
    if total==0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==1:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif total==4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif total==5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)

    elif total==6:
        led_1.write(1)
    elif total==7:
        led_1.write(0)
    elif total==8:
        led_2.write(1)
    elif total==9:
        led_2.write(0)
    elif total==10:
        led_3.write(1)
    elif total==11:
        led_3.write(0)
    elif total==12:
        led_4.write(1)
    elif total==13:
        led_4.write(0)
    elif total==14:
        led_5.write(1)
    elif total==15:
        led_5.write(0)
    elif total==16:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    
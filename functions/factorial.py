# Made by Spyridon Manolidis | 28/10/2023
import ctypes
def factorial(n):
    '''Runs the mathematical factorial function, denoted by n!'''
    x = 1
    try:
        for i in range(n):
            x = x*(i+1)
    except:
        print("The factorial function has failed - ensure value is an integer.\nProcess terminated.")
        try:
            ctypes.windll.user32.MessageBoxW(0,"The factorial function has failed - ensure value is an integer.\nProcess terminated.","Python Error",0x00000010)
        except:
            pass
        exit(1)
    return x

import pyautogui
import time

time.sleep(3) 
i = 0 

for i in range(1, 1000000):
    pyautogui.typewrite(str(i))
    # pyautogui.press("space")
    pyautogui.press("enter")

# include<string.h>

# int main( )
# {
# 	char source[ ] = "Kunal" ;
# 	char target[20]="Hello" ;
# 	printf ( "\nsource string = %s", source ) ;
# 	printf ( "\ntarget string = %s", target ) ;

# 	strcat ( target , source ) ;

# 	printf ( "\nsource string = %s", source ) ;//Kunal
# 	printf ( "\ntarget string = %s", target ) ;//HelloKunal
# }

# source = "Kunal"
# target = "Hello"
# target = target + source
# print(target) #KunalHello
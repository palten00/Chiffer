word = ""
key = 12
letters = []
crypt = []
meny = 0
char = []
hej = []
import time 
import sys

while meny !=3:
    meny = int(input(" 1 för att krypter:  \n 2 för att dekryptera:  \n 3 för att avsluta: "))
    if meny == 1:
        key = int(input("skriv in en siffra för att kryptera "))
        word = input("skriv in ett ord du vill kryptera ")
        animation = "/-\\ /-\\" 
        for i in range(10):    
            time.sleep(0.5)    
            sys.stdout.write("\r" + animation[i % len(animation)])   
            sys.stdout.flush() 
        for letter in word:
            letters.append(ord(letter) + key)
        for l in letters:
            char.append(chr(l ))
        print(char)
        
    elif meny == 2:
        key = int(input("skriv in en siffra för att dekryptera"))
        word = input("skriv in siffrorna för dom krypterade bokstävera ")
        for letter in word:
            hej.append(ord(letter))
        for l in letters:
            crypt.append(chr(l -key))
            
        print(crypt)
    elif meny ==3:
        animation = "/-\\ /-\\" 
        for i in range(100):    
            time.sleep(0.5)    
            sys.stdout.write("\r" + animation[i % len(animation)])   
            sys.stdout.flush() 
        print("nu avslutas programmet")
       

        






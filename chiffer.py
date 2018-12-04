word = ""
key = 12
letters = []
crypt = []
meny = 0

while meny !=3:
    meny = int(input("1 för att krypter \n 2 för att dekryptera"))
    if meny == 1:
        key = int(input("skriv in en siffra för att kryptera"))
        word = input("skriv in ett ord du vill kryptera")
        for letter in word:
            letters.append(ord(letter) + key)

        print(letters)
    elif meny == 2:
        key = int(input("skriv in en siffra för att dekryptera"))
        word = input("skriv in ett ord du vill dekryptera")
    
    for l in letters:
        crypt.append(chr(l -key))

    print(crypt)






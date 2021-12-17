number = input("press 1 to decrypt press 2 to encrypt")
bruther = " "
if number=="2":
    sentence2dec = input("please enter the words you want to encrypt")
    for word2dec in sentence2dec:
        for letter in word2dec:
            bruther = bruther + (chr(ord(letter) + 3))
    print(bruther)
elif number=="1":
    sentence2dec = input("please enter what you want to decrypt")
    for word2dec in sentence2dec:
        for letter in word2dec:
            bruther = bruther + (chr(ord(letter) - 3))
    print(bruther)
else:
    print("bruh you fucking retarted or something?")
   
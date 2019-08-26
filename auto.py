alphabet='abcdefghijklmnopqrstuvwxyz'
key = 4
newmsg=''
message=input("Enter your message : ")
print("1. To Encrypt")
print("2. To decrypt")

num = int(input("enter your option"))

if num==1:
    for character in message:
        position = alphabet.find(character)
        newposition = (position+key)%26
        newchar = alphabet[newposition]
        print('Encrypted new character is :',newchar)
        newmsg+=newchar
    print('The encrypted message is ', newmsg)
elif(num==2):
    for character in message:
        position = alphabet.find(character)
        newposition = (position-key)%26
        newchar = alphabet[newposition]
        print('Encrypted new character is :',newchar)
        newmsg+=newchar
    print('The encrypted message is ', newmsg)
else:
    print("Enter correct option")

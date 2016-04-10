# Michael Gardiner
# Due: 10-20-15
# Encode/Decode a given phrase by a given shift amount

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Also know as Caesar's cipher and the Shift cipher, this cyclic cipher
is an example of an encryption technique.
This cipher takes a phrase given to it, changes each character to an ASCII value,
shifts the ASCII value according to the given shift value, then returns the changed
ASCII values into characters to output the encrypted message.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def cypher():
    #Encode a phrase, changing only lowercase letters

    print ("This program encodes all lowercase characters in a phrase using a cyclic cipher.")
    phrase = input("Enter a phrase: ")
    newPhrase = ""
    value = int(input("Enter a shift value: "))

    for ch in phrase:
        if (ch >= 'a') and (ch <= 'z'):
            newPhrase = newPhrase + chr(((ord(ch)-ord('a'))+ value) % 26 + ord('a'))
        else:
            newPhrase = newPhrase + ch

    print ("Encoded phrase: ", newPhrase)

def supercypher():
    #Encode a phrase, changing lowercase, uppercase, and numbers.

    print ("This program encodes all characters and numbers in a phrase using a cyclic cipher.")
    phrase = input("Enter a phrase: ")
    newPhrase = ""
    value = int(input("Enter a shift value: "))

    for ch in phrase:
        if (ch >= 'a') and (ch <= 'z'):
            newPhrase = newPhrase + chr(((ord(ch)-ord('a'))+ value) % 26 + ord('a'))
        elif (ch >= 'A') and (ch <= 'Z'):
            newPhrase = newPhrase + chr(((ord(ch)-ord('A'))+ value) % 26 + ord('A'))
        elif (ch >= '0') and (ch <= '9'):
           newPhrase = newPhrase + chr(((ord(ch)-ord('0'))+ value) % 26 + ord('0'))
        else:
            newPhrase = newPhrase + ch

    print ("\nEncoded phrase: ", newPhrase, "\n")

def decode():
    #Decode the encoded phrase that was given

    phrase = input("Enter the code you would like to decode: ")
    newPhrase = ""
    value = int(input("Enter the shift value: "))
    
    for ch in phrase:
        if (ch >= 'a') and (ch <= 'z'):
            newPhrase = newPhrase + chr(((ord(ch)-ord('a'))- value) % 26 + ord('a'))
        elif (ch >= 'A') and (ch <= 'Z'):
            newPhrase = newPhrase + chr(((ord(ch)-ord('A'))- value) % 26 + ord('A'))
        elif (ch >= '0') and (ch <= '9'):
           newPhrase = newPhrase + chr(((ord(ch)-ord('0'))- value) % 26 + ord('0'))
        else:
            newPhrase = newPhrase + ch

    print ("\nDecoded phrase: ", newPhrase, "\n")
    
def main():

    answer = input("Would you like a regular cypher or a super cypher? Regular/Super: ")
    if answer.lower() == "regular" :
        cypher()
        ques = input("Would you like to decode your phrase? yes/no: ")
        if ques.lower() == "yes" :
            decode()
        else:
            print("Goodbye")
    elif answer.lower() == "super" :
        supercypher()
        ques = input("Would you like to decode your phrase? yes/no: ")
        if ques.lower() == "yes" :
            decode()
        else:
            print("Goodbye")
    else:
        print("Error")

main()
    

characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    # space and symbols
    #' ',',','.','?','!','@','#','$','&','*','(',')'
]


def csrCphr(message, alphabet): 
    for char in (message): 
        search =alphabet.index(char)
        yield search

msg = input("enter message:")
shift = int(input("enter shift:"))

def csrShift(inpshift):
    indexes = (csrCphr(msg, characters))
    for i in (indexes):
        ushift = i + inpshift
        charshift = characters.index(ushift)
        print (charshift)
    if charshift > 25: 
        yield
         
  

        





#msgindex = csrCphr(msg, characters)
print(list(csrCphr(msg, characters)))
print(csrShift(shift))

#print(csrCphr(msg, characters))


       #if search == (len(message)-1):
        #    + str(test_list[i]))
         #   yield search

#msg = input("Enter message:")


#shift = input("Enter shift:")

    #for i in range (len(characters)):   


#letter= iter(msg) 


#def csrShift(shift)

# Iterate over the string
#for value,char in enumerate(msg):
 #  print(char, end='')

        #nexChar= (next(letter))
        #alphabet= characters.index(letter)
        #return(next(letter))
        #return(nexChar == (next(search)))
        #return(characters.index(msg[0:]))
        #characters.index = letter 

#print(char)




#def Csr(letter, shift):
 #       csrmsg = " "
  #  if shift == 0:
   #     print ("nothing to shift")
    #else:
     #   for i in range(shift):
      #      shift += key

       # genKey += key[0:remainder]

        #return genKey

#def CsrLetter(letter, keyLetter):
#   letterBin = encode(letter)
 #   encryptedLetter = XORonByte(letterBin, keyLetterBin)
  #  return decode(encryptedLetter)


#def CsrSentence(sentence, key):
    
 #   encryptedSentence = ""
  #  genKey = generateKey(sentence, key)
   # for i in range (len(sentence)):
        
    #    encryptedSentence += XORonLetter(sentence[i], genKey[i])

#def shiftchar(characters):
    #for i in range(len(characters)):

    #return shift[+= ]

#print("Your encrypted message is:", XORonSentence(msg, shift))

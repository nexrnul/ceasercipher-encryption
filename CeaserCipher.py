characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
#def encode(character):
    #charIndex = characters.index(character)
    #return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
#def decode(binary):
 #   charIndex = int(binary, 2)
  #  return characters[charIndex]


def csrCphr(message, alphabet): 
    for char in (message): 
        search =alphabet.index(char)
        if message

msg = input("Enter message:")



def filter_odd(numbers):

   for number in range(numbers):

       if(number%2!=0):

           yield number 

odd_numbers = filter_odd(20)

print(list(odd_numbers))





#x= xcute()

print(xcute(msg, characters))

#msg = input("Enter message:")

print(csrCphr(msg, characters))



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

import os
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]


def csrCphr(message, alphabet): 
    for char in (message): 
        search =alphabet.index(char)
        yield search

def csrShift(inpshift, alph):
    indexes = (list(csrCphr(msg, characters)))
    shiftd_output= []
    for i in indexes:
        ushift = i + inpshift
        charshift = alph[ushift]
        shiftd_output.append(charshift)
    return ''.join(shiftd_output)


msg = input("enter message:")
shift = int(input("enter shift:"))        
outputt= csrShift(shift, characters)
os.system('clear')

print("your decoded msg is: " +msg)
print("using the Caesar Cypher with shift [{}] your input was encrypted to: {}".format(shift, outputt))



#TRASHD CODE:



        #charshift = alph.index(ushift)
    #yield charshift
#print(list(csrCphr(msg, characters)))
#print(list(csrShift(shift, characters)))
#encrtpyion = [alph[i] for i in charshift]
#def findElements(lst1, lst2):
#return [lst1[i] for i in lst2]
# Driver code
#lst1 = [10, 20, 30, 40, 50]
#lst2 = [0, 2, 4]
#print(findElements(lst1, lst2))
#if charshift > 25: 
        #yield
#msgindex = csrCphr(msg, characters)
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

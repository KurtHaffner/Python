def englishToYoda(Englishphrase):

    contract = {"don't" : "do not", "can't" : "can not", "won't" : "will not", "aren't" : "are not", "couldn't" : "could not", "doesn't" : "does not"}

    #phraseLen = (len(Englishphrase)) - 1
    end = Englishphrase[-1:]

    #Makes the first word lower case. At the end, make the first letter of first word upper case.
    newPhrase = Englishphrase[:-1]
    if (Englishphrase[:1] != 'I'):
        
        newPhrase = newPhrase.lower()
        
    newString = newPhrase.split()

    #Stuff to put first two words on the end.
    first = newString[0]
    second = newString[1]

    newString.pop(0)
    newString.pop(0)
    newString.append(first)
    newString.append(second)
    #/Stuff

    #!!!!!!Still needs to be fixed! Can't look up in the dictionary for some reason.!!!!!!
    for i in range(0,((len(newString))-1)):
        if newString[i] in contract:
            phrase = newString[i]
            newString[i] = contract[phrase]

    #Taking out nto and adding it to the end.
    if 'not' in newString:
        newString.remove('not')
        newString.append('not')

    print(newString)

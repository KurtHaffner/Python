def englishToYoda(Englishphrase):

    import random

    final = ""

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

    #Break ups the contractions and builds new string.
    for i in range(0,(len(newString))):
        if newString[i] in contract:
            phrase = newString[i]
            final = final + contract[phrase] + " "
        else:
            final = final + newString[i] + " "

    #Split the new string up again.
    newString = final.split()

    #Taking out not and adding it to the end.
    if 'not' in newString:
        newString.remove('not')
        newString.append('not')

    endings = ["... hmmm...", "... yes...", "... herh, herh, herh..."]

    final = ""

    for i in range(0, (len(newString) - 1)):
        final = final + newString[i] + " "

    final = final + newString[(len(newString))-1]

    if (end == '?'):
        final = final + "? Hmmmm...?"
    else:
        rand = (int)(random.uniform(0,2))
        final = final + endings[rand]

    #Print when you are done.
    print(final)

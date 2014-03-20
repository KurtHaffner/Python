def englishToYoda(Englishphrase):

    #Import random for random numbers.
    import random

    #Set final to a blank string.
    final = ""

    #Dictionary for contractions.
    contract = {"don't" : "do not", "can't" : "can not", "won't" : "will not", "aren't" : "are not", "couldn't" : "could not", "doesn't" : "does not", "isn't" : "is not", "wasn't" : "was not", "haven't" : "have not", "shouldn't" : "should not", "didn't" : "did not", "hasn't" : "has not", "mustn't" : "must not", "wouldn't" : "would not"}

    #Set end to the punctuation at the end. This will
    #help with knowing if a question was asked.
    end = Englishphrase[-1:]

    #Makes the first word lower case. At the end, make the first letter of first word upper case.
    newPhrase = Englishphrase[:-1]
    if (Englishphrase[:1] != 'I'):
        
        newPhrase = newPhrase.lower()

    #Split the newString into a list of words.    
    newString = newPhrase.split()

    #Put a comma on the end, so that it seperates the added words on the end.
    length = len(newString)
    newString[(length-1)] = newString[(length-1)] + ","

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

    #List of possible endings, already including the punctuation.
    endings = ["... Hmmm...", "... Yes...", "... Herh, herh, herh..."]

    #Set final to a blank string again.
    final = ""

    #Build the string with spaces after each word
    #leaving off the last word.
    for i in range(0, (len(newString) - 1)):
        final = final + newString[i] + " "

    #Add the last word onto the end, with no space after.
    final = final + newString[(len(newString))-1]

    #Make the first word uppercase.
    begin = final[:1]
    begin = begin.upper()

    #Add the lower case letter and the string after the first letter
    #back into final.
    final = begin + final[1:]

    #Choose an ending based on statement or question.
    if (end == '?'):
        final = final + "? Hmmmm...?"
    else:
        rand = (int)(random.uniform(0,2))
        final = final + endings[rand]

    #Print when you are done.
    print(final)

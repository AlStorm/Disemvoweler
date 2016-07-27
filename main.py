#List of vowels
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

#Initiates either the consonant collect function or the vow collect function.
def collectPrompt():
    collectChoice = input(str("\nWrite \"c\" to collect consonants from a sentence.\nWrite \"v\" to collect vows from a sentence.\nWrite \"b\" to collect both from a sentence.\n"))
    if collectChoice == "c":
        print(consonantCollect(str(input("Collect consonants: "))))
    elif collectChoice == "v":
        print(vowCollect(str(input("Collect vows: "))))
    elif collectChoice == "b":
        bothCollect = str(input("Collect both: "))
        print("Consonants:", consonantCollect(bothCollect))
        print("Vows:", vowCollect(bothCollect))

#Consonant collect function.
def vowCollect(sentence):
    vowString = ""
    for i in sentence:
        if i in vowels:
            vowString += i
    return vowString

#Vow collect function.
def consonantCollect(sentence):
    consonantString = ""
    for i in sentence:
        if i not in vowels and i != " ":
            consonantString += i
    return consonantString

collectPrompt()
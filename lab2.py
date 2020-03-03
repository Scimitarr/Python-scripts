print("------------ZADANIE-1--------------------")
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 1
capital = initialCapital
while year <= maxTimeYears:
    capital = capital * (1+percent)
    print("Capital at the end of %d year is %d" % (year, capital))
    year += 1
print("Through %d years You earned %d" % (maxTimeYears, capital - initialCapital))
print("\n------------------ZADANIE-2---------------")
number = 20730906
print(number)
sumaCyfr = 0
iloscZnakow = len(str(number))
x = number
i = 1
while i <= iloscZnakow:
    sumaCyfr = sumaCyfr + x % 10
    x = x // 10
    i += 1
print("Suma cyfr liczby %d wynosi %d" % (number, sumaCyfr))
print("\n------------------ZADANIE-3---------------")
text = "United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier."
print(text)
wordLength = 6
listOfWords = text.split(" ")
shortWords = 0
longWords = 0
for word in listOfWords:
    if len(word) > wordLength:
        longWords += 1
    else:
        shortWords += 1
print("Ilosc slow dluzszych niz 6: %d, a krotszych lub rownych 6: %d" % (longWords, shortWords))




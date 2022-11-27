#!/usr/bin/env python3

def acceptInput():
    num=int(input("Please enter an integer between 1 and 5000:\t"))
    while num < 0 or num > 5000:
        num=int(input("Please enter an integer between 1 and 5000:\t"))
    return num

def primeNumTester(num, fl):
    isP=True
    for i in range(num):    #calculate and store its factors
        if num%(i+1) == 0:
            fl.append(i+1)
    if len(fl)>2:           #check if its a prime number or not
        isP=False
    return isP

def displayResult(num, isP, fl):
    if isP == True:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is NOT a prime number")
        print(f"It has {len(fl)} factors: {fl}")
        

def main():
    factorList=[]
    cont="y"
    while cont == "y" or cont == "Y":   #while loop will repeat over and over till user decides not to
        number=acceptInput()            #acceptInput function will take user input, check if its valid, return it
        isPrime=primeNumTester(number, factorList)  #primeNumTester will check if its a prime num or not and record its factors in the list
        displayResult(number, isPrime, factorList)  #displayResult will display to the user if the number is prime or not, and its factors
        factorList.clear()
        cont=input("Try again? (y/n):\t")
    print("Bye")

    
if __name__ == "__main__":
    main()

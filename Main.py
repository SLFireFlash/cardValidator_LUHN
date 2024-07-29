
def validator(card):
    finalTot =0
    cardN = str(card)
    if(len(cardN) == 16):
        checkN = cardN[-1]
        calcN = cardN[:-1]
        for num in range(0,len(calcN),2):
            newNum = int(calcN[num])*2
            if(newNum >= 10):
                newNumStr = str(newNum);
                finalNum = sum(int(digit) for digit in newNumStr)
            else:
                finalNum = newNum
            finalTot += finalNum  
        for num2 in range(1,len(calcN),2):
            finalTot += int(calcN[num2])

        totLast = str(finalTot)
        calcT = 10 - int(totLast[-1])
        if(calcT == int(checkN)):
            print("Valid Card")
        else:
            print("Wrong Card Number")         
    else:
        print("wrong card number")


#run script with card number
validator(5555555555555555)
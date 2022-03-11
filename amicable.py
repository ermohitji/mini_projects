#this is the program for amicable pair.
# A pair of numbers (a,b) is called to be amicable pair if the sum of the factors of 'a' is equal to 'b'.
# and sum of factors of 'b' is equal to 'a'


def amicablePair(num1, num2):
    x = 1
    temp1 = 0
    while (x < num1):
        if (num1 % x == 0):
            temp1 += x
        x += 1
    y = 1
    temp2 = 0
    while (y < num2):
        if (num2 % y == 0):
            temp2 += y
        y += 1

    if (temp1 == num2 and temp2 == num1):
        return True
    return False


num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))
amicable = amicablePair(num1,num2)
print(f"Pair of both values is amicable: {amicable}")

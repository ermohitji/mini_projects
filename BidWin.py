# the program is for getting the winner of bid
# this program display the name and amount of the applicant who are ready to give maximum amount
BidFile = dict()
while True:
    BidFile[input("Enter the name: ")] = int(input("Enter the amount: "))
    Next = input("for next application press enter else type 'stop ') ")
    if Next =="stop":
        break
max = 0
for applicant in BidFile:
    if BidFile[applicant]>max:
        max = BidFile[applicant]
        win = applicant
print(f"Winner of the bid is {win} at the amount of {max}")

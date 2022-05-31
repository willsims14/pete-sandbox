"""
    Developer: Pete Coutros
    Course: CMIS 102

    Description:
        This program will calculate the weekly pay for a paper carrier
        The user will input the number of paper on the route,
        the number of days the paper is delivered per week,
        and the amount of tips received for the week

        The calculations will be done with a "hard-coded" newspaper cost of $1,
        and a commission rate of 25%
"""


def main():
    """ <String describing the main() function here> """

    #Initialize Variables (newpaperCost = $1, commissionRate = 25%)
    NEWSPAPER_COST = 1.00
    COMMISSION_RATE = 0.25

    # Prompt user for name
    name = input("Hello, what is your name?\t")

    #Display welcome message
    print("\nHello " + name + ", this program will assist you in calculating your weekly pay as a paper carrier.")
    print("To get started we will first need some information from you:")

    #Prompt user for number of papers on route
    numPapersOnRoute = int(input("\nHow many papers do you delivere on your route?\t"))
    #Prompt user for number of days paper is delivered per week
    numDaysPerWeek = int(input("How many days a week do you deliver papers?\t"))
    #Prompt user for amount of tips received z week
    numTipsPerWeek = int(input("How much did you receive in tips this week?\t"))

    totalPapersPerWeek = numPapersOnRoute * numDaysPerWeek
    weeklySalary = totalPapersPerWeek * NEWSPAPER_COST * COMMISSION_RATE
    totalPay = weeklySalary + numTipsPerWeek

    #Display the results
    print("\nThe total number of papers you delivered for the week was " + str(totalPapersPerWeek) + " papers.")
    print("Using a predetermined newspaper cost of $1 and a commission rate of 25%, your weekly salary is $" + str(weeklySalary))
    print("The total amount you collected in tips was $" + str(numTipsPerWeek))
    print("Therefore making your total pay for the week $" + str(totalPay))
    print("\nThank you " + name + ", enjoy the rest of your day!")


if __name__ == "__main__":
    main()

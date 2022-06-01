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

    NEWSPAPER_COST = 1.00
    COMMISSION_RATE = 0.25

    # Prompt user for name
    name = input("Hello, what is your name?\t")

    # Display welcome message
    print(f"Hello {name}, this program will assist you in calculating your"
           "weekly pay as a paper carrier.\nTo get started we will first need"
           "some information from you:")

    # Prompt user for number of papers on route
    try:
        num_papers_on_route = int(input("\nHow many papers do you deliver on your route?\t"))
    except ValueError as e:
        print("\n     ! Please provide an integer !")
        num_papers_on_route = int(input("\nHow many papers do you deliver on your route?\t"))

    # Prompt user for number of days paper is delivered per week
    num_days_per_week = int(input("How many days a week do you deliver papers?\t"))
    # Prompt user for amount of tips received z week
    num_tips_per_week = int(input("How much did you receive in tips this week?\t"))

    total_papers_per_week = num_papers_on_route * num_days_per_week
    weekly_salary = total_papers_per_week * NEWSPAPER_COST * COMMISSION_RATE
    total_pay = weekly_salary + num_tips_per_week

    # Display the results
    print(f"\nThe total number of papers you delivered for the week was {str(total_papers_per_week)} papers.")
    print(f"Using a predetermined newspaper cost of $1 and a commission rate of 25%, your weekly salary is ${str(weekly_salary)}")
    print(f"The total amount you collected in tips was ${str(num_tips_per_week)}")
    print(f"Therefore making your total pay for the week ${str(total_pay)}")
    print(f"\nThank you {name}, enjoy the rest of your day!")


if __name__ == "__main__":
    main()

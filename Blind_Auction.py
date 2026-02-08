
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

user_details = {}
any_person = True
while any_person:

    print(logo)
    print("Welcome to the Blind Auction")

    user_name = input("Please enter your name: ")
    user_bid = int(input("Please enter your bid: $"))

    user_details[user_name] = user_bid

    continue_bid = input("Are there any Bidders? Type 'yes' or 'no':\n").lower()

    if continue_bid == "yes":
        print("\n" * 90)
    elif continue_bid == "no":
        any_person = False

max_amnt = 0
winner = ""

for bidder in user_details:
    bidder_amnt = user_details[bidder]

    if bidder_amnt > max_amnt:
        max_amnt = bidder_amnt
        winner = bidder

print(f"The Winner is {winner} with the Amount of ${max_amnt}")


# winner_name = max(user_details, key = user_details.get)
#
# print(f"The Winner is {winner_name} with the amount of ${max(user_details.values())}")

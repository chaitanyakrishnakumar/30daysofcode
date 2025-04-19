bids = {}

def auction():
    name = input("What is your name?: ")
    bid = int(input("What's your bid in coins?: "))
    bids[name] = bid

print("welcome to the Auction for Rama's Heirloom Ring")

auction()

more_guys = True

while more_guys:
    q = input("Are there any other bidders? Type 'yes or 'no': ").lower()
    if q == "yes":
        print("\n" * 100)
        auction()
    elif q == "no":
        more_guys = False
        highest_bid = 0
        for key in bids:
            if bids[key] > highest_bid:
                highest_bid = bids[key]

        for key in bids:
            if bids[key] == highest_bid:
                winner = key
                print(f"The winner is {winner} with a bid of {highest_bid} coins")

from art import logo


def highest_bidder(record) :
    max_bid = 0
    max_key = ""
    for key in record :
        if record[key] > max_bid :
            max_bid = record[key]
            max_key = key
        print(f"The Winner of the Auction is {max_key}, by the Bid of ${max_bid}")


print(logo)

bidders = {}
over = False

while not over :
    name = input("Name of the Bidder :- ")
    amount = int(input("Enter amount to bid :- "))
    bidders[name] = amount
    choice = input("Are there more bidders,Enter Yes or No :- ").lower()
    if choice == "no" :
        over = True
        highest_bidder(bidders)

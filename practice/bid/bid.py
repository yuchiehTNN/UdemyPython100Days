from art import logo

print(logo)

bid = {}

bidding_finished = False


def find_highest(bid_dict):
    highest_bid = 0
    winner = ""
    for item in bid_dict:
        if highest_bid < bid_dict[item]:
            highest_bid = bid_dict[item]
            winner = item
    print(f"The winner is ${winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("Bidder's name: ")
    price = int(input("Bidder's bid price: "))
    bid[name] = price
    stop_bidding = input("Stop bidding? ")
    if stop_bidding == "yes":
        bidding_finished = True
find_highest(bid)

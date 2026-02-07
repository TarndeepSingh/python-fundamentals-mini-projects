"""
Project: Silent Auction
Description: A command-line program that collects bids from multiple users
and determines the highest bidder.
"""

from art import logo

print(logo)


def find_highest_bidder(bidding_record):
    """
    Determines and prints the highest bidder from the bidding record.

    Args:
        bidding_record (dict): Dictionary containing bidder names and bid amounts
    """
    highest_bid = 0
    winner = ""

    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\n🏆 The winner is {winner} with a bid of ${highest_bid}")


# Store bids
bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ").strip()

    try:
        price = int(input("What is your bid?: $"))
    except ValueError:
        print("❌ Bid must be a number. Try again.")
        continue

    bids[name] = price

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no':\n"
    ).lower().strip()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 30)  # clear screen effect
    else:
        print("❌ Invalid input. Please type 'yes' or 'no'.")


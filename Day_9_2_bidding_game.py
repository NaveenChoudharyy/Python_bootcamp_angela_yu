def bidding():
    bids = {}
    bidding_ends = True
    while bidding_ends:

        user = input("Enter your name: \n")
        if not user.isalpha():
            print("Name can only contain alphabetical letters.")
            break
        else:
            user = user


        bid = input("Enter your bid: \n")
        if not bid.isdigit():
            print("Bid can only contain numbers.")
            break
        else:
            bid = int(bid)

        bids[user] = bid

        next_bid = input("Any other user wants to bid? 'y' for yes and any other keyword to no: ")
        if next_bid == "y":
            next_bid = next_bid.lower()
            print("\n"*100)
        else:
            print("With no more bidding, This auction is over.")
            break


    max_list = []
    for i in bids:
        max_list.append(bids[i])


    for i in bids:
        if bids[i] == max(max_list):
            print(f"\nThe winner is {i.capitalize()} who bidded for ${max(max_list)}")

bidding()
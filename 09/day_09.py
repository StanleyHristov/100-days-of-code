user_answer = 'yes'

bidders = dict()

def is_active():
    if user_answer == 'yes':
        return True;
    else:
        return False

while(is_active()):
    user_name = input("What is your name")
    user_bid = input("What is your bid?")
    bidders[user_name] = user_bid

    user_answer = input("Is there any more bidders? , yes , no").lower()
    max = 0
    max_bidder = ''
    for names ,  bids in bidders.items():
        if max< int(bids): 
            max = int(bids)
            max_bidder = names

    
print(f"The winner is {max_bidder} with the bid of {max}")

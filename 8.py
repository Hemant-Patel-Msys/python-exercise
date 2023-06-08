def credit_card_masked(credit_card_number):
    num_of_credit_to_mask = len(credit_card_number)-4
    masked_credit_card = '*' * num_of_credit_to_mask + credit_card_number[-4:]
    return masked_credit_card

credit_card_number = "7432764328769"
print(credit_card_masked(credit_card_number))
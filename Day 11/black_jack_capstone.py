import random


def first_two_card():
    empty_hand = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    first_card = get_a_card(0, empty_hand)
    second_card = get_a_card(first_card[0], first_card[1])
    return tuple(list(second_card) + [first_card[0]])


def compare(player_scores, computer_scores):
    if player_scores > 21:
        if computer_scores > 21:
            return "Draw"
        else:
            return "Lose"
    elif player_scores < 16:
        return "Lose"
    else:
        if computer_scores > 21:
            return "Win"
        else:
            if player_scores > computer_scores:
                return "Win"
            elif player_scores == computer_scores:
                return "Draw"
            else:
                return "Lose"


def draw_player(player_scores, player_cards, computer_first_card):
    # input "y" or "n", return True or False using lambda function
    """ Ask user if they want to draw more or not, return new player_scores and player_cards"""
    print(f"Your current cards {list(player_cards.items())}")
    print(f"Your current scores {player_scores}")
    print(f"Computer's first card {computer_first_card}")
    run = (input("Do you want to draw more? ") == "y")
    while run:
        get_result = get_a_card(player_scores, player_cards)
        player_scores, player_cards = get_result
        if (player_scores > 21) and (player_cards[11] > 0):
            player_scores -= 10
            player_cards[11] -= 1
            player_cards[1] += 1
        print(f"Your current cards {list(player_cards.items())}")
        print(f"Your current scores {player_scores}")
        if player_scores > 21:
            break
        run = (input("Do you want to draw more? ") == "y")

    return player_scores, player_cards


def draw_computer(computer_scores, computer_cards):
    while computer_scores < 15:
        # assign get_a_card function's return to get_result
        get_result = get_a_card(computer_scores, computer_cards)
        # Modify scores, cards to its right value
        computer_scores, computer_cards = get_result
    if (computer_scores > 21) and (computer_cards[11] > 0):
        computer_scores -= 10
        computer_cards[11] -= 1
        computer_cards[1] += 1
        return draw_computer(computer_scores, computer_cards)
    print(f"Computer end cards {list(computer_cards.items())}")
    print(f"Computer end scores {computer_scores}")
    return computer_scores, computer_cards


def get_a_card(now_scores, now_cards):
    """#Use random module to get a card from card list"""
    card_collection = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Get an index number using random module
    card_index = random.randint(0, len(card_collection) - 1)
    # assign "card_value" from the index we just got
    card_value = card_collection[card_index]
    # Now modify result_scores and result_cards to fit what we just draw
    result_scores = now_scores + card_value
    result_cards = now_cards
    result_cards[card_value] = now_cards[card_value] + 1
    return result_scores, result_cards


def main_game():
    first_two_card_result = list(first_two_card())
    player_scores, player_cards = first_two_card_result[0], first_two_card_result[1]
    first_two_card_result = list(first_two_card())
    computer_scores, computer_cards, computer_first_card = first_two_card_result[0], first_two_card_result[1], first_two_card_result[2]

    if player_scores == 21:
        print(compare(player_scores, computer_scores))
        return
    player_scores, player_cards = draw_player(player_scores, player_cards, computer_first_card)
    computer_scores, computer_cards = draw_computer(computer_scores, computer_cards)
    print(f"Your end cards {list(player_cards.items())}")
    print(f"Your end scores {player_scores}")
    print(compare(player_scores, computer_scores))
# print(draw_computer(11, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 1}))
# draw_player(11, {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 0})

main_game()
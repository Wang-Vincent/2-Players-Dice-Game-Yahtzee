"""
Yahtzee
"""


import re
from textwrap import fill
from random import randint
import doctest


def FIRST_YAHTZEE_VALUE():
    """first Yahtzee value"""
    return 50


def BONUS_YAHTZEE_VALUE():
    """bonus Yahtzee value"""
    return 100


def FULL_HOUSE_VALUE():
    """full house value"""
    return 25


def SMALL_STRAIGHT_VALUE():
    """small straight value"""
    return 30


def LARGE_STRAIGHT_VALUE():
    """large straight value"""
    return 40


def NO_MATCH_VALUE():
    """large straight value"""
    return 0


def UPPER_SECTION_BONUS():
    """upper section bonus"""
    return 35


def UPPER_BONUS_REQUIREMENT():
    """upper section bonus min score requirement"""
    return 63


def NUMBER_OF_REC_CHOICE():
    """number of box to record choices"""
    return 13


def UPPER_START():
    """upper section start number"""
    return 1


def UPPER_STOP():
    """upper section stop number"""
    return 6


def LOWER_START():
    """lower section start number"""
    return 7


def LOWER_STOP():
    """lower section stop number"""
    return 13


def CUBE_DICE_MAX_VALUE():
    """die max value"""
    return 6


def CUBE_DICE_MIN_VALUE():
    """die min value"""
    return 1


def EMPTY_BOX():
    """empty box"""
    return -1


def SCORE_SHEET_LENGTH():
    """score sheet length (name+13)"""
    return 14


def UNSORTED_DICE_LENGTH():
    """dice in hand + dice on table = 2"""
    return 2


def COUNTER_TOTAL():
    """max chances to roll"""
    return 3


def TOTAL_NUMBER_OF_DICE():
    """number of dice"""
    return 5


def REC_ACES():
    """player choice to record in box 1"""
    return 1


def REC_2s():
    """player choice to record in box 2"""
    return 2


def REC_3s():
    """player choice to record in box 3"""
    return 3


def REC_4s():
    """player choice to record in box 4"""
    return 4


def REC_5s():
    """player choice to record in box 5"""
    return 5


def REC_6s():
    """player choice to record in box 6"""
    return 6


def REC_THREE_OF_A_KIND():
    """player choice to record in box 7"""
    return 7


def REC_FOUR_OF_A_KIND():
    """player choice to record in box 8"""
    return 8


def REC_FULL_HOUSE():
    """player choice to record in box 9"""
    return 9


def REC_S_STRAIGHT():
    """player choice to record in box 10"""
    return 10


def REC_L_STRAIGHT():
    """player choice to record in box 11"""
    return 11


def REC_YAHTZEE():
    """player choice to record in box 12"""
    return 12


def REC_CHANCE():
    """player choice to record in box 13"""
    return 13


def TXT_WIDTH():
    """textwrap width"""
    return 100


def game():
    """
    this function act as a wrapper for all yahtzee component functions.

    it will use a while not to check if there is still unfilled cells in the score sheet of either player. if there is,
    the game will continue. Otherwise it will calculate the total score for both player and decide a winner. also,
    before each player's turn start, if that player's score sheet is fulled, their turn will be skipped

    :precondition: no precondition, can always run
    :postcondition: no post condition
    :return: none
    """
    print(fill('Greeting players! For your convenience, the system will automatically roll for you if no prior '
               'decisions is required. Let the Game begins!', TXT_WIDTH()))
    player1_name = 'player1'
    player2_name = 'player2'
    score_sheet1 = create_score_sheet(player1_name)
    score_sheet2 = create_score_sheet(player2_name)
    while not endgame(score_sheet1, score_sheet2):
        if EMPTY_BOX() in score_sheet1:
            print('\nPlayer1, your turn has begun!\n')
            turn_manager(score_sheet1)
        else:
            print('\nPlayer1, your score_sheet is fulled! The system will skip your turn now!\n')

        if EMPTY_BOX() in score_sheet2:
            print('\nPlayer2, your turn has begun!\n')
            turn_manager(score_sheet2)
        else:
            print('\nPlayer2, your score_sheet is fulled! The system will skip your turn now!\n')
    game_summary(score_sheet1, score_sheet2)


def create_score_sheet(player_name):
    """
    generate and return a list to represent the score sheet for player with their name as the first item.

    :param player_name: a string
    :precondition: no precondition, the function can always execute.
    :postcondition: return a list to represent the score sheet for player.
    :return: a list to represent the score sheet for player. (score_sheet)

    >>> pn = 'player1'
    >>> print(create_score_sheet(pn))
    ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    """
    score_sheet = [player_name, EMPTY_BOX(), EMPTY_BOX(), EMPTY_BOX(), EMPTY_BOX(), EMPTY_BOX(),
                   EMPTY_BOX(), EMPTY_BOX(), EMPTY_BOX(), EMPTY_BOX(), EMPTY_BOX(), EMPTY_BOX(),
                   EMPTY_BOX(), EMPTY_BOX()]
    return score_sheet


def endgame(score_sheet1, score_sheet2):
    """
    this function returns a boolean to decide if the game continue or over base on if every cell of both score sheet is
    filled.

    this function will check the score sheet each time players had finished their turn.

    :param score_sheet1: a list
    :param score_sheet2: a list
    :precondition: parameter must be 2 lists
    :postcondition: return a boolean representing if every score cell is filled for each player.
    :return: a boolean representing if every score cell is filled for each player.

    >>> ss1 = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
    >>> ss2 = ['player2', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
    >>> endgame(ss1, ss2)
    True

    >>> ss1 = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
    >>> ss2 = ['player2', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, -1, 13]
    >>> endgame(ss1, ss2)
    False
    """
    if EMPTY_BOX() not in score_sheet1 and EMPTY_BOX() not in score_sheet2:
        return True
    else:
        return False


def turn_manager(score_sheet):
    """
    This function represents the turn of each player.

    Firstly, fresh new dice is created. each player can roll no more than 3 times. They can choose to end their turn
    and record before they used all their rolls. Use a while loop to control a counter, Each they roll the counter
    increase. when it reach the limit, the while loop end and invoke player_turn_end. it functioned the same as
    turn_manager2 but just take param from different address to represent a separate score sheet.

    :param score_sheet: a list
    :precondition: parameter must be a list of 13 negative one (to represent empty) or integer.
    :postcondition: no post condition. this is a manager function.
    :return: none
    """
    counter = 0
    dice = new_dice()
    rolled_dice = roll(dice)
    while counter < COUNTER_TOTAL():
        returned_list = player_action(rolled_dice, score_sheet, counter)
        if len(returned_list) == SCORE_SHEET_LENGTH():  # score sheet
            updated_score_sheet = returned_list
            return updated_score_sheet
        if len(returned_list) == UNSORTED_DICE_LENGTH():  # dice
            rolled_dice = roll(returned_list)
            counter += 1

    updated_score_sheet = player_turn_end(rolled_dice, score_sheet)
    return updated_score_sheet


def new_dice():
    """
    generate a nested list (dice) with 5 zeros as placeholder to the second list of a nested list (dice[1]).

    first list in the nested list is reserve for player to hold. it is empty now because it represents all dice is on
    table at the beginning of the turn.

    :precondition: no precondition, can always run
    :postcondition: return a nested list with a empty dice[0] and a dice[1] with 5 zeros
    :return: dice: a nested list with a empty 1st list and a 2nd list of 5 zeros.
    """
    dice = [[], [0, 0, 0, 0, 0]]
    return dice


def roll(dice):
    """
    take the dice as param, roll all the dice that are not hold by player.

    for each integers in the second list of the nested list, generate same amount of randint(1, 6) and append them to
    a new list. remove the second list, append the new list into the nested list. return the updated dice.
    :param dice: a nested list
    :precondition: dice must be a nested list of 2 list and the second list within the nested list must not be empty
    :postcondition: return a nested list with a empty 1st list and a 5 random integer 2nd list
    :return: dice: a nested list
    """
    rolled_dice = []
    for die in dice[1]:
        rolled_dice.append(randint(1, CUBE_DICE_MAX_VALUE()))
    dice[1] = rolled_dice
    return dice


def player_action(dice, score_sheet, counter):
    """
    First print a message to remind player how many rolls left. Secondly print score_sheet and sorted dice result for
    player's reference. prompt player to input a number representing their decision: 1.select any number between
    0-4 of dice to hold, and then keep rolling the dice that the not chosen. 2. stop and record score.

    if player_decision is 1 invoke pick_dice(sorted_dice), otherwise invoke record_score(dice, score_sheet)

    :param dice: a nested list
    :param score_sheet: a list
    :param counter : a integer
    :precondition: dice must be a nested list, score sheet must be a list and counter must be a integer between 1-3
    :postcondition: return an updated nested list if player choose to hold some dice after pick_dice() is invoked
    :return: dice, an updated nested list if player choose to hold some dice after pick_dice() is invoked
    """
    total_score = calculate_total(score_sheet)
    print_sheet(score_sheet, total_score)
    sorted_dice = sort_dice(dice)
    print(f'\nYour sorted dice result is: {sorted_dice}')
    print(f'You have {COUNTER_TOTAL() - counter} rolls left! Here is your score sheet for your reference.')
    while True:
        player_decision = input('1. select any number between 0-4 of dice to hold, and then keep rolling the dice '
                                'that the not chosen.\n2. stop and record score.\nPlease decide your next move'
                                ' by entering 1 or 2: ')
        if player_decision == '1':
            return pick_dice(sorted_dice)
        if player_decision == '2':
            return record_score(sorted_dice, score_sheet)
        else:
            print("Invalid input. please re-enter.")


def player_turn_end(dice, score_sheet):
    """
    notify the player that they used all their rolls and they must record down a score now. Sort the dice,
    print the score sheet and the sorted dice result for player's reference. and then invoke record_score(sorted_dice,
    score_sheet)

    :param dice: a nested list
    :param score_sheet: a list
    :precondition: dice must be a nested list and score sheet must be a list
    :postcondition: no post condition
    :return: none
    """
    total_score = calculate_total(score_sheet)
    print_sheet(score_sheet, total_score)
    print(fill('You have used all your rolls! You must record down a score now. Here is your score sheet and dice '
               'result for your reference.', TXT_WIDTH()))
    sorted_dice = sort_dice(dice)
    print(f'\nYour sorted dice result is: {sorted_dice}')
    updated_score_sheet = record_score(sorted_dice, score_sheet)
    return updated_score_sheet


def pick_dice(sorted_dice):
    """
    Before player start picking dice to hold, print a sorted dice result. Prompt player to pick dice to hold, create
    new nested list "dice" to represent dice in hand and dice on table and finally invoke print_dice for player's
    reference after player finish their picks.

    This action represents appending the dice that player wants to hold from the sorted dice result to hand. If player
    enter "12", that mean appending two dice on the left side from the sorted_dice to the dice[0]. For each dice not in
    hand, system will then generate a placeholder "0" to represent the dice on table and append them to the dice[1].
    player can hold 4 dice at most. if the player entered anything other than 1-4 unique numbers in the range of 1-5,
    the system will treat it as if player choose not to hold any dice.

    :param sorted_dice: a list
    :precondition: sorted_dice must be a sorted list, with the length of 5 numbers in the range of 1-6(represent 5 dice)
    :postcondition: return an updated nested list
    :return: dice, a nested list of two lists
    """
    print(f'\nYour sorted dice result is: {sorted_dice}')
    player_picks = input(fill('Here is your sorted dice result. Please enter 1-4 unique numbers in the range of 1-5 to'
                              ' represent the selection of dice you want to hold. the numbers represents the location '
                              'of die in the dice list from left to right. For example if you want to hold 2 dice that '
                              'are on the left of the sorted dice list, you will enter "12". Warning: if you enter '
                              'anything else, the system will treat it as if you choose not to hold any dice: ',
                              TXT_WIDTH()))
    dice = [[], []]
    if re.match(r'^(?!.*(.).*\1)[1-5]{1,4}$', player_picks):
        picks_list = [int(pick) for pick in player_picks]
        index_list = [pick - 1 for pick in picks_list]
        for index in index_list:
            dice[0].append(sorted_dice[index])
        for die in range(TOTAL_NUMBER_OF_DICE() - len(dice[0])):
            dice[1].append(0)
    else:
        for die in sorted_dice:
            dice[1].append(0)
    return dice


def calculate_total(score_sheet):
    """
    if the score_sheet is fully recorded, calculate and return the total score.

    :param score_sheet: a list
    :precondition: score sheet must be a list
    :postcondition: a integer total_score will be calculated and returned
    :return: total_score, a integer
    >>> ss = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
    >>> calculate_total(ss)
    93
    """
    total_score = EMPTY_BOX()
    if EMPTY_BOX() not in score_sheet:
        if sum(score_sheet[slice(UPPER_START(), UPPER_STOP()+1)]) >= UPPER_BONUS_REQUIREMENT():
            total_score = sum(score_sheet[slice(UPPER_START(), LOWER_STOP()+1)]) + UPPER_SECTION_BONUS()
        elif sum(score_sheet[slice(UPPER_START(), UPPER_STOP()+1)]) < UPPER_BONUS_REQUIREMENT():
            total_score = sum(score_sheet[slice(UPPER_START(), LOWER_STOP()+1)])
    else:
        total_score = EMPTY_BOX()

    return total_score


def record_score(sorted_dice, score_sheet):
    """
    Print the score sheet first with print_sheet(), prompt player to choose an empty cell to record their score.

    The function will then first check if the cell is empty, the system will calculate the score by invoking
    score_calculator base on the corresponding cell and fill in. If player choose to record in the Yahtzee cell,
    yahtzee_score_cal will invoke to calculate yahtzee scores. If either helper function is invoked, they will return
    a score for the system to fill into the cell of player's choice. If neither condition is met, that means player has
     tried an invalid move. that is not allowed and player must re-enter a valid number for the score sheet to be
      properly recorded.


    :param sorted_dice: a nested list
    :param score_sheet: a list
    :precondition: dice must be a nested list and score sheet must be a list with the length of 14
    :postcondition: corresponding cell of players choice will be filled
    :return: score_sheet, a list
    """
    str_d = "".join(map(str, sorted_dice))
    while True:
        player_choice = input(fill("Your score sheet and dice result are printed above for reference. please enter"
                                   " a valid number representing the choice of the cell you want to fill:",
                                   TXT_WIDTH()))

        if player_choice.isnumeric() and int(player_choice) in range(1, NUMBER_OF_REC_CHOICE()+1):
            if score_sheet[int(player_choice)] == EMPTY_BOX():
                score = calculate_score(sorted_dice, int(player_choice))
                score_sheet[int(player_choice)] = score
                return score_sheet
            elif re.search(r'([1-6])\1{4}', str_d) and score_sheet[REC_YAHTZEE()] >= FIRST_YAHTZEE_VALUE():
                score_sheet[int(player_choice)] += BONUS_YAHTZEE_VALUE()
                return score_sheet
            else:
                print("Invalid input. Please Re-enter.")

        else:
            print("Invalid input. Please Re-enter.")


def print_sheet(score_sheet, total_score):
    """
    This function will print the score sheet, including bonus, upper and lower section sum and total scores.

    bonus, upper and lower section sum and total scores will only be displayed if all of their required cells are filled

    :param score_sheet: a list
    :param total_score: a integer
    :precondition: score sheet must be a list
    :postcondition: a formatted print out of the list will be displayed
    :return: none

    >>> ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    >>> ts = -1
    >>> print_sheet(ss, ts)
    -------------------------
    Yahtzee Score Sheet
    -------------------------
    Player:player1
    1. Aces:
    2. 2s:
    3. 3s:
    4. 4s:
    5. 5s:
    6. 6s:
    7. 3 of a kind:
    8. 4 of a kind:
    9. Full House:
    10. Small Straight:
    11. Large Straight:
    12. Yahtzee:
    13. Chance:
    Sum of Upper Section:
    Bonus:
    Sum of Lower Section:
    Total Score:
    -------------------------

    >>> ss = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, -1, 0, 0, 50, 13]
    >>> ts = -1
    >>> print_sheet(ss, ts)
    -------------------------
    Yahtzee Score Sheet
    -------------------------
    Player:player1
    1. Aces:3
    2. 2s:6
    3. 3s:6
    4. 4s:4
    5. 5s:5
    6. 6s:6
    7. 3 of a kind:0
    8. 4 of a kind:0
    9. Full House:
    10. Small Straight:0
    11. Large Straight:0
    12. Yahtzee:50
    13. Chance:13
    Sum of Upper Section:30
    Bonus:0
    Sum of Lower Section:
    Total Score:
    -------------------------

    >>> ss = ['player1', 3, 6, 6, 4, -1, 6, 0, 0, -1, 0, 0, 50, 13]
    >>> ts = -1
    >>> print_sheet(ss, ts)
    -------------------------
    Yahtzee Score Sheet
    -------------------------
    Player:player1
    1. Aces:3
    2. 2s:6
    3. 3s:6
    4. 4s:4
    5. 5s:
    6. 6s:6
    7. 3 of a kind:0
    8. 4 of a kind:0
    9. Full House:
    10. Small Straight:0
    11. Large Straight:0
    12. Yahtzee:50
    13. Chance:13
    Sum of Upper Section:
    Bonus:
    Sum of Lower Section:
    Total Score:
    -------------------------

    >>> ss = ['player1', -1, -1, -1, -1, -1, -1, 0, 0, 25, 30, 40, 50, 18]
    >>> ts = -1
    >>> print_sheet(ss, ts)
    -------------------------
    Yahtzee Score Sheet
    -------------------------
    Player:player1
    1. Aces:
    2. 2s:
    3. 3s:
    4. 4s:
    5. 5s:
    6. 6s:
    7. 3 of a kind:0
    8. 4 of a kind:0
    9. Full House:25
    10. Small Straight:30
    11. Large Straight:40
    12. Yahtzee:50
    13. Chance:18
    Sum of Upper Section:
    Bonus:
    Sum of Lower Section:163
    Total Score:
    -------------------------

    >>> ss = ['player1', 6, 12, 18, 24, 20, 30, 0, 0, 25, 30, 40, 50, 20]
    >>> ts = 310
    >>> print_sheet(ss, ts)
    -------------------------
    Yahtzee Score Sheet
    -------------------------
    Player:player1
    1. Aces:6
    2. 2s:12
    3. 3s:18
    4. 4s:24
    5. 5s:20
    6. 6s:30
    7. 3 of a kind:0
    8. 4 of a kind:0
    9. Full House:25
    10. Small Straight:30
    11. Large Straight:40
    12. Yahtzee:50
    13. Chance:20
    Sum of Upper Section:110
    Bonus:35
    Sum of Lower Section:165
    Total Score:310
    -------------------------
    """
    print('-------------------------\nYahtzee Score Sheet\n-------------------------')
    name_list = ['Player', '1. Aces', '2. 2s', '3. 3s', '4. 4s', '5. 5s', '6. 6s', '7. 3 of a kind', '8. 4 of '
                 'a kind', '9. Full House', '10. Small Straight', '11. Large Straight', '12. Yahtzee', '13. Chance']
    temp_list = ["" if score == EMPTY_BOX() else score for score in score_sheet]
    for i in range(len(score_sheet)):
        print(f'{name_list[i]}:{temp_list[i]}')
    if EMPTY_BOX() not in score_sheet[slice(UPPER_START(), UPPER_STOP()+1)]:
        if sum(score_sheet[slice(UPPER_START(), UPPER_STOP()+1)]) >= UPPER_BONUS_REQUIREMENT():
            print(f'Sum of Upper Section:{sum(score_sheet[slice(UPPER_START(), UPPER_STOP()+1)])}\nBonus:35')
        elif sum(score_sheet[slice(UPPER_START(), UPPER_STOP()+1)]) < UPPER_BONUS_REQUIREMENT():
            print(f'Sum of Upper Section:{sum(score_sheet[slice(UPPER_START(), UPPER_STOP()+1)])}\nBonus:0')
    else:
        print('Sum of Upper Section:\nBonus:')
    if EMPTY_BOX() not in score_sheet[slice(LOWER_START(), LOWER_STOP()+1)]:
        print(f'Sum of Lower Section:{sum(score_sheet[slice(LOWER_START(), LOWER_STOP()+1+1)])}')
    else:
        print('Sum of Lower Section:')
    if EMPTY_BOX() not in score_sheet:
        print(f'Total Score:{total_score}\n-------------------------')
    else:
        print(f'Total Score:\n-------------------------')


def sort_dice(dice):
    """
    convert the dice (nested list) into 1 single list and sort.

    so it can be easier to process in score_calculator().

    :param dice: a nested list
    :precondition: dice must be a nested list of 2 list
    :postcondition: combine them into 1 single list, sort and return
    :return: sorted_dice, a list representing the dice

    >>> d = [[], [5, 2, 3, 4, 2]]
    >>> print(sort_dice(d))
    [2, 2, 3, 4, 5]

    >>> d = [[6, 6], [3, 4, 2]]
    >>> print(sort_dice(d))
    [2, 3, 4, 6, 6]
    """
    dice = dice[0] + dice[1]
    sorted_dice = sorted(dice)
    return sorted_dice


def calculate_score(sorted_dice, choice):
    """
    check if the dice pass condition and/or regex match/search the pattern, return corresponding scores.

    for each type of player choice (1-6: count and add, 7-8: match pattern and add, 9-11 match pattern and fixed scores,
    13 add)
    :param sorted_dice: a nested list
    :param choice: an integer between 1-13
    :precondition: dice must be a nested list of 2 list and player_choice must be an integer between 1-13
    :postcondition: return a calculated score
    :return: score, an integer between 0-50

    >>> sd = [2, 3, 4, 6, 6]
    >>> pc = 6
    >>> calculate_score(sd, pc)
    12

    >>> sd = [2, 3, 3, 4, 5]
    >>> pc = 10
    >>> calculate_score(sd, pc)
    30

    >>> sd = [1, 2, 3, 4, 5]
    >>> pc = 11
    >>> calculate_score(sd, pc)
    40
    """
    score = NO_MATCH_VALUE()
    str_d = "".join(map(str, sorted_dice))
    if choice in range(1, 6+1):
        score = sorted_dice.count(choice) * choice
    elif choice == REC_THREE_OF_A_KIND() and re.search(r'([\d])\1{2}', str_d):
        score = sum(sorted_dice)
    elif choice == REC_FOUR_OF_A_KIND() and re.search(r'([\d])\1{3}', str_d):
        score = sum(sorted_dice)
    elif choice == REC_FULL_HOUSE():
        if re.search(r'([\d])\1{2}([\d])\2', str_d) or re.search(r'([\d])\1([\d])\2{2}', str_d):
            score = FULL_HOUSE_VALUE()
    elif choice == REC_S_STRAIGHT() and re.search(r'(1234|2345|3456|12234|23345|34456|12334|23445|34556)', str_d):
        score = SMALL_STRAIGHT_VALUE()
    elif choice == REC_L_STRAIGHT() and re.match(r'(12345|23456)', str_d):
        score = LARGE_STRAIGHT_VALUE()
    elif choice == REC_YAHTZEE() and re.search(r'([\d])\1{4}', str_d):
        score = FIRST_YAHTZEE_VALUE()
    elif choice == REC_CHANCE():
        score = sum(sorted_dice)
    return score


def game_summary(score_sheet1, score_sheet2):
    """
    summarize the game when it ends. compare the total score of both score sheets, the one with higher score win.

    print the result with f string and control the winner declaration with if statement.

    :param score_sheet1: a list
    :param score_sheet2: a list
    :precondition: both list must not contain negative one (to represent empty).
    :postcondition: no postcondition
    :return: none
    >>> ss1 = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
    >>> ss2 = ['player2', 4, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
    >>> game_summary(ss1, ss2)
    --------------------------------------------------
    Game over! player1 has the total score of 93, player2 has the total score of 94, player2 win!
    """
    total_score1 = calculate_total(score_sheet1)
    total_score2 = calculate_total(score_sheet2)
    print(f'--------------------------------------------------\nGame over! {score_sheet1[0]} has the total score of '
          f'{total_score1}, {score_sheet2[0]} has the total score of {total_score2}, ', end='')
    if total_score1 > total_score2:
        print('player1 win!')
    elif total_score2 > total_score1:
        print('player2 win!')
    elif total_score2 == total_score1:
        print("It's a draw!")


def main():
    game()
    doctest.testmod()


if __name__ == '__main__':
    main()
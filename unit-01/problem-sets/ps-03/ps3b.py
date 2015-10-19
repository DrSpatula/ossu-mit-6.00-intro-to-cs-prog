from ps3a import *
import time
from perm import *


def find_words(aggregator, hand, wordlen, word_set):
    """
    Recursively accumulates set of valid words made from the given hand

    aggregator: list (should be empty list in manual call)
    hand: dictionary (string -> int)
    wordlen: int (should be number of letters in hand to start)
    word_set: set of valid words
    """
    if wordlen == 0:
        return aggregator

    else:
        new_words = set(get_perms(hand, wordlen))
        return aggregator + list(word_set & new_words) + \
            find_words(aggregator, hand, wordlen - 1, word_set)

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    words = find_words([], hand, calculate_handlen(hand), set(word_list))

    if len(words) > 0:
        return words[0]

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    total_score = 0
    while calculate_handlen(hand) > 0:
        print
        print 'Current hand: {}'.format(get_displayable_hand(hand))
        word = comp_choose_word(hand, word_list)

        if word == None:
            print 'Computer could not find a word.'
            break
        else:
            print 'Computer plays: {}'.format(word)
            word_score = get_word_score(word, calculate_handlen(hand))
            total_score += word_score
            print '"{0}" scored {1:d} points. Total: {2:d} points'.format(
                word, word_score, total_score)
            hand = update_hand(hand, word)

    print
    print 'Total score: {0:d} points.'.format(total_score)

#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    hand = {}

    while True:
        user_action = ''
        print
        print
        print 'Main Menu:'
        print '----------'
        print 'n - deals a new, random hand'

        if calculate_handlen(hand) > 0:
            print 'r - replays the previous hand'

        print 'e - exits'
        print
        user_action = raw_input("Your choice: ")

        if user_action == 'e':
            print "Goodbye!"
            break

        if user_action == 'n':
            hand = deal_hand(HAND_SIZE)

        if user_action == 'r' or user_action == 'n':
            player_choice = ''
            while player_choice not in ('u', 'c'):
                print
                print 'Who plays?'
                print 'u - you'
                print 'c - computer'
                player_choice = raw_input('Your choice: ')

                if player_choice == 'u':
                    play_hand(hand, word_list)

                elif player_choice == 'c':
                    comp_play_hand(hand, word_list)

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)



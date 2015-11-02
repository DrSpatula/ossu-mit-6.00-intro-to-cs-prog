import random


def roll_die():
    """
    returns a random roll of a six-sided die (int)
    """
    return random.choice(range(1, 7))


def roll_dice(num_dice):
    """
    num_dice: the number of six-sided dice to roll
    returns: a list containing num_dice elements of ints in the range 1-6
    """
    result = []
    for i in range(num_dice):
        result.append(roll_die())

    return result


def yahtzee_sim(num_trials):
    """
    rolls 5 six-sided dice num_trials times
    returns: the fraction of yahtzees in num_trials rolls
    """
    yahtzees = 0
    for i in range(num_trials):
        if len(set(roll_dice(5))) == 1:
            yahtzees += 1

    return yahtzees / float(num_trials)


def run_sim(num_times):
    """
    runs the yahtzee simulation num_times times
    returns: mean of the results of each run
    """
    results = []
    for i in range(num_times):
        results.append(yahtzee_sim(100000))

    return sum(results) / float(num_times)

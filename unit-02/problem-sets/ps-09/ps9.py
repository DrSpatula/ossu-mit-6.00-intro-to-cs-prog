# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#
SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#


def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    course_dict = {}

    inputFile = open(filename)
    for line in inputFile:
        name, value, work = line.split(",")
        course_dict[name] = (int(value), int(work))

    return course_dict


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0, 0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = sorted(subjects.keys())
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) + '\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

#
# Problem 2: Subject Selection By Greedy Optimization
#


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return subInfo1[0] > subInfo2[0]


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return subInfo1[1] < subInfo2[1]


def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    ratio1 = subInfo1[0] / float(subInfo1[1])
    ratio2 = subInfo2[0] / float(subInfo2[1])

    return ratio1 > ratio2


def totalWork(subjects):
    """
    Finds the total work required for a subject list

    subjects: dictionary mapping subject name to (value, work)
    returns: integer representing total work required
    """
    if len(subjects.keys()) == 0:
        return 0

    total_work = 0
    for subj in subjects:
        total_work += subjects[subj][1]

    return total_work


def totalValue(subjects):
    """
    Finds the total value of a subject list

    subjects: dictionary mapping subject name to (value, work)
    returns: integer representing total value
    """
    if len(subjects.keys()) == 0:
        return 0

    total_value = 0
    for val in subjects:
        total_value += subjects[val][0]

    return total_value


def sortSubjects(subjects_list, subjects_dict, comparator):
    """
    Sorts subjects using provided comparator function

    subjects_list: list containing strings of subject names
    subjects_dict: dictionary mapping subject names to (value, work) tuples
    comparator: function used to compare two subjects
    returns: sorted list of subject names
    """
    if len(subjects_list) <= 1:
        return subjects_list

    midpoint = len(subjects_list) / 2
    list_a = sortSubjects(subjects_list[:midpoint], subjects_dict, comparator)
    list_b = sortSubjects(subjects_list[midpoint:], subjects_dict, comparator)
    return mergeSubjects(list_a, list_b, subjects_dict, comparator)


def mergeSubjects(
        subj_list_a,
        subj_list_b,
        subjects_dict,
        comparator,
        accumulator=None):
    """
    Merges two lists of subject names into a sorted list
    based on a comparison function

    subj_list_a: list containing strings of subject names
    subj_list_b: list containing strings of subject names
    subjects_dict: dictionary mapping subject names to (value, work) tuples
    comparator: function used to compare two subjects
    accumulator: sorted list combining items from the two input lists
    returns: merged list of subject names, sorted according to comparator
    """

    if accumulator is None:
        accumulator = []

    if len(subj_list_a) == 0:
        return accumulator + subj_list_b

    if len(subj_list_b) == 0:
        return accumulator + subj_list_a

    if comparator(subjects_dict[subj_list_a[0]], subjects_dict[subj_list_b[0]]):
        accumulator.append(subj_list_a[0])
        return mergeSubjects(
            subj_list_a[1:],
            subj_list_b,
            subjects_dict,
            comparator,
            accumulator)

    else:
        accumulator.append(subj_list_b[0])
        return mergeSubjects(
            subj_list_a,
            subj_list_b[1:],
            subjects_dict,
            comparator,
            accumulator)


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    chosen = {}
    sorted_subj = sortSubjects(subjects.keys(), subjects, comparator)

    i = 0
    while totalWork(chosen) < maxWork and i < len(sorted_subj):
        if totalWork(chosen) + subjects[sorted_subj[i]][1] <= maxWork:
            chosen[sorted_subj[i]] = subjects[sorted_subj[i]]

        i += 1

    return chosen

#
# Problem 3: Subject Selection By Brute Force
#


def decimalToBinary(number, number_of_digits):
    """
    Converts the decimal number into a string of length number_of_digits
    representing number in binary

    number: int, the number to convert
    number_of_digits: int, the length of the returned string
    returns: string, representation of number in binary
    """
    binary_string = ''
    while number > 0:
        binary_string = str(number % 2) + binary_string
        number = number // 2

    while len(binary_string) < number_of_digits:
        binary_string = '0' + binary_string

    return binary_string


def generatePowerSet(subjects):
    """
    Generates a list of dicts containing all possible combinations of
    items in subjects

    subjects: dict mapping subject names to (value, work) tuples
    returns: list of dicts
    """
    subj_names = subjects.keys()
    templates = []
    for n in range(2**len(subj_names)):
        templates.append(decimalToBinary(n, len(subj_names)))

    power_set = []
    for t in templates:
        combination = {}
        for i in range(len(t)):
            if t[i] == '1':
                combination[subj_names[i]] = subjects[subj_names[i]]

        power_set.append(combination)

    return power_set


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    combinations = generatePowerSet(subjects)

    best_combo = {}
    for combo in combinations:
        if totalValue(combo) > totalValue(best_combo) and \
                totalWork(combo) <= maxWork:
            best_combo = combo

    return best_combo

# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1


class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link


#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = string.lower(word)

    def is_word_in(self, text):
        words = self._split_text(text)
        return self.word in words

    def _split_text(self, text):
        split_chars = string.punctuation + ' '

        for idx in range(len(text)):
            if text[idx] in split_chars:
                return [string.lower(text[:idx])] + \
                    self._split_text(text[idx + 1:])

        return []


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.title)

    def __str__(self):
        return "TitleTrigger: '{}'".format(self.word)

    __repr__ = __str__


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.subject)

    def __str__(self):
        return "SubjectTrigger: '{}'".format(self.word)

    __repr__ = __str__


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.summary)

    def __str__(self):
        return "SummaryTrigger: '{}'".format(self.word)

    __repr__ = __str__


# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

    def __str__(self):
        return "NotTrigger: NOT '{}'".format(self.trigger)

    __repr__ = __str__


class AndTrigger(Trigger):
    def __init__(self, trigger_a, trigger_b):
        self.trigger_a = trigger_a
        self.trigger_b = trigger_b

    def evaluate(self, story):
        return self.trigger_a.evaluate(story) and self.trigger_b.evaluate(story)

    def __str__(self):
        return "AndTrigger: '{}' AND '{}'".format(
            self.trigger_a, self.trigger_b)

    __repr__ = __str__


class OrTrigger(Trigger):
    def __init__(self, trigger_a, trigger_b):
        self.trigger_a = trigger_a
        self.trigger_b = trigger_b

    def evaluate(self, story):
        return self.trigger_a.evaluate(story) or self.trigger_b.evaluate(story)

    def __str__(self):
        return "OrTrigger: '{}' OR '{}'".format(
            self.trigger_a, self.trigger_b)

    __repr__ = __str__


# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        return self.phrase in story.title \
            or self.phrase in story.subject \
            or self.phrase in story.summary

    def __str__(self):
        return "PhraseTrigger: '{}'".format(self.phrase)

    __repr__ = __str__


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break

    return filtered_stories

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggerlist = []
    triggers = {}

    for line in lines:
        split = string.split(line, ' ')
        if split[0] == "ADD":
            for trigger in split[1:]:
                triggerlist.append(triggers[trigger])

        else:
            if split[1] == "TITLE":
                triggers[split[0]] = TitleTrigger(split[2])

            elif split[1] == "SUBJECT":
                triggers[split[0]] = SubjectTrigger(split[2])

            elif split[1] == "SUMMARY":
                triggers[split[0]] = SummaryTrigger(split[2])

            elif split[1] == "NOT":
                triggers[split[0]] = NotTrigger(triggers[split[2]])

            elif split[1] == "AND":
                triggers[split[0]] = AndTrigger(
                    triggers[split[2]], triggers[split[3]])

            elif split[1] == "OR":
                triggers[split[0]] = OrTrigger(
                    triggers[split[2]], triggers[split[3]])

            elif split[1] == "PHRASE":
                triggers[split[0]] = PhraseTrigger(
                    string.join(split[2:]))

    print triggers
    print triggerlist

    return triggerlist


import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("republican")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]

    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []

    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)

        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)

        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()


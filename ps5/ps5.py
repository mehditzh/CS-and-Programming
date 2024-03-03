# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: <M. Mehdi Taherzadeh>
# Collaborators: < - >
# Time: 09:30

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

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
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):

    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        #implemted lower() method assuming it is not necessary to keep the maing phrase string
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        phrase_words = self.phrase.split(' ')
        text_lower = text.lower()
        for char in string.punctuation:
            while char in text_lower:
                text_lower = text_lower.replace(char, ' ')
        text_words = text_lower.split()

        is_in = False
        if phrase_words[0] in text_words:
            for i in range(1, len(phrase_words)):
                if len(text_words) > text_words.index(phrase_words[0]) + 1:
                    if phrase_words[i] == text_words[text_words.index(phrase_words[0]) + 1]:
                        is_in = True
                    else:
                        is_in = False
                        break

        return is_in



# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())


# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, date):
        date_format = '%d %b %Y %H:%M:%S'
        self.date = datetime.strptime(date, date_format)

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, date):
        TimeTrigger.__init__(self, date)

    def evaluate(self, story):
        pubdate = story.get_pubdate().replace(tzinfo=None)
        return pubdate < self.date
class AfterTrigger(TimeTrigger):
    def __int__(self, date):
        TimeTrigger.__init__(self, date)

    def evaluate(self, story):
        pubdate = story.get_pubdate().replace(tzinfo=None)
        return pubdate > self.date

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2):
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2

    def evaluate(self, story):
        return (self.trigger_1.evaluate(story) and self.trigger_2.evaluate(story))

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2):
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2

    def evaluate(self, story):
        return (self.trigger_1.evaluate(story) or self.trigger_2.evaluate(story))


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break

    return filtered_stories




#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    triggers_mapping = {'TITLE': TitleTrigger, 'DESCRIPTION': DescriptionTrigger,
                     'BEFORE': BeforeTrigger, 'AFTER': AfterTrigger,
                     'AND': AndTrigger, 'OR': OrTrigger, 'NOT': NotTrigger}
    # 't_keyed' is a dictionary keyed on trigger names i.e: t1, t2, t3, ....
    # the values for this dictionary are the triggers with their inputs i.e: TitleTrigger('election')
    t_keyed = {}
    # 'add_list' is a list of trigger names that are supposed to be implemented
    add_list = []
    # 'triggers_list' is a list of triggers with their inputs taken from 't_keyed'
    # which is the desired output for this function
    triggers_list = []

    # create 't_keyed' from the lines and triggers_mapping
    for line in lines:
        # 'trigger_config' is a temoprary list of the elements in each of the lines
        trigger_config = line.split(',')
        if trigger_config[1] in triggers_mapping:
            # normal triggers take one str input
            if trigger_config[1] not in ['OR', ' AND']:
                t_keyed[trigger_config[0]] = (
                    triggers_mapping[trigger_config[1]](trigger_config[2]))
            # if the trigger is a composite it should take two normal triggers as input
            else:
                t_keyed[trigger_config[0]] = (
                    triggers_mapping[trigger_config[1]](t_keyed[trigger_config[2]], t_keyed[trigger_config[3]]))
        # create 'add_list' according to the trigger_config with 'ADD' in the first position
        elif trigger_config[0] == 'ADD':
            for t in trigger_config[1:]:
                add_list.append(t)
    # according to the 'add_list' create the 'triggers_list' looking up to the 't_keyed' dictionary
    for t in add_list:
        triggers_list.append(t_keyed[t])

    return triggers_list




SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        #t1 = TitleTrigger("election")
        #t2 = DescriptionTrigger("Trump")
        #t3 = DescriptionTrigger("Clinton")
        #t4 = OrTrigger(t2, t3)
        #triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()


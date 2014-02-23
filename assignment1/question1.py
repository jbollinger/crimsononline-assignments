import operator
import collections
import re

"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    f = open(filename)
    text = f.read()
    f.close()
    words = re.findall(r"[\w']+", text)
    words_collection = collections.Counter(words)
    return ([word for word, count in words_collection.most_common()])

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    f = open(filename)
    text = f.read()
    f.close()
    words = re.findall(r"[\w']+", text)
    words_collection = collections.Counter(words)
    return ([word for word, count in words_collection.most_common() if len(word) > min_chars])

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    f = open(filename)
    text = f.read()
    f.close()
    words = re.findall(r"[\w']+", text)
    words_collection = collections.Counter(words)
    return ([(word, count) for word, count in words_collection.most_common() if len(word) > min_chars])

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        f = open(filename)
        text = f.read()
        f.close()
        words = re.findall(r"[\w']+", text)
        words_collection = collections.Counter(words)
        return ([(word, count) for word, count in words_collection.most_common() if len(word) > min_chars])
    except IOError:	
        return 'Sorry, the file you wanted cannot be found. Please try another file.'
	   

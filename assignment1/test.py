from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple,
    common_words_safe)
from question2 import (Article, Picture)
from PIL import Image

"""
print "==testing question 1=="
print "common_words... ",
pprint(common_words("words.txt"))

print "common_words_min 2... ",
pprint(common_words_min("words.txt", 2))

print "common_words_min 5... ",
pprint(common_words_min("words.txt", 5))

print "common_words_min 9... ",
pprint(common_words_min("words.txt", 9))

print "common_words_tuple w/ min 5... ",
pprint(common_words_tuple("words.txt", 5))

print "common_words_safe... ",
pprint(common_words_safe("words_fail.txt", 5))
print
"""
print "==testing question 2=="
print "making article... ",
print
a = Article()
a.author = "James"
a.headline = "Testing"
a.content = "AaBaCcDdEe FfGgHhIiJj KkLlMmNnOo..."
a.show()

print "saving to test.txt..."
a.save("test.txt")

print "trying to load from a nonexistent file..."
a.load("fake.txt")

print "trying to load from test.txt..."
a.load("test.txt")

print "trying to load from new.txt..."
a.load("new.txt")
a.show()

print "creating a picture and displaying it..."
p = Picture()
p.creator = "Internet stock photos"
p.title = "Strange stock stock photo"
p.location = "stock.jpg"
p.show()

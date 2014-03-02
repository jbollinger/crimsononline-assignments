from question1 import *
import datetime
from PIL import Image
import re

# testing basic class functions
c = Content('Example', 'This is a test', 'James', 2014, 3, 1)
p = Picture('Example', 'This is a test', 'James', 2014, 3, 1, None)
a = Article('Example', 'This is a test', 'James', 2014, 3, 5, 'fake_image.txt')

c.show()
print
p.show()
print
a.show()
print

# URL functions
print c.matches_url("http://www.thecrimson.com/Content/2014/3/1/This_is_a_test") # True
print p.matches_url("http://www.thecrimson.com/Content/2014/3/1/This_is_a_test") # False
print a.matches_url("http://www.thecrimson.com/Content/2014/3/1/This_is_a_test") # False
print
print from_url([c], "http://www.thecrimson.com/Content/2014/3/1/This_is_a_test") # Prints same output as c.show()
print
print from_url([c], "http://www.thecrimson.com/Article/2014/3/1/This_is_a_test") # Prints "No items match this URL."
print
print from_url([c, c, c], "http://www.thecrimson.com/Content/2014/3/1/This_is_a_test") # Prints "Error: No items match this URL."
print

# posted_after calls .show()
posted_after([c, p, a], datetime.date(2014, 2, 28)) # Shows all three
print
posted_after([c, p, a], datetime.date(2014, 3, 5)) # Shows none of the three
print
posted_after([c, p, a], datetime.date(2014, 3, 2)) # Shows a
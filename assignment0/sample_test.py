# This is a sample file for how your tests should look like.

# To run these tests, make sure you are in the directory that has both your test file (e.g. tests.py) 
# and the files you want to test (question1, question2, etc.) - this is because the from/import 
# statements will look for files in whatever path you are currently in

# Then run "python FILENAME" (e.g. this file is called sample_test.py, so run "python sample_test.py")
# This will run the file, and the file will run the functions and print out the results


from pprint import pprint # pretty print output formatting, you don't have to use this, can just use "print"
from question2 import swapchars # so in the file question2.py, this will look for a function called "swapchars"
from question3 import sortcat # so in the file question3.py, this will look for a function called "sortcat"
from question4a import lookaway # so in the file question4a.py, this will look for a function called "lookaway"

print "==testing question 2=="
print "swapchars... ",
pprint(swapchars("hiiiiii"))
# Prints:"ihhhhhh"
print

print "==testing question 3=="
print "sortcat... ",
pprint(sortcat(3, "wordone", "w3", "word2", "4"))
# Prints:"wordoneword2w3"
pprint(sortcat(2, "dd", "aaaaaaa", "eeee", "bbbbb", "ccc"))
# Prints:"aaaaaaabbbbb"
print

print "==testing question 4=="
print "Will luigi win?... ",
pprint(lookaway(100))
pprint(lookaway(100))
pprint(lookaway(100))
# Prints three proportions (usually between 20 to 30 wins out of 100 games)
print

# Make sure you record in comments what the result is! It should be what you expect, or else you know
# something's wrong with your solution!

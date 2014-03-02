import datetime
from PIL import Image
import re

class Content(object):
    '''
    Required properties:
        - title
        - subtitle
        - creator
        - publication date
    Required methods:
        - show
        - matches_url (question 1d)
    '''
    # the year, month and day that init takes are all ints.
    def __init__(self, title, subtitle, creator, year, month, day):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime.date(year, month, day)

    def show(self):
        print self.title
        print self.subtitle
        print self.creator
        print self.date


    def matches_url(self, url):
        url_fixed = url.replace('http://', '')
        url_fixed = url_fixed.replace('_', ' ')
        url_list = re.split('/', url_fixed)
        if url_list[1] == self.__class__.__name__ and int(url_list[2]) == self.year and int(url_list[3]) == self.month and int(url_list[4]) == self.day and url_list[5] == self.subtitle:
            return True
        else: 
            return False

        
class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''
    def __init__(self, title, subtitle, creator, year, month, day, related_image):
        super(Article, self).__init__(title, subtitle, creator, year, month, day)
        self.related_image = related_image

    def show(self):
        super(Article, self).show()
        if not self.related_image:
            im = Image.open(self.related_image)
            im.show()

class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''

    #image_file is a string of a filename (e.g. "example.txt") or a URL
    def __init__(self, title, subtitle, creator, year, month, day, image_file):
        super(Picture, self).__init__(title, subtitle, creator, year, month, day)
        self.image_file = image_file

    def show(self):
        super(Picture, self).show()
        if self.image_file:
            im = Image.open(self.image_file)
            im.show()

'''
Question 1e
'''
def from_url(c_lst, url):
    correct_c = []
    for c in c_lst:
        if c.matches_url(url):
            correct_c.append(c)
    if len(correct_c) > 1:
        return "Error: multiple items match this URL."
    elif len(correct_c) == 0:
        return "No items match this URL."
    else:
        return correct_c[0].show()



'''
Question 1e
'''
def posted_after(c_lst, dt):
    for c in c_lst:
        if c.date > dt:
            c.show()
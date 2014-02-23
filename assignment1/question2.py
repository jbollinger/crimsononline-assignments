from PIL import image
class Article:
    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''
    def __init__(self):
        self.headline = ""
        self.content = ""
        self.author = ""
        self.related_image = ""
        
    def show(self):
        print self.headline
        print self.author
        print self.content
        im = Image.open(self.related_image)
        im.show()
        
    def save(self, file_name):
        n = open(file_name, 'w')
        n.write(self.headline)
        n.write("\n")
        n.write(self.author)
        n.write("\n")
        n.write(self.content)
        n.write("\n")
        n.write(self.related_image)
        
    def load(self, file_name):
        try:
            f = open(file_name)
            contents_list = []
            text = f.readlines()
            for i in range(len(text)):
                contents_list.append(text[i].strip('\n'))
            f.close()
            self.headline = text[0]
            self.author = text[1]
            self.content = text[2]
            self.related_image = text[3]
            print 'Article loaded.'
        except IOError:	
            print 'Sorry, the file you wanted cannot be found. Please try another file.'

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    def __init__(self):
        self.title = ""
        self.location = ""
        self.creator = ""
    
    def show(self):
        im = Image.open(self.location)
        im.show()
        
        
        
        

class Book(object):

    def __init__(self, title, author, pages):
        print('A book has been created!')
        self.title = title
        self.author = author
        self.pages = pages

    # def __str__(self):
    #     return "Title: %s, Author: %s, Pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Book is gone!')

b = Book('Python', 'Author', 100)
print(b)
print(len(b))
del(b)
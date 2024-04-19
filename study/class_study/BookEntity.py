class Book:

    def __init__(self, bookId=0, bookName="", authorName="", publisherName="", isbn=""):  # __init__ = 생성자 , 
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.publisherName = publisherName
        self.isbn = isbn

    def setAuthor(self, author):
        self.author = author

    def __str__(self):
        # 큰따옴표("") 3개 사용 시 줄바꿈 가능
        return f"""Book[
bookId: {self.bookId}, 
bookName: {self.bookName},
authorName: {self.authorName}
publisherName: {self.publisherName}]""" # f 포맷팅 = {}안에 대입 가능
        # return "Book[bookId: {bookId}, bookName: {bookName}]".format(bookId = self.bookId, bookName = self.bookName)
        # return "Book[bookId: %d, bookName: %s]" % (self.bookId, self.bookName)
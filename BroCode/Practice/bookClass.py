class Book():
    def __init__(self, name, year, author, keyword):
        self.name = name
        self.year = year
        self.author = author
        self.keyword = keyword

    def read(self):
        print(f"Read {self.name}")
    def burn(self):
        print(f"Burned {self.name}")
    def describe(self):
        print(f"Name: {self.name}, Year: {self.year}, Author: {self.author}, Keyword: {self.keyword}")

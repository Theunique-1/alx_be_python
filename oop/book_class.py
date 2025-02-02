class Book:
    def __init__(self,title:str,author:str,year:int):
        self.title = title
        self.author = author
        self.year = year
        print(f"Book {self.title} created.")

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, publised in {self.year}"

    def __repr__(self):
        return f"Book({self.title}","{self.author}","{self.year}"


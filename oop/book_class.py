class Book:
    def __inint__(self,title:str,author:str,year:int):
        self.title = title
        self.author = author
        self.year = year
        print(f"Book {self.title} created.")

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, publised in {self.year}"

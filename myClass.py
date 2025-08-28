class Document:
    def __init__(self, auther, title, content,file_extension):
        self.title = title
        self.content = content
        self.auther = auther
        self.file_extension = file_extension

    # method to display title and content of the document
    def display(self):
        print(f"Title: {self.title}\nContent: {self.content}")
    # method to count words in content/document
    def word_count(self):
        return len(self.content.split())
    
    def file_type(self):
        return self.file_extension
    # get auther name
    def get_auther(self):
        return self.auther
    # update auther name
    def set_auther(self, new_auther):
        self.auther = new_auther


doc = Document("Sharon Chepkite", "Python Class", "This is to illustrate the use classes in python", ".txt")
doc.display()
print("Word Count:", doc.word_count())
print("File Type:", doc.file_type())
print("Auther:", doc.get_auther())
doc.set_auther(input("Enter new auther name: "))
print("Updated Auther:", doc.get_auther())

    

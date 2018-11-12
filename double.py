class Book:
    def __init__(self, data=None ):

        self.data = data
        self.next = None
        self.prev = None

class books:
    def __init__(self, title, author, num_page,):
        self.title = title
        self.author = author
        self.num_page = num_page
        self.__head = None

    def setHead(self, newbook):
        self.__head = Book(newbook)

    def display(self):
        printbook = self.__head
        print "Doubly linked list"
        print "========="
        while printbook is not None:
            print (printbook.data)
            printbook = printbook.next
        print "========="
        while printbook is not None:
            print (printbook.data)
            printbook = printbook.prev


    def append(self, new_book):

        new = Book(new_book)
        new.next = None
        if self.__head is None:
            new.prev = None
            self.__head = new
            return
        temp = self.__head
        while temp.next is not None:
            temp = temp.next
        temp.next = new
        new.prev = temp
        return

    def addAtBegining(self, newbook):
        newBook = Book(newbook)
        newBook.next = self.__head
        self.__head = newBook


    def reverse(self):
        temp = None
        current = self.__head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.__head = temp.prev
        print "\n""Reversed"


    def delete(self, item_id):
        current = self.__head
        while current is not None:
            if current.data == item_id:
                if current.prev != None:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.__head = current.next
                current.next.prev = None
            current = current.next

    def findInList(self, book):
        temp = self.__head
        while temp != None:
            if temp.data == book:
                print "{",book,"}", "is in list"
                break
            temp = temp.next
            if temp == None:
                print "{",book,"}", "is not in list"


def main():

   book1 = books()
   book1.setHead("The picture of Dorian Gray, Oscar Wilde, 176")
   book1.append("Me before you, Jojo Moyes, 384")
   book1.append("One + one, Jojo Moyes, 400")
   book1.append("The Boy in the Striped Pyjamas, A, 600")
   book1.append("gg, y, 390")
   book1.delete("One + one, Jojo Moyes, 400")
   book1.display()
   book1.reverse()
   book1.findInList("gg, y, 390")
   book1.addAtBegining("S, h, 79")
   book1.display()


main()








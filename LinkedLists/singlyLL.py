class Node:
    def __init__(self, value, next = None):
        self.value =  value
        self.next = next
    
    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self,value, next = None):
        self.head = Node(value)
        self.curr = self.head
        print("\nSuccessfully created Singly Linked List\n")
    
    def __str__(self):
        return str(self.head)
    
    def __repr__(self):
        return str(self.head)

    def insert_at_beginning(self,value):
        node = Node(value, self.head)
        self.head = node
        print("\nNODE successfully inserted at the beginning\n")


    def insert_at_end(self, value):
        if self.head == None:
            self.head = Node(value)
            self.curr = self.head
            
        else:
            node = Node(value)
            self.curr.next = node
            self.curr = node

        print("\nNODE successfully inserted at the end \n")

    def show_list(self):
        elements = []
        ptr = self.head
        while ptr is not None:
            elements.append(str(ptr.value))
            ptr = ptr.next
        
        print("\n\t\t"+"->".join(elements)+"\n")

if __name__ == "__main__":
    lists = []
    while True:
        q = int(input("Enter Choice : \n\t1.Create Linked List\n\t2.Show all lists\n\t3.Select List\n\t4.Exit\n >>"))
        match q:
            case 1:
                val = int(input("\nEnter value for the first node : "))
                l = LinkedList(val)
                lists.append(l)

            case 2:
                print(f"all the lists you've created are : \n\t{lists}")

            case 3 : 
                q = int(input(f"Select the index of the List {lists}:"))
                l = lists[q]
                while True:
                    q = int(input("Select the operation to perform : \n\t1.Insert element at the beginning.\n\t2.Insert element at the end.\n\t3.Show LIst\n\t4.Back to Menu\n>>"))
                    match q:
                        case 1:
                            val = int(input("\nEnter value to insert : "))
                            l.insert_at_beginning(val)
                        case 2:
                            val = int(input("\nEnter value to insert : "))
                            l.insert_at_end(val)
                        case 3:
                            l.show_list()
                        case 4:
                            break
                        case _:
                            print("\n\nInvalid Input\n\n")
            case 4:
                break
            case _:
                print("\n\nInvalid Input\n\n")
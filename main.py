from circular_linked_list import Clinkedlist

def main():
    cll = Clinkedlist()
    print("Circular Linked List:\n")
    cll.insert_end(5)
    cll.insert_end(10)
    cll.insert_end(20)
    cll.insert_end(25)
    cll.insert_end(30)
    cll.display()
    print("\nDelete node with value 10")
    cll.del_node(10)
    cll.display()
    print("\nSearch for 25:", cll.search(25))
    print("Search for 100:", cll.search(100))
    print("\nReverse the list")
    cll.reverse()
    cll.display()
    print("\nTotal nodes:", cll.count_node())
    print("\nClear the list")
    cll.clear()
    cll.display()
    
if __name__ == "__main__":
    main()


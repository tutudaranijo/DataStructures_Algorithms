# node # subclass of the linked list

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    # append function
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    # length

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    # display
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Error: 'get' Index not in range")
            return None
        cur_idx = 0
        cur_node = self.head

        while cur_node is not None:
            if cur_idx == index:
                if cur_node.data is not None:
                    return cur_node.data
                else:
                    print("Error: 'get' Node data is None")
                    return None
            cur_node = cur_node.next
            cur_idx += 1

        print("Error: 'get' Node not found")
        return None
# delete

    def erase(self, index):
        if index >= self.length():
            print(" Error: ' Erase' Index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list = linked_list()

my_list.display

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
my_list.display()

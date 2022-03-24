class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL():
    def __init__(self, head):
        self.head = head

    def add_front(self,value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp


        # add a method called contains(value) to your SLL class, which is given a value as a parameter.
        #Return a boolean (true/false); true, if the list possesses a node that contains the provided value.

    def contains(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

#Length
#Create a new SLL method length() that returns number of nodes in that list

    def length(self):
        runner = self.head # this can be written also as: temp = self.head
        count = 0
        while (runner):
            count += 1
            runner = runner.next
        return count





    def display(self):
        runner = self.head # we have to tell our runner that we want them to start at the front of the train
        count = 1
        while(runner): #we use while because a linked list doesn't know how many nodes is within it
            print(f"This is your {count} node, it contains value {runner.value}")
            count =+ 1
            runner = runner.next
        return self

llist = SLL()
llist.add_front(1).add_front(3).add_front(7).add_front(8)
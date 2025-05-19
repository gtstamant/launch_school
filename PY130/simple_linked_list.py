"""
## Problem ##
Implement a simple linked list
List is made up of Elements

Element class
- Contains data
- contains a next attribute pointing to another element
-- next is none if no other elements
-- next points to previous element

Linked list:
- contains elements
- one element is a "head" attribute

- Methods
-- size returns number of elements
-- is_empty returns boolean
-- push takes one argument and adds as eleemtn to list
-- peek returns some element, I think most recently added; None if no elements
-- head could be a property that returns most recently added element
-- is_tail returns a boolean, tail is oldest element
-- pop removes most recently added element
-- from_list creates list using list of data, each is added as an element in order left to right
-- r_peek peeks the first item
-- reverse reverses list
-- r_tail returns the 

"""
class Element:
    def __init__(self, datum, next=None):
        self._datum = datum
        self._next = next
    
    @property
    def datum(self):
        return self._datum

    @property
    def next(self):
        return self._next

    def is_tail(self):
        return self.next is None

class SimpleLinkedList:
    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @property
    def size(self):
        size = 0

        element = self.head
        while element:
            size += 1
            element = element.next

        return size
    
    def push(self, datum):
        element = Element(datum, self._head)
        self._head = element

    def is_empty(self):
        return self.head is None
    
    def peek(self):
        return self.head.datum if self.head else None
    
    def pop(self):
        popped = self.peek()
        self._head = self.head.next

        return popped

    @classmethod
    def from_list(cls, lst):
        lst = lst if lst else []

        linked_lst = SimpleLinkedList()
        for item in lst[::-1]:
            linked_lst.push(item)
        
        return linked_lst

    def to_list(self):
        lst = []
        
        element = self.head
        while element:
            lst.append(element.datum)
            element = element.next
        
        return lst

    def reverse(self):
        reversed_lst = self.to_list()[::-1]
        return SimpleLinkedList.from_list(reversed_lst)
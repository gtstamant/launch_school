"""
## Problem ##

Implement a custom set type
- Sets are a container
- Each element is unique
- Order doesn't matter

## Examples and Test Cases ##
CustomSet class
- __init__ method, accepts either one or no arguments
-- argument is a list of numbers

- is_empty method, returns boolean

- contains method, returns boolean

- is_subset, returns boolean

- is_disjoint, returns boolean

- is_same, returns boolean

- add, adds to set if unique

- intersection, returns intersection

- difference, returns difference

- union, returns union


"""
class CustomSet:
    def __init__(self, new_elements=None):
        self._elements = []

        if new_elements is None:
            new_elements = []

        for element in new_elements:
            self.add(element)

    @property
    def elements(self):
        return self._elements

    def is_empty(self):
        return not self.elements

    def contains(self, element):
        return element in self.elements

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
    
    def is_subset(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        
        return all(other.contains(element) for element
                                           in self.elements)

    def is_disjoint(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented

        return not any(other.contains(element) for element
                                               in self.elements)

    def is_same(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented

        return (len(self.elements) == len(other.elements) and
                    self.is_subset(other) and other.is_subset(self))

    def __eq__(self, other):
        return self.is_same(other)
    
    def intersection(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented

        return CustomSet([element for element in self.elements
                                              if other.contains(element)])

    def difference(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented

        return CustomSet([element for element in self.elements
                                              if not other.contains(element)])

    def union(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        
        return CustomSet([element for element in self.elements + other.elements])

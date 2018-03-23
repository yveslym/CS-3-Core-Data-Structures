#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.length() == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items

        return self.list.length()


    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? Because it is a single operation
        and doesn't iteract through the list"""
        # TODO: Insert given item
        self.list.append(item)

        '''running time 0(1)'''


    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.list.length() != 0:
            return self.list.head.data
        else:
            raise ValueError('the list is empty')

        '''running time 0(1)'''


    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? Because we are doing a single operation
        without interacting through a list. First, getting data from the
        head, next, move the head to the next node, and last return the data"""
        # TODO: Remove and return front item, if any
        if self.length != 0:
            data = self.list.head.data
            self.list.head = self.list.head.next
            return data
        else:
            raise ValueError('the list is empty')


        '''running time 0(1)'''

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list.length == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.length

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? Because it is a single operation
        and doesn't iteract through the list"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        return self.list.pop(1)


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue

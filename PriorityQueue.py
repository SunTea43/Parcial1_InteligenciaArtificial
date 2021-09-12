# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue():
    """
    Class of Priority Queue's structure

    Base taken from: https://www.geeksforgeeks.org/priority-queue-in-python/
    """
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def push(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def pop(self):
        """
        Definition that pop an element from the queue
        
        It considers that the elements are saved as (state, actions, cost)

        The priority is determined by the lower cost. 
        """
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][2] < self.queue[min][2]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            return None


class Stack:
    """
    A container with a last-in-first-out (LIFO) queuing policy.
    Taken from https://inst.eecs.berkeley.edu/~cs188/sp21/projects/
    """
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

#Taken from https://inst.eecs.berkeley.edu/~cs188/sp21/projects/
class Queue:
    """
    A container with a first-in-first-out (FIFO) queuing policy.
    Taken from https://inst.eecs.berkeley.edu/~cs188/sp21/projects/
    """
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0
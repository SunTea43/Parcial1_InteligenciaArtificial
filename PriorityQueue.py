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
"""
A Priority queue class implementation
"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = ''


class PriorityQueue:
    """list-based priority queue"""

    # define priority classes served in this
    # priority Q, plus labels ... (mind order)    
    URG, HGH, NOR, LOW = (0, 1, 2, 3)
    PRIO = (URG, HGH, NOR, LOW)
    PRIO_LBLS = ('URG', 'HGH', 'NOR', 'LOW')

    @staticmethod
    def getNrPrioritiesServed():
        """return count of priority classes"""
        return len(PriorityQueue.PRIO)
    
    @staticmethod
    def serves(priority):
        """return T|F priority supported in this Q"""
        return priority in PriorityQueue.PRIO
    
    def __init__(self, nr_priorities = len(PRIO)):
        """construct a queue supporting nr_priorities queues"""
        self.__qs = [[] for p in range(nr_priorities)]
        self.__count = [0] * nr_priorities

    def qsize(self, priority=None):
        """return count of queued item with prio, all if None"""
        if priority is not None:
            # return a count of given prio only ...
            sm = self.__count[priority]
        else:
            # return the total
             sm = sum([self.__count[p] for p in range(len(self.PRIO))])
        return sm
    
    def empty(self, priority=None):
        """return T/F is empty, for given prio, whole Q if None"""
        if priority is not None:
            # is queue of given priority empty?
            is_empty = ( self.__count[priority] == 0 )
        else:
            # are all queues empty?
            is_empty = not any([self.qsize(p) for p in range(len(self.PRIO))])
        return is_empty
    
    def enqueue(self, item, priority):
        """put item on prio queue with prio given"""
        self.__qs[priority].append(item)
        self.__count[priority] += 1

    def dequeue(self):
        """get the next item, priority in order from the priority queue"""

        pass
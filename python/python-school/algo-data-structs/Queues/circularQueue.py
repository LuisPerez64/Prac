class CircularQueue(object):
    """docstring for circularQueue
    Circular Queue Data Structure Implementation.
    Implementing a Ring Buffer. 
    The elements that are placed within the queue will replace the elements should the 
    queue reach full capacity.
    Functions: 
        Enqueue: Place an element into the Queue at the last index
        Dequeue: Remove an element, currently the first element in the queue
        PeeK: View the element that is at the head of the Queue
        Size: Get the current size of the list
        isEmpty: Returns whether or not the queue is empty
        printQueue: Outputs the Queue and Places Null's where no value exists 
    """
    def __init__(self, arg=None):
        super(circularQueue, self).__init__()
        if arg is None:
            arg=5
        self.__capacity = arg
        self.__queue=[ None for x in range(self.__capacity)]
        self.__endPointer=0
        self.__firstPointer=0
        self.__empty=True
        self.__size=0

    def enqueue(self, elt):
        self.__queue[self.__endPointer%self.__capacity]=elt
        self.__size+=1
        self.__updatePointers(1)
        
        if self.__endPointer == self.__firstPointer:
            # If the queue wrapped, and reached the first element.
            # It's basically been popped off, so next element is first.
            # And the list's size did not actually increment
            self.__updatePointers(0)
            self.__size-=1

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue from an empty queue.")
            return None
        elt=self.__queue[self.__firstPointer]
        self.__queue[self.__firstPointer]=None
        self.__size-=1

        # Move to the next element in the queue
        self.__updatePointers(0)
        
        # Empty Queue. Begin == End Pointers
        if self.isEmpty():
            self.__firstPointer=self.__endPointer
        return elt

    def peek(self):
        return self.__queue[self.__firstPointer]
    
    def size(self):
        print(self.__size)

    def isEmpty(self):
        self.__empty=False
        if self.__size == 0:
            self.__empty=True
        return self.__empty
    def printQueue(self):
        for elt in self.__queue:
            print(elt if elt is not None else 'Null')

    def __dataDump(self):
        print('\nEnd:{1}\tFirst:{2}\tSize:{3}\tQueue:{4}\n'.format(None,self.__endPointer, self.__firstPointer, self.__size, self.__queue))

    def __updatePointers(self, upd):
        if  upd == 0:
            self.__firstPointer= (self.__firstPointer+1) % self.__capacity
        elif upd== 1: 
            self.__endPointer= (self.__endPointer+1) % self.__capacity
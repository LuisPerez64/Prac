# Miscellaneous Notes for some of the Caveats that are encountered within the Language
## Language Primitives:
### Introductory Conditional statements.
    Came accross Pythons Ternary operator, not as it is in most languages ie. C/C++
```c
int x = 0;
int y = (x == 0 ? 12 : 15)
// Format: condition_check ? condition_is_true : condition_is_false
```
    Python's implementation is:
```python
x = 0
y = 12 if x == 0 else 15
# Format: condition_is_true if condition_check else condition_is_false
```

## Iterators:
    Pythons Iterators, the base and those found in itertools all return a handle to an iterator that can be operated on. The iterators run until the next variable they are trying to reference is null, and then raise a StopIteration exception. 
### Introduction to [next](https://docs.python.org/3.6/library/functions.html#next)
    The Iterators accessor. This function is able to get the next variable that would come as the result of executing an iterator. Does so by calling the iteratorType.__next__() property. Comes with an added bonus of being able to search through the iterator as it goes forth. Also comes with a detrimental caveat. Once next is called on an iterator, there's no clean way to go back. If StopIteration is met, would have to reverse the iterator with "reversed()?" function to be able to walk through it again.
```python
# Base Use:   
>>> x=enumerate([1,3,5,7])
>>> next(x)
(0, 1)

# Attempts to use it to search
>>> x=enumerate([1,3,5,7])
>>> next( ind for ind,elt in x if elt == 3) 
1
>>> next( ind for ind,elt in x if elt == 5) 
2
# Attempts to search for the element again are me with StopIteration.
# Next alters the element pointed to within the generated iterator functions. 
# It does not hold onto the whole object being referenced when possible and loads only what is needed.
>>> next( ind for ind,elt in x if elt == 5) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### Introduction to [enumerate](https://docs.python.org/3.6/library/functions.html#enumerate) 
    An iterator, cannot be used alone, must be used within an iterator construct. Returns pairs of type (index, element), indexing the input on a base system, where the tuple returned holds the index of the element for a given iteratable type.
```python
inp=['a','b','c','d']
for i,j in enumerate(inp):
    print(i,j)
#Output:
'''
0 a
1 b
2 c
3 d
'''
```

## Classes:
### Self
##### Summary. Explanation, at least attempt at, bringing forth knowledge about referencing self | this, within a python class. 
    'self' is an instantiation of a temporary handle to the object that is created, or being referenced.
    self is a local 'reference' to the instance, and as such changing self, will not change the instance.
    Changes to variables for the instance can be altered or created, if the class is passed an object as it's type (look into this note) at any point by referencing self._someVar.
    If self = _someThing_ is called, then all that occurs is that the handle to the instance is gone, and unless it was placed in another variable beforehand, it cannot be referenced, to my knowledge at the time, until that function is escaped. 

```python
class MyClass(object):
    def __init__(self):
        super(MyClass, self).__init__()
#   ...
    # Attempt to reference self, will return the address of the instance that is being referenced, and also allow mutation of variables stored in (self, which is the instance)
    ''' Outputs: Some Address, and the name of the object
    >>> print(MyClass)
    <class '__main__.MyClass'>
    >>> l=MyClass()
    >>> print(l)
    <__main__.MyClass object at 0x7fcc3ab75390>
    '''

# Code Snippet in which self.__*Node is being modified. Any of those two references to the __*Node  instance variable are mutated past this point. 
#   ...
    # Simulation of freeing up the node.
    # In this context self would be some node that called the function.
    def setNode(self, direction, node=None):
        # Free's up either the left or right node, if no new node is passed in
        # Else makes the left|right point to the node passed in.
        if direction == 'left':
            self.__leftNode = node
        elif direction == 'right':
            self.__rightNode= node
        else:
            print('Not given a handle to operate on.')
            return 1
#   ...
# However, attempts to mutate the node that is being pointed to will not reveal themselves to be effective, because as soon as self, leaves the context of the function that it's working within, it's lost. Within the context of the previous function, if attempting to alter the node itself, through self ie
#   ...
    elif direction == 'this':
        self = node
    # Printing self Before and after this assignment would yield a reference similar to <__main__.MyClass object at 0x7fcc3ab75390> but with reference to the object class to which self belongs, and then a reference to the new node that is handed, if it were none then self would be None, but upon exiting, no change would be made to the instances node. Changes could be made to the node that was passed in though, due to pointing to it now, but handle to previous instance is gone..
```
### Class Wide Variables:
##### Summary. Addressing self.classVar alters instance. Addressing MyClass.classVar alters static variable created at initialization of MyClass.
    These are variables designed within the construct
```python
>>> class MyClass(object):
>>>    classVar=0
"""    
These variables are more or less static variables. On any instance that is created they remain constant, in that unless explicitly done so, are not dependent on the construction of objects within the given class.
If the classVar is altered by an object that is instantiated, it changes only within itself", and it's children?", but does not change the variables value within the context of the class. It becomes at that point a local "static" variable. Any new instances will not hold the new value, but the initial value placed in the classVar at initialization. 
Example:
"""
>>> foo=MyClass()
# Checking the value stored, at init
>>> foo.myVar
>>> 0
>>> MyClass().myVar
>>> 0

#Altered the value within the object constructed, does not change the evaluation of the variable within the context of the class.
>>> foo.myVar=5
>>> foo.myVar
>>> 5
>>> MyClass.myVar
>>> 0

# Instantiate a new variable. Inherits it's value from classWide instance. The context of foo is unchanged, no longer thethered to the class variable.
>>> bar=MyClass()
>>> bar.myVar
>>> 0
>>> foo.myVar
>>> 5

# Change the variable itself, and alter it within the context of the classes declarations. The changes, or lack thereof, made in instances of the class are not affected.
>>> MyClass.myVar=4
>>> bar.myVar
>>> 0
>>> foo.myVar
>>> 5
>>> MyClass.myVar
>>> 4

# Creation of an instance based off of the new variable stored in the class. Will hold the newly defined class variable. The ones from before are still holding on to what they defined themselves as.
>>> baz=MyClass()
>>> baz.myVar
>>> 4
>>> foo.myVar
>>> 5
>>> bar.myVar
>>> 0
>>> MyClass.myVar
>>> 4

# Here is where it gets a bit weird, but with the inheritance model of python makes some sense.
# If the class variable is changed, from within the class construct, and has not been "unthethered" from the initial 
# class by altering it's value, then changes to the class, are now changes to the new var. 
# (If I understand this correctly) Because changes to the class are referencing the same address until,
# they are made their own, and hard copied over to a new address within the constraints of the New Objects.
>>> baz.myVar
>>> 4
>>> MyClass.myVar
>>> 4
>>> MyClass.myVar=8
>>> MyClass.myVar
>>> 8
>>> baz.myVar
>>> 8
``` 
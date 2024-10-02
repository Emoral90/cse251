'''
Requirements:
1. Create a class that extends the 'threading.Thread' class (see https://stackoverflow.com/questions/15526858/how-to-extend-a-class-in-python). This means that the class IS a thread. 
   Any objects instantiated using this class ARE threads.
2. Instantiate this thread class that computes the product of all numbers 
   between one and that number (exclusive)
3. COMMENT every line that you write yourself.

Things to consider:
a. How do you instantiate a class and pass in arguments (see https://realpython.com/lessons/instantiating-classes/)?
b. How do you start a thread object (see this week's reading)?
c. How will you wait until the thread is done (see this week's reading)?
d. How do you get the value an object's attribute (see https://datagy.io/python-print-objects-attributes/)?
'''

import threading
from cse251functions import *

###############################
# DO NOT USE YOUR OWN GLOBALS #
###############################

# Create Thread_product class by inheiriting from the threading.Thread class
class Thread_product(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        # Store the input and init the product to save the result
        self.n = n
        self.product = 1

    # Defeine the behavior of the thread by calculating the factorial
    def run(self):
        for i in range(1, self.n):
            self.product *=i


def main():
    # Instantiate your thread class and pass in 5 (delete this line).
    # Test (assert) if its product attribute is equal to 45 (delete this line).
    # Note: do no use 'yourThread' as the name of your thread object (delete this line).

    # Create, start, and join threaded class with an argument of 5
    t5 = Thread_product(5)
    t5.start()
    t5.join()
    assert t5.product == 24, f'The product should equal 24 but instead was {
        t5.product}'

    # Create, start, and join threaded class with an argument of 10
    t10 = Thread_product(10)
    t10.start()
    t10.join()
    assert t10.product == 362880, f'The product should equal 362880 but instead was {
        t10.product}'

    # Create, start, and join threaded class with an argument of 15
    t15 = Thread_product(15)
    t15.start()
    t15.join()
    assert t15.product == 87178291200, f'The product should equal 87178291200 but instead was {
        t15.product}'


if __name__ == '__main__':
    main()
    print("DONE")
    create_signature_file()

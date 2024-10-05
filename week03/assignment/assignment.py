'''
Requirements
1. Write a multithreaded program that counts the number of prime numbers 
   between 100,000,000 and 100,370,803.
2. The program should be able to use a variable amount of threads.
3. Each thread should look over an approximately equal number of numbers.
   This means that you need to devise an algorithm that can divide up the
   370,803 numbers "fairly" based on a variable number of threads. 
4. The algorithm should work for 1 to 101 threads.
5. COMMENT every line that you write yourself.
   
Questions:
1. Time to run using 1 thread = Avg of 3.25 sec
2. Time to run using 10 threads = 3.25 sec
3. Time to run using 50 threads = 3.26 sec
4. Time to run using 101 threads = 3.24 sec
4. Based on your study of the GIL (see https://realpython.com/python-gil), 
   what conclusions can you draw about the similarity of the times (short answer)?
   > Python's GIL only allows for 1 active thread to run on the CPU, which means it can't truly run concurrently despite having more than 1 core. 
   >
5. Is this assignment an IO Bound or CPU Bound problem (see https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)?
   > This one is CPU bound
'''

import math
import threading
import time
from datetime import datetime, timedelta

from cse251functions import *

# Global count of the number of primes found
PRIME_COUNT = 0

# Global count of the numbers examined
NUMBERS_EXAMINED_COUNT = 0

# The number of threads to use (should try 1, 10, 50, and 101 and
# report results above in the questions)
NUMBER_THREADS = 1

def is_prime(n: int):
    """
    Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test

    Parameters
    ----------
    ``n`` : int
        Number to determine if prime

    Returns
    -------
    bool
        True if ``n`` is prime.
    """

    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    # Start a timer
    begin_time = time.perf_counter()

    # number to start at
    first_number = 100_000_000

    # interval to check over
    interval = 370_803

    # number to end at
    last_number = first_number + interval - 1

    # Divide the range among threads
    step = interval // NUMBER_THREADS
    threads = []
    # remainder = interval % NUMBER_THREADS
    start = first_number # For my own sanity when I plug in the args in the thread
    lock = threading.Lock()

    def check_primes_in_range(start, end, lock):
        global PRIME_COUNT, NUMBERS_EXAMINED_COUNT
        local_prime_count = 0
        local_examind_count = 0

        # Loop through specified range to check for primes
        for num in range(start, end + 1):
            if is_prime(num):
                local_prime_count += 1
            local_examind_count += 1

        # Update globals safely with lock
        with lock:
            PRIME_COUNT += local_prime_count
            NUMBERS_EXAMINED_COUNT += local_examind_count

        # print(f"Thread checked range {start}-{end}: Primes = {local_prime_count}, Examined = {local_examind_count}")


    for i in range(NUMBER_THREADS):
        # Calculate start and end values for each thread
        # end = start + step - 1
        # if i < remainder:
        #     end += 1

        start = first_number + i * step
        end = start + step - 1 if i < NUMBER_THREADS - 1 else last_number

        # Start thread to check primes in the assigned range
        t = threading.Thread(target=check_primes_in_range, args=(start, end, lock))
        threads.append(t)
        t.start()

    # Join all threads
    for t in threads:
        t.join()

    # Check how many threads are active?
    print(f"Final active threads: {threading.active_count()}")

    # Use the below code to check and print your results
    assert NUMBERS_EXAMINED_COUNT == 370_803, f"Should check exactly 370,803 numbers, but checked {
        NUMBERS_EXAMINED_COUNT:,}"
    assert PRIME_COUNT == 20_144, f"Should find exactly 20,144 primes but found {
        PRIME_COUNT:,}"

    # Print out summary
    print(f'Numbers processed = {NUMBERS_EXAMINED_COUNT:,}')
    print(f'Primes found = {PRIME_COUNT:,}')
    total_time = "{:.2f}".format(time.perf_counter() - begin_time)
    print(f'Total time = {total_time} sec')


if __name__ == '__main__':
    main()
    create_signature_file()

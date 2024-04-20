import math
import numpy as np
from sympy import prime
from pathlib import Path  # for paths of files
import csv
import copy
import random
from sklearn.metrics.pairwise import cosine_similarity

# ANSI escape codes for colors
class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    end = '\033[0m'  
# Username data for the creation of bloom filters - B
data_file = (Path("data/bloom_username").with_suffix('.csv'))

# Test data to check the functionality and false positive rate
test1_file = (Path("data/test1_username").with_suffix('.csv'))
test2_file = (Path("data/test2_username").with_suffix('.csv'))

# Default bloom filter parameters
bloom_size = 1500000 # parameter N
h = 3 # number of hash functions

# create an array of bloom filter with zeros
B = np.zeros(bloom_size)

# def print_progress_bar(i, N):
#     """
#     Prints a progress bar to the console to visually indicate the progress of a task.

#     The progress bar is colored and updates dynamically in the terminal, providing a visual and numerical 
#     indication of the task's completion percentage. The function is designed to be called within a loop to 
#     update the progress bar in place.

#     Args:
#         i (int): The current progress of the task (e.g., the current loop iteration number). 
#                  Should start at 0 and go up to N-1.
#         N (int): The total number of iterations the task will perform, representing 100% completion.

#     Returns:
#         None: This function does not return a value but prints the progress bar to the standard output.
#     """
#     bar_length = 40
#     progress = i / N
#     num_bar_filled = int(bar_length * progress)
#     bar = '\033[35m#' * num_bar_filled + '\033[0m-' * (bar_length - num_bar_filled)
#     percent_complete = progress * 100
#     print(f'[{bar}] {percent_complete:.1f}% Complete', end='\r')


def generatePrimes(n):
    i = 3
    primes=[2]
    flag = False
    while(len(primes) < n):
        flag = True
        for j in primes:
            if math.floor(math.sqrt(i)) + 1 <= j:
                break
            elif (i%j == 0):
                flag = False
                break
        if(flag):
            primes.append(i)
        i+=1
    
    return primes


def generate_hash(h, N):
    hash_list = []
    primes=generatePrimes(h)

    for p in range(h):
        func = lambda s: sum([ord(s[i])*primes[p]**(i+1) for i in range(len(s))])%N
        hash_list.append(func)
    return hash_list


hashes = generate_hash(h, bloom_size)

def create_bloom_filter(B, hashes, data):
    with data.open(encoding="utf-8") as f:
        for name in f:
            for hash in hashes:
                index=hash(name)
                B[index]=1
        
            
    return B

bloom_array = create_bloom_filter(B, hashes, data_file)
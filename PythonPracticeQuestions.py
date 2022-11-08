# Codility Practice Questions

############################### Lesson 1: Binary Gap ###############################

def solution(N):
    print('binary:', format(N, 'b'))
    binary = format(N, 'b')
    zeros_arr = binary.split('1')
    zeros_arr.pop(-1)
    max_length = len(max(zeros_arr))
    print('longest binary gap:', max_length)
    
solution(277)

############################### Lesson 2: Arrays ###############################

# Cyclic Rotation
array = [3,8,9,7,6]

def solution(A, K):
    if len(A) == 0:
        return A
    if K == 0:
        print(A)
    elif K == 1:
        A.insert(0, A[-1])
        A.pop(-1)
        print(A)
    elif K == len(A):
        print(A)
    else:
        while K > 0:
            A.insert(0, A[-1])
            A.pop(-1)
            K = K - 1
        print(A)
    
solution(array, 3)

# Odd Occurrences in Array
import numpy as np

array = [3,9,9,6,3,5,6,3,5,5,3]

def solution(A):
    new_arr = []
    for i in A:
        for j in A:
            if i == j:
                new_arr.append(i)
    bin_count = np.bincount(new_arr)
    
    for i in bin_count:
        if i % 2 != 0:
            index, = np.where(bin_count == i)
            print(index[0])
    
solution(array)

############################### Lesson 3: Time Complexity ###############################
# Frog Jump
def solution(X, Y, D):
    gap = Y - X
    flt = gap / D
    res = int(-(-flt // 1))
    print(res)
    
solution(10, 85, 30)

# Find the missing element in a given permutation
import numpy as np

array = [1,2,3,4,6,7]

def solution(A):
    bin_count = np.bincount(A)
    bin_count_slice = bin_count[1:]
    for i in bin_count_slice:
        if i == 0:
            index, = np.where(bin_count_slice == i)
            result = index[0] + 1
            print(result)
    
solution(array)

# without numpy - 100%
def solution(A):
    xor_sum = 0
    for i in A:
        xor_sum = xor_sum ^ i
    
    xor_full_sum = 0 
    for i in range(1,len(A)+2):
        xor_full_sum = xor_full_sum ^ i
        
    print(xor_full_sum ^ xor_sum)

# Tape Equilibrium
# correct but not efficient - 53%
array = [3,1,2,4,3]
def solution(A):
    length = len(A)
    P_arr = [i for i in range (1, length)]
    diffs_arr = []

    for i in P_arr:
        split_arr_one = A[:i]
        split_arr_two = A[i:]
        
        one_sum = 0
        two_sum = 0
        
        for i in split_arr_one:
            one_sum = one_sum + i
        
        for i in split_arr_two:
            two_sum = two_sum + i
            
        res = abs(one_sum - two_sum)
        
        diffs_arr.append(res)

    print(min(diffs_arr))
    
solution(array)


# correct and efficient - 100%
def solution(A):          
    array_sum = sum(A)
    array_difs = []
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        array_difs.append(abs(array_sum - 2*left_sum))
    return min(array_difs)


############################### Lesson 4: Counting Elements ###############################
# Frog River One
array = [1,3,1,4,2,3,5,4,2,3,1,4,5,1,2,5,3,2,1,3,4,5]

def solution(X, A):
    arr = []
    while len(arr) < X:
        for i in A:
            if i not in arr:
                arr.append(i)
                if i == X:
                    ind = A.index(i)
                    print(ind)
                
solution(5, array)

# Permutation Check
array = [1,3,4,2]

def solution(A):
    sum = 0
    for i in A:
        sum = sum + i
    
    full_sum = 0 
    for i in range(1,len(A)+1):
        full_sum = full_sum + i

    if sum == full_sum:
        print(1) 
    else:
        print(0)

solution(array)












































# find a possible solution for the missing dice rolls
# A is the array of dice rolls you remember
# F is the number of results you forgot
# M is the mean of all the results


# first attempt solution
import math
def solution(A, F, M):
    no_of_rem_res = len(A)
    
    no_of_res = no_of_rem_res + F
    
    total_rem_score = sum(A)
    
    total_score = M*no_of_res
    
    total_forgo_score = total_score - total_rem_score

    pos_arr = []
    
    if total_forgo_score <= 0 or total_forgo_score < F:
        print([0])
        return
    
    initial = total_forgo_score/F
    
    rem = total_forgo_score % F
    
    if initial > 6:
        print([0])
        return
    
    if initial == 6 and rem > 0:
        print([0])
        return
    
    x = 0
    
    pos_arr = [0]*F

    
    while sum(pos_arr) < total_forgo_score:
        while x < F:
            for i in range(x,len(pos_arr)):
                print(i)
                pos_arr[i] = pos_arr[i] + 1
                x = x + 1
    

    print(pos_arr)
    
solution([1,5,6], 4, 3)






# Second attempt solution
import math
def solution(A, F, M):
    no_of_rem_res = len(A)
    
    no_of_res = no_of_rem_res + F
    
    total_rem_score = sum(A)
    
    total_score = M*no_of_res
    
    total_forgo_score = total_score - total_rem_score

    pos_arr = []
    
    #add sixes to array
    div_six_score = math.floor(total_forgo_score/6)
    
    if div_six_score >= 1:
        for i in range(div_six_score):
            pos_arr.append(6)
        
    pos_arr_sum_one = sum(pos_arr)
    
    score_left_one = total_forgo_score - pos_arr_sum_one
    
    
    #add fives to array
    div_five_score = math.floor(score_left_one/5)
    
    if div_five_score >= 1:
        for i in range(div_five_score):
            pos_arr.append(5)
        
    pos_arr_sum_two = sum(pos_arr)
    
    score_left_two = total_forgo_score - pos_arr_sum_two
    
    
    #add fours to array
    div_four_score = math.floor(score_left_two/4)
    
    if div_four_score >= 1:
        for i in range(div_four_score):
            pos_arr.append(4)
        
    pos_arr_sum_three = sum(pos_arr)
    
    score_left_three = total_forgo_score - pos_arr_sum_three
    
    #add threes to array
    div_three_score = math.floor(score_left_three/3)
    
    if div_three_score >= 1:
        for i in range(div_three_score):
            pos_arr.append(3)
        
    pos_arr_sum_four = sum(pos_arr)
    
    score_left_four = total_forgo_score - pos_arr_sum_four
    
    #add twos to array
    div_two_score = math.floor(score_left_four/2)
    
    if div_two_score >= 1:
        for i in range(div_two_score):
            pos_arr.append(2)
        
    pos_arr_sum_five = sum(pos_arr)
    
    score_left_five = total_forgo_score - pos_arr_sum_five
    
    #add one to array
    if score_left_five != 0:
        pos_arr.append(1)
    
    print(pos_arr)
    
    
solution([1,5,6], 4, 3)
































import re

def solution(S):
    arr = re.split("\.|\?|\!", S)
    print(arr)
    
    split_arr = []
    
    lengths = []
    
    for i in arr:
        split_arr = i.split(" ")
        print("split_arr", split_arr)
        for j in split_arr:
            if '' in split_arr:
                split_arr.remove('')
            lengths.append(len(split_arr))

    print(max(lengths))

    
string = "We test coders. Give us a try?"

solution(string)





# Problem Set 4A
# Name: <M. Mehdi Taherzadeh>
# Collaborators: < - >
# Time Spent: <3:15>

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:

    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''


    #a function that takes one character and a list containing the permutations of the remaing characters
    #and outputs all permutations of the charachters in the list + the single input character
    def get_perm(char, perm_list):
        permutation_list = []
        for seq in perm_list:
            for i in range(len(seq) + 1):
                permutation_list.append(seq[:i] + char + seq[i:])
        return permutation_list

    #base case if sequence has only one character then return a list containing one element: sequence itself
    if len(sequence) == 1:
        return [sequence]
    #recursion case: smaller (n-1) slices of the string are recursively called through the same function until
    #it reaches the base case
    else:
        #the list() and the set() functions are used to ensure that the output is list of unique elements
        return list(set(get_perm(sequence[0], get_permutations(sequence[1:]))))


#this function takes an input string and its corresponding permutation list and outputs a text telling if the function
#outputs the correct permutation list
#it checks if the length of the lists are equal and if every permutation in the function output is also in the
#expected output
def is_correct(input, expected):
    correct = True
    if len(get_permutations((input))) == len(expected):
        for seq in get_permutations(input):
            if seq in expected:
                correct = True
            else:
                correct = False
                break
    else:
        correct = False

    if correct == True:
        print('----------------------------------------------------\nWell Done! Your list matches the expected output.')
    else:
        print('----------------------------------------------------\nWhoops! Your function does not work as expected!')


if __name__ == '__main__':

#    #EXAMPLE
    example_input = 'abc'
    print('*************\nInput #1:', example_input)
    expected_output = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print('Expected Output:', expected_output)
    print('Actual Output:', get_permutations(example_input))
    is_correct(example_input, expected_output)

#    #EXAMPLE
    example_input = 'ab'
    print('*************\nInput #2:', example_input)
    expected_output = ['ab', 'ba']
    print('Expected Output:', expected_output)
    print('Actual Output:', get_permutations(example_input))
    is_correct(example_input, expected_output)

#    #EXAMPLE
    example_input = 'abb'
    print('*************\nInput #3:', example_input)
    expected_output = ['abb', 'bba', 'bab']
    print('Expected Output:', expected_output)
    print('Actual Output:', get_permutations(example_input))
    is_correct(example_input, expected_output)

#    #EXAMPLE
    example_input = 'bust'
    print('*************\nInput #4:', example_input)
    expected_output = ['bust', 'ubst', 'usbt', 'ustb', 'bsut', 'sbut', 'subt', 'sutb', 'bstu', 'sbtu', 'stbu', 'stub',
                       'buts', 'ubts', 'utbs', 'utsb', 'btus', 'tbus', 'tubs', 'tusb', 'btsu', 'tbsu', 'tsbu', 'tsub']
    print('Expected Output:', expected_output)
    print('Actual Output:', get_permutations(example_input))
    is_correct(example_input, expected_output)


#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length
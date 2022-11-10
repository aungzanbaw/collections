'''
    [8 Queens in 6 lines](https://code.activestate.com/recipes/576647/)
    Originally by Raymond Hettinger
    On a regular 8x8 board only 40,320 possible queen positions are examined.

    With the solution represented as a vector with one queen in each row, we don't have to check to see if two queens are on the same row. By using a permutation generator, we know that no value in the vector is repeated, so we don't have to check to see if two queens are on the same column. Since rook moves don't need to be checked, we only need to check bishop moves.
    The technique for checking the diagonals is to add or subtract the column number from each entry, so any two entries on the same diagonal will have the same value (in other words, the sum or difference is unique for each diagonal). Now all we have to do is make sure that the diagonals for each of the eight queens are distinct. So, we put them in a set (which eliminates duplicates) and check that the set length is eight (no duplicates were removed).
    Any permutation with non-overlapping diagonals is a solution. So, we print it and continue checking other permutations.
'''
from itertools import permutations

n = 8
columns = range(n)

def board(vec):
    #(Optional)Translate column positions to an equivalent chess board.
    for col in vec:
        s = ['-'] * len(vec)
        s[col] = 'Q'
        print(''.join(s))
    print()

for vec in permutations(columns):
    if n == len(set(vec[i]+i for i in columns)) \
         == len(set(vec[i]-i for i in columns)):
        board ( vec ) # print(vec) for raw vector(just 6 lines of code)
# easy way utilizing python's itertools
import itertools

my_array = [50913,47946,97391,27488,69147]
# 47946 50913 97391 27488 69147
#   1     0     2     3     4
# Generate all permutations
all_permutations_iterator = itertools.permutations(my_array)

# Convert the iterator to a list of tuples for easier viewing
all_permutations_list = list(all_permutations_iterator)

# or loop over without converting it to a list for memory efficiency
for item in all_permutations_iterator:
    print(*item)

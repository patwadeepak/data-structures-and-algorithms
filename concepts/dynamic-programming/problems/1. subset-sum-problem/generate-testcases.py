import random
import sys
import os

# Change the current working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

# Constants for file names. You can change these to configure the output.
INPUT_FILE_NAME = "subset_sum_input.txt"
OUTPUT_FILE_NAME = "subset_sum_output.txt"

# Constants for problem constraints.
MIN_ARR_SIZE = 1
MAX_ARR_SIZE = 200
MIN_ARR_ELEM = 1
MAX_ARR_ELEM = 200
MIN_SUM = 1
MAX_SUM = 10000

# Number of test cases to generate.
NUM_TEST_CASES = 50

# Set a higher recursion limit for deep recursive calls, though this
# script uses an iterative DP approach which doesn't need it.
sys.setrecursionlimit(200000)

def solve_subset_sum_dp(arr, target_sum):
    """
    Solves the subset sum problem using dynamic programming (tabulation).

    Args:
        arr: A list of positive integers.
        target_sum: The target sum to check for.

    Returns:
        True if a subset with the target_sum exists, False otherwise.
    """
    # Create a 2D DP table. dp[i][j] will be True if a sum of j is possible
    # with the first i elements of the array.
    dp = [[False] * (target_sum + 1) for _ in range(len(arr) + 1)]

    # Base case: A sum of 0 is always possible with an empty set.
    for i in range(len(arr) + 1):
        dp[i][0] = True

    # Fill the DP table.
    for i in range(1, len(arr) + 1):
        for j in range(1, target_sum + 1):
            # If the current element is greater than the current sum,
            # we can't include it. The solution is the same as the previous row.
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # We can either not include the current element (dp[i-1][j])
                # or include it (dp[i-1][j - arr[i-1]]).
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[len(arr)][target_sum]

def generate_and_solve_test_cases():
    """
    Generates test cases for the subset sum problem, writes them to an input file,
    solves them, and writes the results to an output file.
    """
    try:
        with open(INPUT_FILE_NAME, 'w') as input_file, open(OUTPUT_FILE_NAME, 'w') as output_file:
            print(f"Generating and solving {NUM_TEST_CASES} test cases...")
            for i in range(NUM_TEST_CASES):
                # Generate random array size and elements.
                arr_size = random.randint(MIN_ARR_SIZE, MAX_ARR_SIZE)
                arr = [random.randint(MIN_ARR_ELEM, MAX_ARR_ELEM) for _ in range(arr_size)]

                # Generate a random sum.
                target_sum = random.randint(MIN_SUM, MAX_SUM)

                # Write the input to the input file.
                input_str = f"{arr_size} {target_sum} {' '.join(map(str, arr))}\n"
                input_file.write(input_str)

                # Solve the problem and write the output to the output file.
                is_subset_sum = "True" if solve_subset_sum_dp(arr, target_sum) else "False"
                output_file.write(is_subset_sum + "\n")

            print("Successfully generated inputs and outputs. Check the files:")
            print(f"  - Input file: {INPUT_FILE_NAME}")
            print(f"  - Output file: {OUTPUT_FILE_NAME}")

    except IOError as e:
        print(f"Error writing to files: {e}")

if __name__ == "__main__":
    generate_and_solve_test_cases()

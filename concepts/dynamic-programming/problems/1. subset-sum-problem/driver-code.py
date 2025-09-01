import sys
import os

# since non memoization or tabulation used this one keeps going on and never stops.
# from subset_sum_recursion import Solution # don't actually run this. only try on very very small dataset.
# from subset_sum_memoization import Solution
from subset_sum_tabulation import Solution

# Change the current working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

# Constants for configurable file names.
INPUT_FILE_NAME = "subset_sum_input.txt"
OUTPUT_FILE_NAME = "driver-code.output"

def run_driver():
    """
    Reads test cases from the input file, runs the solution, and writes
    the output to a new file.
    """
    try:
        # Open input file for reading and output file for writing.
        with open(INPUT_FILE_NAME, 'r') as input_file, open(OUTPUT_FILE_NAME, 'w') as output_file:
            print(f"Reading from '{INPUT_FILE_NAME}' and writing to '{OUTPUT_FILE_NAME}'...")

            # Instantiate the solution class once.
            sol = Solution()

            # Process each line (test case) from the input file.
            for line in input_file:
                # Split the line and parse the values.
                parts = line.strip().split()
                if not parts:
                    continue

                arr_size = int(parts[0])
                total_sum = int(parts[1])
                arr = list(map(int, parts[2:]))

                # Check if the parsed data matches the expected size.
                if len(arr) != arr_size:
                    print(f"Warning: Array size mismatch in input. Expected {arr_size}, got {len(arr)}.")
                    continue

                # Call the solution method and get the result.
                result = sol.isSubsetSum(arr, total_sum)

                # Write the result to the output file with a newline.
                output_file.write(str(result) + "\n")

        print("Driver script finished successfully.")

    except FileNotFoundError:
        print(f"Error: One of the files was not found. Please make sure '{INPUT_FILE_NAME}' exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_driver()

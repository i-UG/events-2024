'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

# Explanation:
#
# Define the mean function: Calculates the average of the list of numbers by dividing the sum of the numbers by the count of the numbers.
# Define the median function:
# Sorts the list of numbers.
# Determines the middle index.
# If the number of elements is odd, returns the middle element.
# If the number of elements is even, returns the average of the two middle elements.
# Define the mode function:
# Creates a frequency dictionary to count occurrences of each number.
# Identifies the highest frequency.
# Finds and returns the number corresponding to the highest frequency (assuming there is a single mode).
# Calculate and store statistics:
# Calls the mean, median, and mode functions.
# Stores the results in a dictionary stats.
# Return the dictionary: The function returns the stats dictionary containing the computed statistics.
# Example usage: The provided example demonstrates how to use the function with a given list of numbers and prints the resulting statistics.

def calculate_statistics(numbers):
    def mean(nums):
        return sum(nums) / len(nums)

    def median(nums):
        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        mid = n // 2
        if n % 2 == 0:
            return (nums_sorted[mid - 1] + nums_sorted[mid]) / 2
        else:
            return nums_sorted[mid]

    def mode(nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        most_frequent = max(frequency.values())
        mode_val = [num for num, freq in frequency.items() if freq ==
                    most_frequent]
        return mode_val[0]  # Assuming there is a single mode

    stats = {
        'mean': mean(numbers),
        'median': median(numbers),
        'mode': mode(numbers)
    }
    return stats


# Example usage
numbers = [1, 2, 2, 3, 4]
stats = calculate_statistics(numbers)
print(stats)  # Output: {'mean': 2.4, 'median': 2, 'mode': 2}

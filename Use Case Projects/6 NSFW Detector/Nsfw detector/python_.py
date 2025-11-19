# Define the list of elements
my_list = [6, 2, 2, 3, 4, 6, 5, 7, 6, 6, 6, 6, 6, 7]

# Initialize variables to track the current element and its count
current_element = None
current_count = 0

# Initialize variables to track the greatest common duplicate and its count
greatest_duplicate = None
greatest_count = 0

# Iterate over each element in the list
for element in my_list:
    # Check if the current element is the same as the current one
    if element == current_element:
        # If yes, increment the count
        current_count += 1
    else:
        # If not, update the greatest duplicate if needed
        if current_count > greatest_count:
            greatest_duplicate = current_element
            greatest_count = current_count
        # Reset variables for the new element
        current_element = element
        current_count = 1

# Check the last element after the loop
if current_count > greatest_count:
    greatest_duplicate = current_element
    greatest_count = current_count

# Print the result for the greatest common duplicate
if greatest_count > 1:
    print(f"The greatest common duplicate is: {greatest_duplicate} (occurs {greatest_count} times)")

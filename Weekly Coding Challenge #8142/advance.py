# Get the input number from the user
input_number = int(input("Enter a number: "))

# Loop from 1 to the input_number
for current_number in range(1, input_number + 1):
    # Calculate the cube of the current number
    cube = current_number ** 3
    
    # Print the result
    print(f"Current Number is: {current_number} and the cube is {cube}")

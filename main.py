# A program to demonstrate using both 'for' and 'while' loops together

# 1. Using a for loop to iterate over a list of numbers
numbers = [1, 2, 3, 4, 5]
print("Using a 'for' loop:")
for number in numbers:
    print(f"Processing number: {number}")
    # For each number, we will use a while loop to count down from that number
    count = number  # Starting countdown from the current number
    print(f"Counting down from {count}:")
    
    # 2. Using a while loop to count down from the current number
    while count > 0:
        print(count)
        count -= 1  # Decrease the count by 1 each time

    print("Done counting down!")

print("\nAll loops completed!")

import random

def display(room):
    for row in room:
        print(' '.join(str(cell) for cell in row))
    print()

def initialize_room(size):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

def clean_room(room):
    size = len(room)
    cleaned = 0
    for x in range(size):
        for y in range(size):
            if room[x][y] == 1:
                print(f"Vacuuming location ({x}, {y}) now.")
                room[x][y] = 0
                print(f"Cleaned ({x}, {y})")
                cleaned += 1
    return cleaned

# User input for room size
try:
    size = int(input("Enter the size of the room (e.g., 4 for a 4x4 room): "))
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
    size = 4  # Default size if input is invalid

room = initialize_room(size)

print("All rooms are dirty:")
display(room)

print("Before cleaning, I detect all of these random dirts:")
display(room)

cleaned_count = clean_room(room)

# Calculate performance
total_cells = size * size
performance = 100 - (cleaned_count / total_cells * 100)

print("Room is clean now, Thanks for using : 3710933")
display(room)
print(f'Performance = {performance:.2f}%')

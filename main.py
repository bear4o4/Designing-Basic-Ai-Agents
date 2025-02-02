

#TASK 1
sensor = [True, False, True, False, True, False, True, False, True, False]
def simple_reflex_agent(input):
    if input:
        return "turn right"
    else:
        return "move forward"

for i in range(10):
    input = sensor[i]
    action = simple_reflex_agent(input)
    print(f"step {i + 1} {action}")
print("#############################################")


#TASK 2
sensor = [True, False, True, False, True, False, True, False, True, False]
def model_based_reflex_agent(sensor_history):
    if sensor_history[-1] and sensor_history[-2]:
        return "Turn Left"
    elif sensor_history[-1]:
        return "Turn Right"
    else:
        return "Move Forward"

sensor_history = []
for i in range(3):
    sensor_history.append(sensor[i])

for i in range(3, 10):
    action = model_based_reflex_agent(sensor_history)
    print(f"sensor history =  {sensor_history[-3:]} action = {action}")
    sensor_history.append(sensor[i])
print("#############################################")

#TASK 3
grid_size = 5
start_row, start_col = 1, 1
target_row, target_col = 3, 4

def goal_based_agent(row, col, target_row, target_col):
    if col < target_col:
        return "Move Right"
    elif row < target_row:
        return "Move Down"
    elif row > target_row:
        return "Move Up"
    else:
        return "Reached Target"

row, col = start_row, start_col

print(f"Starting position: ({row}, {col})")
print(f"Target position: ({target_row}, {target_col})")

while (row, col) != (target_row, target_col):
    action = goal_based_agent(row, col, target_row, target_col)

    if action == "Move Right":
        col += 1
    elif action == "Move Down":
        row += 1
    elif action == "Move Up":
        row -= 1

    print(f"Position = ({row}, {col}), Action = {action}")

if (row, col) == (target_row, target_col):
    print(f"Target reached at Position = ({row}, {col})")
else:
    print(f"Target not reached. Final Position = ({row}, {col})")
print("#############################################")



#TASK 4
grid_size = 5
move_closer = 10
move_away = -5
target_reached = 50

def calculate_distance(row1, col1, row2, col2):
    return abs(row1 - col2) + abs(col1 - col2)

def utility_based_agent(row, col, target_row, target_col):
    actions = [
        ("Move Right", row, col + 1),
        ("Move Up", row - 1, col),
        ("Move Down", row + 1, col)
    ]

    best_action = None
    highest_utility = float('-inf')

    for action, new_row, new_col in actions:
        if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
            if (new_row, new_col) == (target_row, target_col):
                utility = target_reached
            else:
                current_distance = calculate_distance(row, col, target_row, target_col)
                new_distance = calculate_distance(new_row, new_col, target_row, target_col)
                if new_distance < current_distance:
                    utility = move_closer
                else:
                    utility = move_away

            if utility > highest_utility:
                highest_utility = utility
                best_action = action

    return best_action, highest_utility

start_row, start_col = 1, 1
target_row, target_col = 4, 3
row, col = start_row, start_col
total_utility = 0
steps = 0

print(f"Starting Position: ({row}, {col})")
print(f"Target Position: ({target_row}, {target_col})")

while (row, col) != (target_row, target_col) and steps < 10:
    action, utility = utility_based_agent(row, col, target_row, target_col)
    if action == "Move Right":
        col += 1
    elif action == "Move Up":
        row -= 1
    elif action == "Move Down":
        row += 1
    print(f" Position = ({row}, {col}), Action = {action}, Utility = {utility}")
    total_utility += utility
    steps += 1

if (row, col) == (target_row, target_col):
    print(f"Target reached at step {steps}: Position = ({row}, {col})")
else:
    print(f"Target not reached within 10 steps: Final Position = ({row}, {col})")

print(f"Total Utility: {total_utility}")

print("#############################################")

#TASK 5

grid_size = 5
move_closer = 10
move_away = -5
target_reached = 50

def calculate_distance(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)

def utility_based_agent(row, col, target_row, target_col, visited_cells):
    actions = [
        ("Move Right", row, col + 1),
        ("Move Up", row - 1, col),
        ("Move Down", row + 1, col)
    ]

    best_action = None
    highest_utility = float('-inf')

    for action, new_row, new_col in actions:
        if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
            if (new_row, new_col) in visited_cells and visited_cells[(new_row, new_col)] < 0:
                continue
            if (new_row, new_col) == (target_row, target_col):
                utility = target_reached
            else:
                current_distance = calculate_distance(row, col, target_row, target_col)
                new_distance = calculate_distance(new_row, new_col, target_row, target_col)
                if new_distance < current_distance:
                    utility = move_closer
                else:
                    utility = move_away

            if utility > highest_utility:
                highest_utility = utility
                best_action = action

    return best_action, highest_utility

start_row, start_col = 1, 1
target_row, target_col = 4, 3
row, col = start_row, start_col
total_utility = 0
steps = 0
visited_cells = {}

print(f"Starting Position: ({row}, {col})")
print(f"Target Position: ({target_row}, {target_col})")

while (row, col) != (target_row, target_col) and steps < 10:
    action, utility = utility_based_agent(row, col, target_row, target_col, visited_cells)
    if action == "Move Right":
        col += 1
    elif action == "Move Up":
        row -= 1
    elif action == "Move Down":
        row += 1

    print(f"Position = ({row}, {col}), Action = {action}, Utility = {utility}")
    visited_cells[(row, col)] = utility
    total_utility += utility
    steps += 1

if (row, col) == (target_row, target_col):
    print(f"Target reached at step {steps}: Position = ({row}, {col})")
else:
    print(f"Target not reached within 10 steps: Final Position = ({row}, {col})")

print(f"Total Utility: {total_utility}")
print(f"Visited Cells: {visited_cells}")
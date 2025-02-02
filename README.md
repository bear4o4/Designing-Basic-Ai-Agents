# Designing-Basic-Ai-Agents


# T.1: Simple Reflex Agent
Scenario: A robot in a warehouse needs to move along a straight path while avoiding obstacles.
Task:
Implement a simple reflex agent with the following condition:
If an obstacle is detected (sensor_input = True), turn right.
If no obstacle (sensor_input = False), move forward.
Simulate the agent’s movement for 10 steps with random obstacle inputs (True or False). Use a loop and if-else statements.

# T.2: Model-Based Reflex Agent
Scenario: The robot now remembers previously encountered obstacles to make better decisions.
Task:
Extend the agent to:
Keep track of the last 3 sensor readings in a list (e.g., [True, False, False]).
If the last two readings were obstacles (True), turn left instead of right.
Simulate the agent’s movement for 10 steps using random sensor user inputs and memory tracking.

# T.3: Goal-Based Agent
Scenario: The robot now has a specific goal: reach a target cell in a 5x5 grid warehouse.
Task:
Place the robot at a random starting position (x, y) and a target at (target_x, target_y).
Allow the robot to take one of three actions:
Move up, move down, or move right (restrict actions to simplify the grid exploration).
Design logic to calculate the distance to the target and prioritize moves that reduce the distance. For example:
If the robot is below the target, move up.
If the robot is left of the target, move right.
Stop when the robot reaches the target.

# T.4: Utility-Based Agent
Scenario: The robot now assigns utility values to its actions to make better decisions in achieving its goal.
Task:
Assign utilities to each action:
Moving closer to the target: +10.
Moving away: -5.
Reaching the target: +50.
Simulate the agent navigating the 5x5 grid for up to 10 steps. At each step:
Calculate the utility of each possible action.
Choose the action with the highest utility.
Print the agent’s path, total utility, and whether the target was reached.

# T.5: Learning Agent
Scenario: The robot now learns from its actions to improve future navigation.
Task:
Extend the utility-based agent:
Keep a record of visited cells.
Avoid cells that resulted in negative utility previously.
Simulate the robot's navigation in the grid:
Print the path, visited cells, and adjustments based on learned behavior.

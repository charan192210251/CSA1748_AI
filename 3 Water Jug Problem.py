from collections import defaultdict

def waterJugSolver(jug1, jug2, aim, amt1, amt2, visited):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    if not visited[(amt1, amt2)]:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        return (waterJugSolver(jug1, jug2, aim, 0, amt2, visited) or
                waterJugSolver(jug1, jug2, aim, amt1, 0, visited) or
                waterJugSolver(jug1, jug2, aim, jug1, amt2, visited) or
                waterJugSolver(jug1, jug2, aim, amt1, jug2, visited) or
                waterJugSolver(jug1, jug2, aim,
                               amt1 + min(amt2, (jug1 - amt1)),
                               amt2 - min(amt2, (jug1 - amt1)),
                               visited) or
                waterJugSolver(jug1, jug2, aim,
                               amt1 - min(amt1, (jug2 - amt2)),
                               amt2 + min(amt1, (jug2 - amt2)),
                               visited))
    else:
        return False

def user_input():
    jug1 = int(input("Enter the capacity of the first jug: "))
    jug2 = int(input("Enter the capacity of the second jug: "))
    aim = int(input("Enter the target amount: "))

    visited = defaultdict(lambda: False)
    print("Steps: ")
    waterJugSolver(jug1, jug2, aim, 0, 0, visited)

# Call the function to take user input and solve the problem
user_input()

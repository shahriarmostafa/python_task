

def get_state(room_name):
    """Ask the user for the state of a room until a valid answer is given."""
    while True:
        state = input("Enter the state of Room " + room_name + " (Clean/Dirty): ").strip().capitalize()
        if state in ("Clean", "Dirty"):
            return state
        print("Invalid input! Please type Clean or Dirty.")


def get_location():
    """Ask the user for the starting location of the agent."""
    while True:
        location = input("Enter the current location of the vacuum agent (A/B): ").strip().upper()
        if location in ("A", "B"):
            return location
        print("Invalid input! Please type A or B.")


rooms = {}
rooms["A"] = get_state("A")
rooms["B"] = get_state("B")
location = get_location()

print("\nInitial state -> Room A:", rooms["A"], "| Room B:", rooms["B"])
print("Agent starts in Room", location)
print("\n--- Agent Actions ---")

step = 0
cost = 0  

while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":
    step = step + 1

    if rooms[location] == "Dirty":
        print("Step", step, ": Room", location, "is Dirty -> Action: SUCK (cleaning Room " + location + ")")
        rooms[location] = "Clean"
        cost = cost + 1
    else:
        if location == "A":
            print("Step", step, ": Room A is Clean -> Action: MOVE RIGHT (going to Room B)")
            location = "B"
        else:
            print("Step", step, ": Room B is Clean -> Action: MOVE LEFT (going to Room A)")
            location = "A"
        cost = cost + 1

print("Step", step + 1, ": Both rooms are Clean -> Action: NoOp (agent stops)")

print("--- Final Result ---")
print("Room A :", rooms["A"])
print("Room B :", rooms["B"])
print("Agent final location :", location)
print("Total actions performed :", cost)

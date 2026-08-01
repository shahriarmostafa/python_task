

def simple_reflex_agent(percept):
    print("Perception Received: " + str(percept))
    location, status = percept

    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Right"
    return "Left"


def simulate():
    rooms = {
        "A": input("Enter the state of Room A (Clean/Dirty): ").strip().capitalize(),
        "B": input("Enter the state of Room B (Clean/Dirty): ").strip().capitalize(),
    }
    location = input("Enter the current location of the agent (A/B): ").strip().upper()

    print("Initial State: " + str(rooms))
    print("Agent starts in Room " + location)

    while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":
        action = simple_reflex_agent((location, rooms[location]))
        print("Action Performed: " + action)

        if action == "Suck":
            rooms[location] = "Clean"
        elif action == "Right":
            location = "B"
        else:
            location = "A"

    print("Action Performed: NoOp (both rooms are Clean)")
    print("Final State -> Room A: " + rooms["A"] + ", Room B: " + rooms["B"])
    print("Agent final location: Room " + location)


if __name__ == "__main__":
    simulate()

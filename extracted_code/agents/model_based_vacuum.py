"""Model-based two-room vacuum agent and interactive simulation."""

import random

model = {"A": "Unknown", "B": "Unknown"}
world_state = "Bad"
action = "Unknown"


def update_state(previous_action, percept):
    global world_state

    location, status = percept
    model[location] = status

    if previous_action == "Suck":
        model[location] = "Clean"

    world_state = (
        "Good" if model["A"] == "Clean" and model["B"] == "Clean" else "Bad"
    )
    return world_state


def model_based_reflex_agent(percept):
    global action

    location, status = percept
    if world_state == "Good":
        action = "Pause"
        return action
    if status == "Dirty":
        action = "Suck"
    elif location == "A":
        action = "Right"
    else:
        action = "Left"

    update_state(action, percept)
    print("Perception: " + str(percept))
    print("Action Performed: " + action)
    print("Model: " + str(model))
    print("State: " + world_state)
    return action


def reset_agent():
    global model, world_state, action
    model = {"A": "Unknown", "B": "Unknown"}
    world_state = "Bad"
    action = "Unknown"


def simulate():
    location = random.choice(["A", "B"])
    condition = random.choice(["Clean", "Dirty"])

    while True:
        print("*****")
        next_action = model_based_reflex_agent((location, condition))

        if next_action == "Right":
            location = "B"
            condition = random.choice(["Clean", "Dirty"])
        elif next_action == "Left":
            location = "A"
            condition = random.choice(["Clean", "Dirty"])
        elif next_action == "Suck":
            condition = "Clean"
        elif next_action == "Pause":
            if input("Stopped. Do restart? (yes/no): ") != "yes":
                break
            location = random.choice(["A", "B"])
            condition = random.choice(["Clean", "Dirty"])
            reset_agent()


if __name__ == "__main__":
    simulate()

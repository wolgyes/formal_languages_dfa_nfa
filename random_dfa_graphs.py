import json
import random

def generate_dfa_json(name="dfa_test"):
    num_states = random.randint(2, 5)
    states = [f"q{i}" for i in range(num_states)]

    alphabet = random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(2, 5))

    transitions = []
    for state in states:
        for symbol in alphabet:
            to_state = random.choice(states)
            transitions.append({"from": state, "symbol": symbol, "to": to_state})

    start_state = random.choice(states)
    num_accept_states = random.randint(1, len(states))
    accept_states = random.sample(states, num_accept_states)

    dfa = {
        "name": name,
        "states": states,
        "alphabet": alphabet,
        "transitions": transitions,
        "start_state": start_state,
        "accept_states": accept_states,
        "test_words": ["test", "cica", "mica", "macska"]
    }

    return dfa

def main():
    num_jsons = 3

    for i in range(num_jsons):
        dfa = generate_dfa_json(name=f"dfa_{i}")
        with open(f"dfa_{i}.json", "w") as json_file:
            json.dump(dfa, json_file, indent=4)
        print(f"Generated DFA JSON: dfa_{i}.json")

if __name__ == "__main__":
    main()
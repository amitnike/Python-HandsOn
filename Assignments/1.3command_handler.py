#!/usr/bin/env python3
# command_handler.py - Accepts user commands and responds using match-case.
# Valid commands: start, stop, exit

def handle_command(command):
    """Process a command string using a match-case statement."""
    match command:
        case "start":
            print("System started. Everything is up and running.")

        case "stop":
            print("System stopped. All processes have been halted.")

        case "exit":
            print("Exiting program. Goodbye!")
            return False  # Signal the loop to stop

        case _:
            # Default case: catches any unrecognized input
            print(f"Unrecognized command: '{command}'. Valid commands are: start, stop, exit.")

    return True  # Continue the loop


# --- Main loop ---

print("Command Handler — type a command to get started.")
print("Valid commands: start | stop | exit\n")

while True:
    # Prompt the user and normalize input to lowercase
    user_input = input("Enter command: ").strip().lower()

    # Pass the command to the handler; stop looping if it returns False
    if not handle_command(user_input):
        break

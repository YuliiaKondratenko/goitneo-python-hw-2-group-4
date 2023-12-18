def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Incorrect input. Please check your command format."
    return inner
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact '{name}' updated."
@input_error
def get_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts.get(name)
@input_error
def list_all_contacts(contacts):
    if not contacts:
        return "No contacts saved."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(list_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

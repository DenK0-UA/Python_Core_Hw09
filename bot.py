def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid input. Please try again."
        except IndexError:
            return "Invalid command. Please try again."
    return wrapper

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added successfully"

@input_error
def change_phone(name, phone):
    contacts[name] = phone
    return "Phone number updated successfully"

@input_error
def get_phone(name):
    return contacts[name]

def show_all_contacts():
    if not contacts:
        return "No contacts found"
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid input. Please enter name and phone number separated by a space.")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                print(change_phone(name, phone))
            except ValueError:
                print("Invalid input. Please enter name and phone number separated by a space.")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(get_phone(name))
            except ValueError:
                print("Invalid input. Please enter a name.")
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
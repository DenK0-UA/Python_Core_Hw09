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
        except TypeError:
            return "Invalid number of arguments passed"
        except KeyboardInterrupt:
            return "See you next time"
    return wrapper


contacts = {}


@input_error
def hello():
    return "How can I help you?"


@input_error
def add_contact(name, phone):
    if name in contacts:
        return "Contact already exists. Use the 'change' command to modify the phone number."
    contacts[name] = phone
    return "Contact added successfully"


@input_error
def change_contact(name, phone):
    if name not in contacts:
        return "Contact not found. Use the 'add' command to add a new contact."
    contacts[name] = phone
    return "Phone number updated successfully"


@input_error
def phone_contact(name):
    return contacts[name]


@input_error
def show_all_contacts():
    if not contacts:
        return "No contacts found"
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


@input_error
def good_bye():
    return "Good bye!"


COMMAND = {
    "hello": hello,
    "add": add_contact,
    "change": change_contact,
    "phone": phone_contact,
    "show_all": show_all_contacts,
    "exit": good_bye
}


@input_error
def process_command(command):
    command_parts = command.split(maxsplit=1)
    cmd = command_parts[0].lower()
    args = command_parts[1] if len(command_parts) > 1 else None
    func = COMMAND.get(cmd)
    if func:
        if args:
            print(func(*args.split()))
        else:
            print(func())
    else:
        print("Invalid command. Please try again.")


@input_error
def main():
    while True:
        user_input = input("Enter command: ").lower()
        if user_input in ("good bye", "close", "exit"):
            print(COMMAND["exit"]())
            break
        else:
            process_command(user_input)


if __name__ == "__main__":
    main()

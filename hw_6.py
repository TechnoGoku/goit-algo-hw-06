from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('Value error')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        # Phone('0951111111') == '0951111111'
        self.phones = [p for p in self.phones if str(p) != phone_number]

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if result is None: 
                    return "Contact not found."
                return result
            except KeyError:
                return "Contact not found."
            except ValueError:
                return "Give me name and phone please"
            except IndexError:
                return "Enter the argument for the command."
        return inner
    
    def parse_input(user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    
    @input_error
    def add_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    
    @input_error
    def change_contact(args, contacts):
        name, phone = args
        if name not in contacts:
            raise ValueError("Contact does not exist.")
        contacts[name] = phone
        return "Contact updated successfully"
    
    @input_error
    def show_contact(args, contacts):
        name = args[0]
        if name in contacts:
            return contacts[name]
        
    def all_contacts(contacts):
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

    def main():
        contacts = {}
        print("Welcome to the assistant bot!")
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "show":
                print(show_contact(args, contacts))   
            elif command == "all": 
                all_contacts(contacts)             
            else:
                print("Invalid command.")
            

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        # Put your logic here
        pass
# Add a dog
# - max of 25
# - name can't be duplicate
# Update a dog (not now)
# Remove a dog
# - remove by name
# Exit
dogs = []


def read_required_string(prompt):
    value = ""
    while not value:
        value = input(prompt).strip()
        if not value:
            print("Error: value is required.")
    return value


def add_dog():
    print("Add a dog")

    if len(dogs) >= 25:
        print("Error: too many dogs")
        return

    name = read_required_string("Dog's name?: ")
    while name in dogs:
        print("Error: duplicate name. Please refine by last or middle name.")
        name = read_required_string("Dog's name?: ")
    dogs.append(name)


def display_dogs():
    print("Dogs:")

    if len(dogs) <= 0:
        print("No dogs found.")

    for index, name in enumerate(dogs):
        print(f"{index + 1}. {name}")


def remove_dog():
    print("Remove a dog")
    name = read_required_string("Dog's name?: ")
    if name in dogs:
        dogs.remove(name)
        print(f"{name} removed, success!")
    else:
        print("Dog not found.")


def run():
    print("Cur-ious Hounds")
    print("")
    option = ""
    while option != "0":
        print("Main Menu")
        print("0. Exit")
        print("1. Add a dog")
        print("2. Display dogs")
        print("3. Remove a dog")
        option = read_required_string("Select [0-3]: ")
        if option == "0":
            print("Goodbye.")
        elif option == "1":
            add_dog()
        elif option == "2":
            display_dogs()
        elif option == "3":
            remove_dog()
        else:
            print("I don't understand that command.")


if __name__ == "__main__":
    run()
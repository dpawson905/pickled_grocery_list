import sys
import os
import pickle
import shelve
import progressbar
import time

grocery_list = []

print("""\n            --------------------
Hello, welcome to your Grocery List application
            --------------------\n""")


def add_progress_bar():
    bar = progressbar.ProgressBar()

    for i in bar(range(100)):
        time.sleep(0.02)
        bar.update(i)


def invalid_selection():
    print("That is an invalid selection... Please try again!")
    main()


def print_list():
    grocery_list = pickle.load(open("groc.pkldb", "rb"))

    for index, value in enumerate(grocery_list, 1):
        print("{}. {}".format(index, value))


def view_list():
    print("Loading your list")
    add_progress_bar()
    print("\nHere is your list!")
    print_list()
    selection = input("Would you like to do anything else? (y/n): ").lower()
    if selection == "y" or selection == "yes":
        selection = input("What would you like to do? (A)dd item, (D)elete list or (Q)uit application").lower()
        if selection == "a":
            add_to_list()
        elif selection == "d":
            delete_list()
        elif selection == "q":
            quit_application()
        else:
            invalid_selection()
    elif selection == "n" or selection == "no":
        quit_application()
    else:
        invalid_selection()


def add_to_list():
    print("Opening your grocery list...")
    add_progress_bar()
    list_file = "groc.pkldb"

    grocery_list = []

    if os.path.exists(list_file):
        with open(list_file, "rb") as rfp:
            grocery_list = pickle.load(rfp)

    item_add = input("What would you like to add to your list?: ")

    grocery_list.append(item_add)

    with open(list_file, "wb") as wfp:
        pickle.dump(grocery_list, wfp)

    with open(list_file, "rb") as rfp:
        grocery_list = pickle.load(rfp)

    print(f"Adding {item_add} to your list")
    add_progress_bar()

    selection = input("Would you like to view your list? (y/n): ").lower()
    if selection == "y" or selection == "yes":
        view_list()
    else:
        selection = input(
            "What would you like to do then... (A)dd another item or (Q)uit: ").lower()
        if selection == "a":
            add_to_list()
        elif selection == "q":
            quit_application()
        else:
            invalid_selection()


def delete_list():
    print("Please wait while your grocery list is deleted...")
    add_progress_bar()
    os.remove("groc.pkldb")
    selection = input(
        "Grocery list deleted... Would you like to make a new list? (y/n): ").lower()
    if selection == "y" or selection == "yes":
        add_to_list()
    elif selection == "n" or selection == "no":
        quit_application()
    else:
        invalid_selection()


def quit_application():
    print("Good bye!")
    sys.exit(0)


def main():
    action = input("""What are you wanting to do?
(V)iew list...
(A)dd to list...
(D)elete list...
(Q)uit Application...
Please select an option: """).lower()

    if action == "v":
        view_list()
    elif action == "a":
        add_to_list()
    elif action == "d":
        delete_list()
    elif action == "q":
        quit_application()
    else:
        invalid_selection()


if __name__ == "__main__":
    main()

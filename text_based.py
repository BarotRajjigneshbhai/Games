import time

def intro():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious forest...")
    time.sleep(2)
    print("You see two paths ahead. One leads to a dark cave, and the other to a hidden garden.")
    time.sleep(2)

def choose_path():
    print("Which path will you choose?")
    print("1. Explore the dark cave")
    print("2. Enter the hidden garden")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def explore_cave():
    print("You enter the dark cave and hear strange noises...")
    time.sleep(2)
    print("You find a treasure chest!")
    time.sleep(2)
    print("Congratulations! You have found the hidden treasure.")

def enter_garden():
    print("You enter the hidden garden and are surrounded by beautiful flowers.")
    time.sleep(2)
    print("You see a mysterious statue in the center of the garden.")
    time.sleep(2)
    print("Suddenly, the statue comes to life!")
    time.sleep(2)
    print("You engage in a friendly conversation with the statue and learn valuable secrets.")
    time.sleep(2)
    print("You feel enlightened.")

def main():
    intro()
    choice = choose_path()
    
    if choice == '1':
        explore_cave()
    elif choice == '2':
        enter_garden()
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()

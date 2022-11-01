while True:
    print("\nSelect an option from the menu ")
    print("1. Add Recipe")
    print("2. View all recipes")
    print("3. Search a recipe")
    print("4. Update a recipe")
    print("5. Delete recipe")
    print("6.exit\n")

    choice = int(input("Enter an option: "))
    if(choice == 1):
        print("Recipe data insertion")
    elif(choice == 2):
        print("View Recipe")
    elif(choice == 3):
        print("Searching a Recipe")
    elif (choice == 4):
        print("update Recipe")
    elif(choice == 5):
        print("delete a Recipe")
    elif(choice==6):
        break
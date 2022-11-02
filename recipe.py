import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'recipedb')

mycursor = mydb.cursor()


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

        rtitle = input("Enter recipe name: ")
        rdesc = input("Enter recipe description: ")
        rpreparedby = input("Recipe prepared by: ")
        ringredients = input("Enter the ingredients: ")
        rcategory = input("Enter the recipe category: ")

        sql = 'INSERT INTO `recipes`(`title`, `description`, `preparedby`, `ingredients`, `recipecategory`) VALUES(%s,%s,%s,%s,%s)'
        data = (rtitle,rdesc,rpreparedby,ringredients,rcategory)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Recipe's data inserted successfully.")

    elif(choice == 2):
        print("View Recipe")
        sql = "SELECT * FROM `recipes`"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice == 3):
        print("Searching a Recipe")
    elif (choice == 4):
        print("update Recipe")
    elif(choice == 5):
        print("delete a Recipe")
    elif(choice==6):
        break
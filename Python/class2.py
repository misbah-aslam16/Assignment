# ============================================================
#   CLASS 2 — HOMEWORK QUESTIONS
#   Dictionaries, Input & String Handling
#   Total Questions: 10
# ============================================================
#   Instructions:
#     - Write your answer below each question.
#     - Do NOT delete the question comments.
#     - Run your code after each question to test it.
#     - Use only what was covered in Class 1 & Class 2.
# ============================================================


# ─────────────────────────────────────────────
# QUESTION 1 — String Methods
# ─────────────────────────────────────────────
# Ask the user to enter a sentence.
# Then print the following:
#   1. The sentence in ALL UPPERCASE
#   2. The sentence in all lowercase
#   3. The total number of characters (including spaces)
#   4. How many times the letter 'a' appears (uppercase or lowercase)
#   5. The sentence with every space replaced by a dash ( - )
#
# Example (if user enters "I love Python"):
#   UPPERCASE  : I LOVE PYTHON
#   lowercase  : i love python
#   Length     : 13
#   Letter 'a' : 0
#   Dashes     : I-love-Python

# Write your code below:

# text = input("Enter any sentence: ")
# split_text =  text.split (' ')
# joined = "-".join(split_text)
# print("UPPERCASE", text.upper())        
# print("lowercase", text.lower())         
# print("Length ", (len(text)))   
# print("Letter 'a'", text.find("a")) 
# print(split_text) 
# print("Dashes", joined)

# ─────────────────────────────────────────────
# QUESTION 2 — String Slicing
# ─────────────────────────────────────────────
# Ask the user to enter any word.
# Then print:
#   1. The first 3 characters
#   2. The last 3 characters
#   3. The word reversed
#   4. Every other character (characters at index 0, 2, 4, 6, ...)
#
# Example (if user enters "elephant"):
#   First 3     : ele
#   Last 3      : ant
#   Reversed    : tnahpele
#   Every other : eepat

# Write your code below:

# word = input("Enter any word: ")
# print(word[0:3]) 
# print(word[-3:])  
# print(word[::-1]) 
# print(word[::2])

# ─────────────────────────────────────────────
# QUESTION 3 — f-strings & Formatting
# ─────────────────────────────────────────────
# Write a program that works like a simple invoice generator:
#   1. Ask the user for: item name, quantity, unit price
#   2. Calculate: subtotal = quantity × unit price
#   3. Calculate: tax = subtotal × 13%
#   4. Calculate: grand total = subtotal + tax
#
# Print a neatly formatted invoice like this:
# ─────────────────────────────
#   INVOICE
# ─────────────────────────────
#   Item        : Notebook
#   Quantity    : 3
#   Unit Price  : Rs. 120.00
#   Subtotal    : Rs. 360.00
#   Tax (13%)   : Rs. 46.80
#   Grand Total : Rs. 406.80
# ─────────────────────────────
# (Use f-strings and :.2f to show exactly 2 decimal places)

# Write your code below:

# name = input("Enter item name: ")
# quantity = int(input("Enter item quantity: "))
# price = int(input("Enter item price: "))
# subtotal = price * quantity
# tax = subtotal * 0.13
# total = subtotal + tax

# print("Item  :", name)
# print("Quantity  :", quantity)
# print("Unit Price  :", price)
# print("Subtotal  :" , subtotal)
# print("Tax (13%)  :", tax)
# print("Grand Total  :", total)

# ─────────────────────────────────────────────
# QUESTION 4 — Creating & Accessing Dictionaries
# ─────────────────────────────────────────────
# Create a dictionary for a mobile phone with these keys:
#   brand, model, storage_gb, ram_gb, price, in_stock
#   (in_stock should be True or False)
#
# Then print:
#   1. The brand and model on one line.
#   2. The storage and RAM on one line.
#   3. A message: "Available" if in_stock is True,
#                 "Out of Stock" if in_stock is False.
#
# Example output:
#   Phone   : Samsung Galaxy S24
#   Storage : 256 GB | RAM: 8 GB
#   Status  : Available

# Write your code below:

# brand = input("Enter mobile brand: ")
# model = input("Enter model: ")
# storage_gb = input("Enter storage: ")
# ram_gb = input("Enter ram : ")
# price = input("Enter price: ")
# in_stock = input("In stock? true or false: ")

# print(f"Phone:  {brand} | {model}")
# print(f"Storage:  {storage_gb} | {ram_gb}")

# if in_stock.lower() == "true":
#     print("Available")
# else:
#     print("Out of Stock")


# ─────────────────────────────────────────────
# QUESTION 5 — Dictionary Operations
# ─────────────────────────────────────────────
# Start with this dictionary of a student:
student = {
    "name": "Sara",
    "age": 19,
    "course": "Computer Science"
}
#
# Perform the following steps IN ORDER and print the
# dictionary after EACH step:
#
#   Step 1: Add a new key "gpa" with value 3.7
#   Step 2: Update "age" to 20
#   Step 3: Add a new key "year" with value 2
#   Step 4: Delete the key "course"
#   Step 5: Print the final number of keys in the dictionary

# Write your code below:

# student["gpa"] = 3.7
# student["age"] = 20
# student["year"] = 2
# del student["course"]
# print(student)
# print(len(student))             


# ─────────────────────────────────────────────
# QUESTION 6 — Looping Through a Dictionary
# ─────────────────────────────────────────────
# You are given this dictionary of country capitals:
capitals = {
    "Pakistan": "Islamabad",
    "Turkey": "Ankara",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Brazil": "Brasilia"
}
#
# Write a program that:
#   1. Prints all countries and their capitals in this format:
#        The capital of Pakistan is Islamabad.
#        The capital of Turkey is Ankara.
#        (and so on for all countries)
#
#   2. Asks the user to type a country name.
#      If it exists in the dictionary, print its capital.
#      If not, print "That country is not in our list."

# Write your code below:

# capitals = {
#     "pakistan": "Islamabad",
#     "turkey": "Ankara",
#     "france": "Paris",
#     "japan": "Tokyo"
# }

# for item in capitals:
#     print(f"The capital of {item.title()} is {capitals[item]}.")

# country = input("Type any country name: ").lower()

# if country in capitals:
#     print(f"The capital of {country.title()} is {capitals[country]}.")
# else:
#     print("That country is not in our list.")


# ─────────────────────────────────────────────
# QUESTION 7 — Nested Dictionary
# ─────────────────────────────────────────────
# Create a nested dictionary called 'library' with
# at least 3 books. Each book should have:
#   - title
#   - author
#   - year
#   - available (True / False)
#
# Structure example:
#   library = {
#       "book1": { "title": "...", "author": "...", ... },
#       ...
#   }
#

# Then:
#   1. Loop through all books and print their title and author.
#   2. Print only the books that are currently available.

# Write your code below:

# library = {
#       "book1": { "title": "Science", "author": "Misbah","year":"2034","available":"true" },

#       "book2": { "title": "Math", "author": "Misbah","year":"2034","available":"false" },

#       "book3": { "title": "English", "author": "Misbah","year":"2034","available":"true" },

#       "book4": { "title": "Urdu", "author": "Misbah","year":"2034","available":"false" },

#       "book5": { "title": "Islamiat", "author": "Misbah","year":"2034","available":"false" }

#   }
# for book in library:
#     # print("title",library[book]["title"],"and author ",library[book]["author"])
#     if library[book]["available"].lower() == "true".lower():
#         print(library[book])
#     else:
#         print("Not Available")
    



# ─────────────────────────────────────────────
# QUESTION 8 — String Split & Dictionary
# ─────────────────────────────────────────────
# Ask the user to enter the names of 3 students and their
# marks, one per line in this exact format:
#   Ali 85
#   Sara 92
#   Ahmed 78
#
# After all three are entered:
#   1. Store each student's name and mark in a dictionary.
#   2. Print all names and marks.
#   3. Print the name and mark of the student with the highest score.
#
# Hint: use .split() to separate the name from the mark.

# Write your code below:

# students = {}

# for i in range(3):
#     data = input("Enter name and mark: ").split()
#     name = data[0]
#     mark = int(data[1])
#     students[name] = mark

# print("\nNames and Marks:")
# for name, mark in students.items():
#     print(name, mark)

# print("Maximum marks", max(students.values()))

# ─────────────────────────────────────────────
# QUESTION 9 — Word Frequency Counter
# ─────────────────────────────────────────────
# Ask the user to enter a sentence (e.g. "the cat sat on the mat").
# Write a program that counts how many times each word appears
# and stores the result in a dictionary.
#
# Rules:
#   - Treat uppercase and lowercase as the same word
#     ("The" and "the" should both count as "the")
#   - Print the words and their counts, one per line.
#
# Example input : "the cat sat on the mat the cat"
# Example output:
#   the : 3
#   cat : 2
#   sat : 1
#   on  : 1
#   mat : 1
#
# Hint: use .split() and a for loop.

# Write your code below:




# ─────────────────────────────────────────────
# QUESTION 10 — Full Mini Project (Putting it all together)
# ─────────────────────────────────────────────
# Build a simple EXPENSE TRACKER using a while loop and dictionary.
#
# The program should:
#   1. Show a menu with these options:
#        1. Add Expense
#        2. View All Expenses
#        3. View Total Spent
#        4. Delete an Expense
#        5. Exit
#
#   2. For option 1: ask for category (e.g. Food, Transport)
#      and amount, then save to the dictionary.
#      (category = key, amount = value)
#
#   3. For option 2: print all categories and their amounts.
#
#   4. For option 3: print the sum of all expense amounts.
#
#   5. For option 4: ask for the category name and remove it.
#
#   6. For option 5: print "Goodbye!" and exit the loop.
#
# Sample run:
#   1. Add Expense   → Food: 500
#   1. Add Expense   → Transport: 200
#   2. View All      → Food: Rs.500  |  Transport: Rs.200
#   3. Total Spent   → Total: Rs.700
#   4. Delete        → Food deleted
#   5. Exit          → Goodbye!

# Write your code below:




# ============================================================
#   END OF CLASS 2 HOMEWORK
#   Submit your completed file to your instructor.
# ============================================================
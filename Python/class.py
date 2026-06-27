import random;
# ─────────────────────────────────────────────
# QUESTION 2 — Arithmetic Operations
# ─────────────────────────────────────────────
# A shopkeeper sells 3 items:
#   - Rice bag    → Rs. 350
#   - Cooking oil → Rs. 480
#   - Sugar bag   → Rs. 120
#
# Write a program that:
#   1. Stores each price in a variable.
#   2. Calculates the total cost.
#   3. Calculates a 10% discount on the total.
#   4. Calculates the final price after the discount.
#   5. Prints the total, discount amount, and final price.

# rice_price =  350 
# oil_price = 480
# sugar_price = 120

# total_cost = rice_price + oil_price  + sugar_price
# print( "Total Price", total_cost)

# discount_price =  total_cost * 0.10 
# print( "Discount Price", discount_price)

# final_price =  total_cost - discount_price
# print( "Final Price", final_price)


# ─────────────────────────────────────────────
# QUESTION 3 — Type Conversion & Input
# ─────────────────────────────────────────────
# Write a program that:
#   1. Asks the user to enter their birth year.
#   2. Calculates their approximate age (use current year = 2024).
#   3. Prints: "You are approximately X years old."
#
# Remember: input() returns a string — convert it to int first!

# birth_year = int(input("Enter your birth year:"))
# year_count = 2024 - birth_year
# print("You are approximately " + str(year_count) + " years old.")

# ─────────────────────────────────────────────
# QUESTION 4 — if / elif / else
# ─────────────────────────────────────────────
# Write a program that asks the user to enter the current temperature
# (in Celsius) and then prints a clothing suggestion:
#
#   temperature > 35  → "It's very hot! Wear light clothes."
#   temperature 25-35 → "It's warm. A t-shirt is fine."
#   temperature 15-24 → "It's a bit cool. Consider a jacket."
#   temperature < 15  → "It's cold! Wear a warm coat."

# current_temp = int(input("Enter current temperature: "))
# if current_temp > 35:
#  print("It's very hot! Wear light clothes.")
# elif current_temp >= 25:
#  print("It's warm. A t-shirt is fine.")
# elif current_temp >= 15:
#  print("It's a bit cool. Consider a jacket.")
# elif current_temp < 15:
#  print("It's cold! Wear a warm coat.")
# else:
#   print("sorry!")

# ─────────────────────────────────────────────
# QUESTION 5 — if / elif / else (Grade Calculator)
# ─────────────────────────────────────────────
# Write a program that:
#   1. Asks the user to enter marks out of 100.
#   2. Prints the grade based on these rules:
#        90 – 100  → Grade A  (Excellent)
#        75 –  89  → Grade B  (Good)
#        60 –  74  → Grade C  (Average)
#        50 –  59  → Grade D  (Below Average)
#         0 –  49  → Grade F  (Fail)
#   3. Also print "Congratulations!" if the student passed (marks >= 50).
#      Print "Better luck next time." if the student failed.

# marks = int(input("Enter your marks out of 100: "))

# if marks >= 50:
#     print("Congratulations!")
# else :
#     print("Better luck next time.")

# if marks >= 90:
#     print("Grade: A, Excellent")           
# elif marks >= 75:
#     print("Grade: B, Good") 
# elif marks >= 60:
#     print("Grade: C,  Average")    
# elif marks >= 60:
#     print("Grade: D, Below Average") 
# elif marks >= 0:
#     print("Grade: F, Fail") 
# else:
#     print("Invalid Number")

# ─────────────────────────────────────────────
# QUESTION 6 — for Loop
# ─────────────────────────────────────────────
# Write a program that prints the multiplication table
# for any number entered by the user.
#
# Example output (if user enters 7):
#   7 x 1  =  7
#   7 x 2  = 14
#   7 x 3  = 21
#   ...
#   7 x 10 = 70

# num = int(input("Enter any number "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# ─────────────────────────────────────────────
# QUESTION 7 — for Loop + List
# ─────────────────────────────────────────────
# You are given this list of exam scores:
#   scores = [72, 88, 45, 95, 60, 53, 78, 91, 40, 85]
#
# Write a program that loops through the list and:
#   1. Prints each score.
#   2. Prints "Pass" next to the score if it is >= 50.
#      Prints "Fail" next to the score if it is < 50.
#
# Example output:
#   72 → Pass
#   88 → Pass
#   45 → Fail
#   ...

# scores = [72, 88, 45, 95, 60, 53, 78, 91, 40, 85]

# for score in scores:
#      if score >= 50:
#          print(score, "→ Pass")
#      else:
#          print(score, "→ Fail")

# ─────────────────────────────────────────────
# QUESTION 8 — while Loop
# ─────────────────────────────────────────────
# Write a number guessing game:
#   1. Set a secret number (you choose it, e.g. 7).
#   2. Ask the user to guess the number.
#   3. Keep asking until they guess correctly.
#   4. Each wrong guess should print one of these hints:
#        "Too high! Try again." — if their guess is too big
#        "Too low! Try again."  — if their guess is too small
#   5. When they get it right, print:
#        "Correct! You got it in X tries."
#      (where X is how many attempts they made)

# secret_num = random.randint(1,100)
# tries = 0

# while True:
#     guess_num = int(input("Guess the secret number: "))
#     tries += 1
#     if guess_num == secret_num:
#       print("Correct! You got it in " + str(tries) + " tries.")
#     elif guess_num > secret_num:
#      print("Too high! Try again.")
#     elif guess_num < secret_num: 
#       print( "Too low! Try again.")


# ─────────────────────────────────────────────
# QUESTION 9 — Functions
# ─────────────────────────────────────────────
# Write the following two functions and then call both of them:
#
# Function 1: is_even(number)
#   - Takes one number as input.
#   - Returns True if the number is even, False if it is odd.
#
# Function 2: celsius_to_fahrenheit(celsius)
#   - Takes a temperature in Celsius.
#   - Returns the temperature in Fahrenheit.
#   - Formula: F = (C × 9/5) + 32
#
# After defining both functions:
#   - Ask the user to enter a number and print whether it is even or odd.
#   - Ask the user to enter a Celsius temperature and print the Fahrenheit value.


# ─────────────────────────────────────────────
# QUESTION 10 — Lists + Functions (Putting it all together)
# ─────────────────────────────────────────────
# Write a function called analyse_scores(scores) that:
#   - Takes a list of numbers (scores) as input.
#   - Calculates and RETURNS a dictionary with:
#       "highest"  → the highest score
#       "lowest"   → the lowest score
#       "average"  → the average score (rounded to 2 decimal places)
#       "passed"   → count of scores that are >= 50
#       "failed"   → count of scores that are < 50
#
# Then call the function with this list:
#   scores = [72, 88, 45, 95, 60, 53, 78, 91, 40, 85]
#
# Print each result clearly. Example output:
#   Highest Score : 95
#   Lowest Score  : 40
#   Average Score : 70.7
#   Passed        : 8
#   Failed        : 2

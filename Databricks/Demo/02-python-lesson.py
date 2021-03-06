# Databricks notebook source
# MAGIC %md # Variables

# COMMAND ----------

my_name = "Otacilio"
my_age = 30

# COMMAND ----------

print(my_name)
print(my_age)

# COMMAND ----------

print(type(my_name))
print(type(my_age))

# COMMAND ----------

# MAGIC %md # Number

# COMMAND ----------

print(2 + 2) # simple addition
print(5 - 2) # simple subtraction
print(7 * 10) # simple multiplication

# COMMAND ----------

print(10 / 4)  # classic division returns a float
print(10 // 4)  # floor division discards the fractional part
print(10 % 4) # the % operator returns the remainder of the division

# COMMAND ----------

print(5 ** 2)  # 5 squared
print(2 ** 7)  # 2 to the power of 7

# COMMAND ----------

#Using variables
tax = 12.5 / 100
price = 100.50
print(price * tax)

# COMMAND ----------

# MAGIC %md # Strings

# COMMAND ----------

print()

# COMMAND ----------

print("Lorem ipsum dolor sit amet")
print('Lorem ipsum dolor sit amet')
print('Lorem "ipsum" dolor sit amet')

# COMMAND ----------

print(len("Lorem ipsum dolor sit amet"))

# COMMAND ----------

print("Lorem ipsum dolor sit amet".upper())

# COMMAND ----------

print("Lorem ipsum dolor sit amet".lower())

# COMMAND ----------

print("Lorem ipsum dolor sit amet dolor".replace("dolor", "laborum"))

# COMMAND ----------

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")

# COMMAND ----------

dummy_text = "Lorem ipsum"
dummy_text_year = 1500
print(f"{dummy_text} has been the industry's standard dummy text ever since the {dummy_text_year}s, when an unknown printer took a galley of type and scrambled it to make a type specimen book")

# COMMAND ----------

print("Hello" + " " + "World")

# COMMAND ----------

print("My age is" + 30)

# COMMAND ----------

# MAGIC %md ## Slicing

# COMMAND ----------

word = 'Python lesson'

# COMMAND ----------

# MAGIC %md
# MAGIC |P|y|t|h|o|n| |l|e|s|s|o|n|
# MAGIC |-|-|-|-|-|-|-|-|-|-|-|-|-|
# MAGIC |0|1|2|3|4|5|6|7|8|9|10|11|12|
# MAGIC |-13|-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

# COMMAND ----------

print(word[0])  # character in position 0
print(word[8])  # character in position 5

# COMMAND ----------

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

# COMMAND ----------

print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end

# COMMAND ----------

print(word[-2:])  # characters from the second-last (included) to the end

# COMMAND ----------

print(word[:2] + word[2:])
print(word[:4] + word[4:])

# COMMAND ----------

# MAGIC %md # List

# COMMAND ----------

numbers_list = [1, 4, 9, 16, 25]
print(numbers_list)

# COMMAND ----------

diff_types_list = [1, "Hello", 9, "16, 25"]
print(diff_types_list)

# COMMAND ----------

print(len(numbers_list))

# COMMAND ----------

print(numbers_list[0])

# COMMAND ----------

print(numbers_list[2:4])

# COMMAND ----------

# MAGIC %md ## Changing Lists

# COMMAND ----------

#Concatenation
concat_list = numbers_list + [36, 49, 64, 81, 100]
print(concat_list)

# COMMAND ----------

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wed', 'Thursday', 'Friday', 'Saturday']
print(days_of_week)

# COMMAND ----------

days_of_week[3] = 'Wednesday'
print(days_of_week)

# COMMAND ----------

# MAGIC %md ## Methods

# COMMAND ----------

students = ['Otacilo', 'Andr??', 'Maria']
print(students)

# COMMAND ----------

students.append('Carlos')
print(students)
students.append('In??s')
print(students)

# COMMAND ----------

last_student = students.pop()
print(last_student)
print(students)

# COMMAND ----------

del students[-1]
print(students)

# COMMAND ----------

students.clear()
print(students)

# COMMAND ----------

# MAGIC %md ## Copy list

# COMMAND ----------

students = ['Otacilo', 'Andr??', 'Maria']
students_2 = students
students_2.append('In??s')
print(students)
print(students_2)

# COMMAND ----------

students = ['Otacilo', 'Andr??', 'Maria']
students_2 = students.copy()
students_2.append('In??s')
print(students)
print(students_2)

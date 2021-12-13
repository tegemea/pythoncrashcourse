#concanteation
first_name = "James"
last_name = "Mwasyola"
full_name = first_name + " " + last_name

print(full_name)

print("")
print ("Hello, " + full_name.title() + "!")

print("")
# new line - \n
message = "What programming language do you love?"
print(message + "\n1. Python\n2. PHP\n3. C++")

print(" ")
# tabes - \t
message = "What programming language do you love?"
print(message + "\n\t1. Python\n2. PHP\n\t3. C++")

# Stripping white spaces

favourate_language = " python "

right_strip = favourate_language.rstrip()
print(right_strip)

left_strip = favourate_language.lstrip()
print(left_strip)

left_right_strip = right_strip.strip()
print(left_right_strip)

# numbers
age = 40
message = "Happy " + str(age) + "th Birthday! Mkulungwa"
print(message)

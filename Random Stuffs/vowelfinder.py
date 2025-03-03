# vowels = ["e", "E", "a", "A", "i", "I", "o", "O", "u", "U"]

# userstext = input("Write some word and I will count up all the vowels: ")
# vowel_count = 0

# # Loop through each character in the input string
# for char in userstext:
#     if char in vowels:  # Check if the character is a vowel
#         vowel_count += 1  # Increment the vowel count

# print(f"There are {vowel_count} vowels in the string.")




vowels = "aeiou"  # No need for uppercase since we'll convert input to lowercase
consonant = "abcdefghijklmnopqrstuvwxyz"
userstext = input("Write some words, and I shall count the vowels and consonants seperately!: ").lower() # Convert input to lowercase
vowel_count = sum(1 for char in userstext if char in vowels)  # More Pythonic approach
consonant_count = sum(1 for char in userstext if char in consonant) 
print(f"""  Your sentence: {userstext}
          Vowel Count: {vowel_count}
          Consonant Count: {consonant_count - vowel_count}""")



vowels = "aeiou"  # No need for uppercase since we'll convert input to lowercase
consonants = "bcdfghjklmnpqrstvwxyz"  # Only consonants

userstext = input("Write some words, and I shall count the vowels and consonants separately!: ").lower()  # Convert input to lowercase

vowel_count = sum(1 for char in userstext if char in vowels)  # Count vowels
consonant_count = sum(1 for char in userstext if char in consonants)  # Count consonants

print(f"""Your sentence: {userstext}
Vowel Count: {vowel_count}
Consonant Count: {consonant_count}""")
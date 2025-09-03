paragraph = input("Enter a paragraph (max 100 words): ")

words = paragraph.split()
palindromes = []

for word in words:
    clean_word = word.lower().strip(",.!?") # Remove punctuation
if clean_word == clean_word[::-1] and len(clean_word) > 1:
    palindromes.append(word)

if palindromes:
    print("Palindromes:", ", ".join(palindromes))
else:
    print(0)
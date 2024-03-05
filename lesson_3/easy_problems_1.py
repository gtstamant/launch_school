str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(str1.endswith('!'))

famous_words = "seven years ago..."

famous_words = "Four score and " + famous_words
print(famous_words)

famous_words = "seven years ago..."
famous_words = f"Four score and {famous_words}"
print(famous_words)

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

munsters_description = munsters_description.capitalize()
print(munsters_description)

munsters_description = "The Munsters are creepy and spooky."
munsters_description = munsters_description.swapcase()
print(munsters_description)

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print('Dino' in str1)
print('Dino' in str2)

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.append('Dino')
print(flintstones)


flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(['Dino', 'Hoppy'])

print(flintstones)

advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.find('house'))
print(advice.split('house')[0])

new_advice = advice.replace('important', 'urgent')
print(new_advice)
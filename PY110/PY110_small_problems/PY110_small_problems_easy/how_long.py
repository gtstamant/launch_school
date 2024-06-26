def word_lengths(s=''):
    return [f'{word} {len(word)}' for word in s.split()]


print(word_lengths('cow sheep chicken'))
# ['cow 3', 'sheep 5', 'chicken 7']

print(word_lengths('baseball hot dogs and apple pie'))
# ['baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3']

print(word_lengths("It ain't easy, is it?"))
# ['It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3']

print(word_lengths('Supercalifragilisticexpialidocious'))
# ['Supercalifragilisticexpialidocious 34']

print(word_lengths(''))      # []
print(word_lengths())        # []
"""
## Problem ##
Input: verse number or no input
Output: part or all of '99 bottles of beer on the wall'

Program takes two arguments, a higher number and a lower number
it then returns a portion of the beer song

## Examples & Test Cases ##

BeerSong class

class method
- verse method
-- one argument returns a single verse

class method
- verses method
-- two arguments returns inclusive range of verses from A to B

class method
- lyrics
-- returns all lyrics

"""

class BeerSong:
    @staticmethod
    def n_bottle_verse(num):
        return (
            f'{num} bottles of beer on the wall, {num} bottles of beer.\n'
            f'Take one down and pass it around, {num - 1} bottles of beer on the wall.\n'
        )
    
    @staticmethod
    def two_bottle_verse():
        return (
            f'2 bottles of beer on the wall, 2 bottles of beer.\n'
            f'Take one down and pass it around, 1 bottle of beer on the wall.\n'
        )

    @staticmethod
    def one_bottle_verse():
        return (
            f'1 bottle of beer on the wall, 1 bottle of beer.\n'
            f'Take it down and pass it around, no more bottles of beer on the wall.\n'
        )

    @staticmethod
    def no_bottles_verse():
        return (
            f'No more bottles of beer on the wall, no more bottles of beer.\n'
            f'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
        )
    
    @classmethod
    def verse(cls, verse_num):
        match verse_num:
            case 2: return cls.two_bottle_verse()
            case 1: return cls.one_bottle_verse()
            case 0: return cls.no_bottles_verse()
            case _: return cls.n_bottle_verse(verse_num)

    @classmethod
    def verses(cls, start, end):
        return '\n'.join(cls.verse(num) for num in range(start, end - 1, -1))

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)

print(BeerSong.lyrics())
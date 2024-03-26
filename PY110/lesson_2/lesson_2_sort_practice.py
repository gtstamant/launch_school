# Practice problem 1

lst = [10, 9, -6, 11, 7, -16, 50, 8]

# print(sorted(lst))
# print(sorted(lst, reverse=True))

# 2

lst.sort()
# print(lst)

lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst.sort(reverse=True)
# print(lst)

# 3

lst = [10, 9, -6, 11, 7, -16, 50, 8]

sorted_lst = sorted(lst, key=str)
# print(sorted_lst)

sorted_lst = sorted(lst, key=str, reverse=True)
# print(sorted_lst)

# 4

from pprint import pp

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {   'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def get_pub_year(book):
    return int(book['published'])

books.sort(key=get_pub_year)

pp(books)
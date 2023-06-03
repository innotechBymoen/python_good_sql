import dbhelpers

def get_all_books():
    results = dbhelpers.run_procedure("call get_all_books()", [])
    for book in results:
        print("--------")
        print("Author:", str(book[2], 'utf-8'))
        print("Title:", str(book[1], 'utf-8'))
        print("Release Date:", book[3])


def get_author_books():
    author = input("Please enter the name of the author you want: ")
    results = dbhelpers.run_procedure("call get_authors_books(?)", [author])
    for book in results:
        print("--------")
        print("Author:", str(book[2], 'utf-8'))
        print("Title:", str(book[1], 'utf-8'))
        print("Release Date:", book[3])

#get_all_books()
get_author_books()
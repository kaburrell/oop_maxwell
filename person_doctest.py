"""
Person class tests


>>> import person
>>> jd = person.Person("John", "Doe")

>>> jd.full_name()
'John Doe'

>>> jd.formal_name("Mr.")
'Mr. John Doe'

"""

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

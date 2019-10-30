
def list_c():
    symbols = '$¢£¥€¤'
    codes = []
    print("Using a for")
    print('''
        for symbol in symbols:
        codes.append(ord(symbol))''')
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

    print("Using list comprehension")
    print('''[ord(symbol) for symbol in symbols]''')
    print([ord(symbol) for symbol in symbols])

    print('''
    Syntax tip
    In Python code, line breaks are ignored inside pairs of [], {} or ().
    So you can build multi-line lists, listcomps, genexps, dictionaries etc.
    without using the ugly \ line continuation escape.''')

    print('using map and filter')
    print('''list(filter(lambda c: c>127, map(ord,symbols)))''')
    beyond_ascii = list(filter(lambda c: c>127, map(ord,symbols)))
    print(beyond_ascii)
    print('using list comprehension')
    print(''' [ord(s) for s in symbols if ord(s) > 127]''')
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)

    colors = ['black','white']
    sizes = ['S','M','L']

    tshirts = [ (c,s) for c in colors for s in sizes]
    print('Cartesian Product')
    print('''[ (c,s) for s in colors for s in sizes]''')
    print(tshirts)

    print('''
    A genexp saves memory because it yields items one by one using the iterator
    protocol instead of building a whole list just to feed another constructor.
    Genexps use the same syntax as listcomps, but are enclosed in parenthesis rather than
    brackets.''')

    print('with generator expression')
    print('''
     for tshirt in ('{} {}'.format(c,s) for c in colors for s in sizes):
        print(tshirt)
    ''')
    for tshirt in ('{} {}'.format(c,s) for c in colors for s in sizes):
        print(tshirt)

    return

def tuples():

    print('''
    Tuples work well as records because of the tuple unpacking mechanism —''')

    print(''' a function returning more than one item\n
    quotient, remainder =   divmod(20,8)''')

    quotient, remainder =   divmod(20,8)
    print(quotient,remainder)
    print('''
    Defining function parameters with *args to grab arbitrary excess arguments is a classic
    Python feature.  The idea can be extended.
    a,b,*rest = range(5)
    ''')
    a,b,*rest = range(5)
    print(a,b,rest)

    print('''Complex unpacking
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:  #
            print(fmt.format(name, latitude, longitude))
    ''')
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:  #
            print(fmt.format(name, latitude, longitude))

    print('''
    The collections.namedtuple function is a factory that produces subclasses of tuple
    enhanced with field names and a class name — which helps debugging.
    Two parameters are required to create a named tuple: a class name and a list of
    field names, which can be given as an iterable of strings or as a single space delimited
    string.
    from collections import namedtuple
    City = namedtuple('City','name country population coordinates')
    tokyo = City('Tokyo','JP',36.933,(35.689722,139.691634))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[1])
    print(City._fields)
    delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
    delhi = City._make(delhi_data)
    for key, value in delhi._asdict().items():
        print(key + ':' , value)

    ''')


    from collections import namedtuple
    City = namedtuple('City','name country population coordinates')
    tokyo = City('Tokyo','JP',36.933,(35.689722,139.691634))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[1])
    print(City._fields)
    delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
    delhi = City._make(delhi_data)
    for key, value in delhi._asdict().items():
        print(key + ':' , value)

    return

def slicing():
    print('''
    
    • It’s easy to see the length of a slice or range when only the stop position is given:
    range(3) and my_list[:3] both produce three items.
    • It’s easy to compute the length of a slice or range when start and stop are given: just
    subtract stop - start.
    • It’s easy to split a sequence in two parts at any index x, without overlapping: simply
    get my_list[:x] and my_list[x:]. See for example:

    to evaluate the expression seq[start:stop:step], Python calls
    seq.__getitem__(slice(start, stop, step)).
    s = 'bicycle'
    
    print(s[::3])
    print(s[::-1])
    print(s[::-2])
    return
    ''')
    s = 'bicycle'
    print(s[::3])
    print(s[::-1])
    print(s[::-2])

    print('''
    Parsing a file
    
    invoice = """
    0.....6.................................40........52...55........
    1909  Pimoroni PiBrella                     $17.50    3    $52.50
    1489  6mm Tactile Switch x20                 $4.95    2     $9.90
    1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
    1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
    """
    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)
    line_items = invoice.split('\n')[2:]
    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])

    return
    ''')

    invoice = """
    0.....6.................................40........52...55........
    1909  Pimoroni PiBrella                     $17.50    3    $52.50
    1489  6mm Tactile Switch x20                 $4.95    2     $9.90
    1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
    1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
    """
    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)
    line_items = invoice.split('\n')[2:]
    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])

    print('''
    
    Slices are not just useful to extract information from sequences, they can also be used
to change mutable sequences in-place
    ''')

    l =list(range(10))
    print(l)
    print('''l[2:5] = [20,30]''')
    l[2:5] = [20,30]
    print(l)

    print('''
    list of lists
    board = [['_'] * 3 for i in range(3)]
    board[1][2] = 'X'
    print(board)
    ''')
    board = [['_'] * 3 for i in range(3)]
    board[1][2] = 'X'
    print(board)

    print('''
    but be carefuel with
    weird_board = [['_'] * 3] * 3
    weird_board[1][2] = 'O'
    print(weird_board)

    ''')
    weird_board = [['_'] * 3] * 3
    weird_board[1][2] = 'O'
    print(weird_board)

    print('''
    when a does not implement __iadd__, the expression a += b
    has the same effect as a = a + b: the expression a + b is evaluated first, producing a
    new object which is then bound to a. In other words, the identity of the object bound
    to a may or may not change, depending on the availability of __iadd__.
    t = (1,2,3)
    print(id(t), t)
    t *= 3
    print(id(t), t)
    
    Three lessons:
    .Putting mutable items in tuples is not a good idea.
    • Augmented assignment is not an atomic operation — we just saw it throwing an
    exception after doing part of its job.
    • Inspecting Python bytecode is not too difficult, and is often helpful to see what is
    going on under the hood.  Online Python Tutor.
    ''')

    t = (1,2,3)
    print(id(t), t)
    t *= 3
    print(id(t), t)

    return


if __name__=='__main__':

    print('''
    Understanding the variety of sequences available in Python saves us from reinventing
    the wheel, and their common interface inspires us to create APIs that properly support
    and leverage existing and future sequence types.\n
    Container sequences hold references to the objects they contain, which may be of any
    type, while flat sequences physically store the value of each item within its own memory
    space, and not as distinct objects. Thus, flat sequences are more compact, but they are
    limited to holding primitive values like characters, bytes and numbers\n
    Another way of grouping sequence types is by mutability:
    Mutable sequences
    list, bytearray, array.array, collections.deque and memoryview
    Immutable sequences
    tuple, str and bytes\n
    A quick way to build a sequence is using a list comprehension (if the target is a list)
    or a generator expression (for all other kinds of sequences). 
    ''')

    #list_c()
    #tuples()
    slicing()
import re
import collections


def usingSets():

    print('''
    
    A set is a collection of unique objects. A basic use case is removing duplication:

    ''')


def usingDics():

    WORD_RE = re.compile('\w+')

    index = {}

    with open('text.txt', encoding='utf-8') as fp:

        for line_no, line in enumerate(fp,1):

            for match in WORD_RE.finditer(line):
                word = match.group()
                col_no = match.start() + 1
                location = (line_no, col_no)
                index.setdefault(word,[]).append(location)

    for word in sorted(index, key=str.upper):
        print(word,index[word])


def usingUserDict():

    print('''
    It’s almost always easier to create a new mapping type by extending UserDict than dict.
    ''')

    class StrKeyDict(collections.UserDict):

        def __missing__(self, key):
            if isinstance(key,str):
                raise KeyError(key)
            return self[str(key)]

        def __contains__(self, key):
            return str(key) in self.data

        def __setitem__(self, key, value):
            self.data[str(key)] = value


if __name__ == '__main__':

    print('''
        Because of their crucial role, Python dicts are highly optimized. Hash tables are the engines behind Python’s high performance dicts.
        my_dict = {}
        isinstance(my_dict,collections.abc.Mapping)
        True
        Using insinstace is better than checking whether a function argument is of dict type, because then alternative mapping types can be used. 
        the keys must be hashable
        x = (1,2,(3,4))
        hash(x)
        -2725224101759650258
        ''')

    print('''

        >>> a = dict(one=1, two=2, three=3) 
        >>> b = {'one': 1, 'two': 2, 'three': 3} 
        >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) 
        >>> d = dict([('two', 2), ('one', 1), ('three', 3)]) 
        >>> e = dict({'three': 3, 'one': 1, 'two': 2}) 
        >>> a == b == c == d == e True 

        Every Pythonista knows that d.get(k, default) is an alternative to d[k] whenever a default value is more convenient than handling KeyError
        
        setdefault example: 
        
        ''')

    usingDics()

    print('''
        >>> d[1]    
        Traceback (most recent call last):      ...    KeyError: '1'
        >>> d.get('2')    'two'    
        >>> d.get(1, 'N/A')    'N/A'
        >>> 2 in d    
        True
        A search in my_dict.keys() is efficient
        options
        collections.OrderedDict 
        collections.ChainMap #searches each grouping 
        collections.Counter  #excellent for histograms
    ''')

    print('''
    MappingProxyType builds a read-only mappingproxy instance from a dict. 
    >>> from types import MappingProxyType 
    >>> d = {1: 'A'} 
    >>> d_proxy = MappingProxyType(d) 
    >>> d_proxy mappingproxy({1: 'A'}) 
    >>> d_proxy[1]  'A' 
    >>> d_proxy[2] = 'x'  
    Traceback (most recent call last):  File "<stdin>", line 1, in <module> 
    TypeError: 'mappingproxy' object does not support item assignment 
    >>> d[2] = 'B' 
    >>> d_proxy  mappingproxy({1: 'A', 2: 'B'}) 
    >>> d_proxy[2] 'B' 
    ''')
    print('Done')
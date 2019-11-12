import requests
import time




class Character:
    """
    A StarWars character

    >>> Character("Luke Skywalker")
    Character("Luke Skywalker")
    >>> Character("Luke Skywalker").name
    'Luke Skywalker'
    >>> Character("Luke Skywalker").movies
    ['A New Hope', 'Return of the Jedi', 'Revenge of the Sith', 'The Empire Strikes Back', 'The Force Awakens']
    >>> Character("Skywalker")
    Traceback (most recent call last):
        ...
    ValueError: found more than one character with "Skywalker" in the name
    >>> Character("C4PO")
    Traceback (most recent call last):
        ...
    ValueError: this is not the character you are looking for
    """


    def __init__(self, name):
        fullname, movies = self._remote(name)

        self.name = fullname
        self.movies = movies

    def __repr__(self):
        return '{0}("{1}")'.format(self.__class__.__name__, self.name)

    def _remote(self, name):
        d = requests.get(f'https://swapi.co/api/people/?search={name}').json()
        results = d['results']
        count = len(results)
        
        if count == 0:
            raise ValueError('this is not the character you are looking for')
        elif count > 1:
            raise ValueError(f'found more than one character with "{name}" in the name')
        
        fullname = results[0]['name']


        movies = []
        for url in results[0]['films']:
            film = requests.get(url).json()
            movies.append(film['title'])
        movies.sort()

        return fullname, movies


def features_together(a, b):
    """
    Returns a list of movie where both character a and character b are present

    >>> features_together(Character("Anakin Skywalker"), Character("Darth Vader"))
    ['Revenge of the Sith']
    >>> features_together(Character("Rey"), Character("Mace Windu"))
    []
    """
    # l =[]                                                               

    # for m in a.movies: 
    #     if m in b.movies: 
    #         l.append(m)
    
    # return l

    return list(set(a.movies) & set(b.movies))



if __name__ == "__main__":
    import vcr
    import doctest
    import time

    t0 = time.time()
    with vcr.use_cassette('swapi.yaml'):
        doctest.testmod()
    t1 = time.time()

    print(f'{t1-t0:.2f}s')
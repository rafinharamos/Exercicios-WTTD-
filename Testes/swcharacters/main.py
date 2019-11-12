import requests
response = requests.get("https://swapi.co/api/").json()

class Character():
    def personagem(self, name, movie):
        self.name = 'Luke Skywalker'
        self.movies = []
        if self.name in movie:
            append.self.movie(self.name)
        else:
            raise AssertionError
        return Character

        


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
    pass

    '''def features_together(a, b):
       
        Returns a list of movie where both character a and character b are present

        >>> features_together(Character("Anakin Skywalker"), Character("Darth Vader"))
        ['Revenge of the Sith']
        >>> features_together(Character("Rey"), Character("Mace Windu"))
        []
        
        #return []'''

if __name__ == "__main__":
    import doctest
    doctest.testmod()


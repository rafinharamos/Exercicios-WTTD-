import requests
class StarWarsMovie:
        
    def __init__(self,
                    title: str,
                    episode_id: int,
                    opening_crawl: str,
                    director: str,
                    producer: str,
                    release_date: datetime,
                    characters: List[str],
                    planets: List[str],
                    starships: List[str],
                    vehicles: List[str],
                    species: List[str],
                    created: datetime,
                    edited: datetime,
                    url: str
                    ):
    
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl= opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species
        self.created = created
        self.edited = edited
        self.url = url
    
        if type(self.release_date) is str:
            self.release_date = dateutil.parser.parse(self.release_date)
    
        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)
    
        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)
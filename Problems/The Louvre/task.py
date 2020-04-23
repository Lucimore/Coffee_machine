class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


masterpiece = Painting(input(), input(), input())
print('"{}" by {} ({}) hangs in the {}.'.format(masterpiece.title,
                                                masterpiece.artist,
                                                masterpiece.year,
                                                masterpiece.museum))

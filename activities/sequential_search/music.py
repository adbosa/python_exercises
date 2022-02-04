class Music():
    def __init__(self, title, interpreter, composer, year):
        self.title = title
        self.interpreter = interpreter
        self.composer = composer
        self.year = year

class SearchEngine():
    def search_by_title(self, playlist, title):
        for i in range(len(playlist)):
            if playlist[i].title == title:
                return i
        return -1

    def lets_search(self):
        playlist = [Music('Ponta de Areia', 'Milton Nascimento', 'Milton Nascimento', 1975),
                    Music('Podres Poderes', 'Caetano Veloso', 'Caetano Veloso', 1984),
                    Music('Baby', 'Gal Costa', 'Caetano Veloso', 1969)]

        position = self.search_by_title(playlist, 'Baby')

        if position == -1:
            print('The title is not in the playlist')
        else:
            favorite = playlist[position]
            print(favorite.title, favorite.interpreter, favorite.composer, favorite.year, sep =', ');

import fresh_tomatoes as ft
import media as md

if __name__ == '__main__':
    movies = []
    m1 = md.Movie('Deadpool', 'https://image.tmdb.org/t/p/w185/inVq3FRqcYIRl2la8iZikYYxFNR.jpg',
                  'http://www.youtube.com/watch?v=7jIBCiYg58k')
    movies.append(m1)
    m2 = md.Movie('The Hunger Games: Mockingjay - Part 2',
                  'https://image.tmdb.org/t/p/w185/nN4cEJMHJHbJBsp3vvvhtNWLGqg.jpg',
                  'http://www.youtube.com/watch?v=Ay-ZN4uRZ-4')
    movies.append(m2)
    m3 = md.Movie('Mad Max: Fury Road', 'https://image.tmdb.org/t/p/w185/kqjL17yufvn9OVLyXYpvtyrFfak.jpg',
                  'http://www.youtube.com/watch?v=2h6IKpgFixg')
    movies.append(m3)
    m4 = md.Movie('Batman v Superman: Dawn of Justice',
                  'https://image.tmdb.org/t/p/w185/6bCplVkhowCjTHXWv49UjRPn0eK.jpg',
                  'http://www.youtube.com/watch?v=nIGtF3J5kn8')
    movies.append(m4)
    m5 = md.Movie('The Hunger Games: Mockingjay - Part 1',
                  'https://image.tmdb.org/t/p/w185/cWERd8rgbw7bCMZlwP207HUXxym.jpg',
                  'http://www.youtube.com/watch?v=C_Tsj_wTJkQ')
    movies.append(m5)

    # Calling the methods in fresh_tomato
    ft.open_movies_page(movies)

import fresh_tomatoes as ft
import media as md

if __name__ == '__main__':
    deadpool = md.Movie('Deadpool', 'https://image.tmdb.org/t/p/w185/inVq3FRqcYIRl2la8iZikYYxFNR.jpg',
                  'http://www.youtube.com/watch?v=7jIBCiYg58k')
    mockingjay_part_two = md.Movie('The Hunger Games: Mockingjay - Part 2',
                  'https://image.tmdb.org/t/p/w185/nN4cEJMHJHbJBsp3vvvhtNWLGqg.jpg',
                  'http://www.youtube.com/watch?v=Ay-ZN4uRZ-4')
    fury_road = md.Movie('Mad Max: Fury Road', 'https://image.tmdb.org/t/p/w185/kqjL17yufvn9OVLyXYpvtyrFfak.jpg',
                  'http://www.youtube.com/watch?v=2h6IKpgFixg')
    dawn_of_justice = md.Movie('Batman v Superman: Dawn of Justice',
                  'https://image.tmdb.org/t/p/w185/6bCplVkhowCjTHXWv49UjRPn0eK.jpg',
                  'http://www.youtube.com/watch?v=nIGtF3J5kn8')
    mockingjay_part_one = md.Movie('The Hunger Games: Mockingjay - Part 1',
                  'https://image.tmdb.org/t/p/w185/cWERd8rgbw7bCMZlwP207HUXxym.jpg',
                  'http://www.youtube.com/watch?v=C_Tsj_wTJkQ')
    movies = [deadpool, mockingjay_part_two, fury_road, dawn_of_justice, mockingjay_part_one]
    # Calling the methods in fresh_tomato
    ft.open_movies_page(movies)

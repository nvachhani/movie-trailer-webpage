import fresh_tomatoes
import media

godzilla = media.Movie("Godzilla",
                       "Centuries old monsters are awoken.",
                       "https://upload.wikimedia.org/wikipedia/en/1/10/Godzilla_%282014%29_poster.jpg",
                       "https://www.youtube.com/watch?v=QjKO10hKtYw")


school_of_rock = media.Movie("School of Rock",
                       "A subsitute teacher inspires his music class.",
                       "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                       "https://www.youtube.com/watch?v=3PsUJFEBC74")


the_rock = media.Movie("The Rock",
                       "A scientist finds himself embroiled in a hostage crisis.",
                       "https://upload.wikimedia.org/wikipedia/en/8/82/The_Rock_%28movie%29.jpg",
                       "https://www.youtube.com/watch?v=jGVJx5mOtL8")


fellowship_of_the_ring= media.Movie("The Fellowship of the Ring",
                                    "Nine companions set out to destroy an evil ring.",
                                    "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
                                    "https://www.youtube.com/watch?v=V75dMMIW2B4")

bad_boys = media.Movie("Bad Boys",
                       "Two cops take on a drug lord.",
                       "https://upload.wikimedia.org/wikipedia/en/a/a8/Bad_Boys.jpg",
                       "https://www.youtube.com/watch?v=ty8eBdHaf1c")

the_life_aquatic = media.Movie("The Life Aquatic",
                               "A man sets out for revenge on a shark that ate his friend.",
                               "https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg",
                               "https://www.youtube.com/watch?v=XVt9g-uQOx0")

movies = [godzilla, school_of_rock, the_rock, fellowship_of_the_ring, bad_boys, the_life_aquatic]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)

star_wards_9 = media.Movie("Star Wars: The Last Jedi",
                     "Having taken her first steps into a larger world in Star Wars: The Force Awakens (2015), Rey continues her epic journey with Finn, Poe and Luke Skywalker in the next chapter of the saga.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Star_Wars_The_Last_Jedi.jpg/220px-Star_Wars_The_Last_Jedi.jpg",
                     "https://www.youtube.com/watch?v=zB4I68XVPzQ")

#print (star_wards_9.storyline)
#star_wards_9.show_trailer()

thor_ragnorok = media.Movie("Thor: Ragnorok",
                            "Imprisoned, the mighty Thor finds himself in a lethal gladiatorial contest against the Hulk, his former ally. Thor must fight for survival and race against time to prevent the all-powerful Hela from destroying his home and the Asgardian civilization.",
                            "https://www.flickeringmyth.com/wp-content/uploads/2017/03/Thor-Ragnarok.jpg",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU")

#thor_ragnorok.show_trailer()



# Save movie objects to array
movies = [toy_story, star_wards_9, thor_ragnorok]

# Launch website from python
fresh_tomatoes.open_movies_page(movies)

#print the predefined variable doc we stored in the class
print (media.Movie.__doc__)
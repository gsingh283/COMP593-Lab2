
def main():

    # : Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Gursewak Singh',
        'student_id' : 10312237 ,
        'pizza_toppings' : ['GREEN PEPPER', 'RED ONION', 'OLIVES'],
        'movies' : [
            {
                "title" : "gurdians of galaxy", "genre" : "action-adventure"
            },
            {
                "title" : "mission impossible - dead reckoning", "genre" : "science fiction"
            }
            
        ]
    }
    
    
    print(print_student_name_and_id(about_me))
    print(print_pizza_toppings(about_me))
    print(add_pizza_toppings(about_me, ["MUSHROOMS"]))
    print(print_pizza_toppings(about_me))
    print(print_movie_genres(about_me))
    print(print_movie_titles(about_me))
    
    # : Step 3 - Add another movie to the data structure
    new_movie = {'title' : 'life of pie', 'genre' : 'adventure'}
    about_me["movies"].append(new_movie)
# : Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f'My name is {full_name},but you can call me Sir {first_name}.\nMy student ID is {student_id}')
    
    
# : Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'] = sorted(map(str.lower, about_me['pizza_toppings']))


# : Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping}")  
# : Step 7 - Function that prints comma-separated list of movie genres

def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    if len(genres) == 1:
        print(f"I like to watch {genres[0]} movies.")
    else:
        genre_list = ', '.join(genres[:-1]) + f" and {genres[-1]}"
        print(f"I like to watch {genre_list} movies.")


# : Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    titles = [movie['title'] for movie in about_me['movies']]
    movie_name = [title.title() for title in titles]
    if len(movie_name) == 1:
        print(f"Some of my favourite movies are {movie_name[0]}!")
    else:
        title_list = ', '.join(movie_name[:-1]) + f" and {movie_name[-1]}"
        print(f"Some of my favourite movies are {title_list}!")
    




if __name__ == '__main__':
    main()


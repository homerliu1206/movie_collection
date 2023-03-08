MENU_PROMPT = "\nEnter 'a' to add  a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movies():
	title = input('Enter the movie title:')
	director = input('Enter the movie director:')
	year = input('Enter the movie release year:')

	movies.append({
		'title': title,
		'director': director,
		'release year': year
	})


def show_movies():
	for movie in movies:
		print_movies(movie)


def print_movies(movie):
	print(f"Title: {movie['title']}")
	print(f"Director: {movie['director']}")
	print(f"Release Year: {movie['release year']}")


def find_movies():
	search_title = input("Enter movie title you're looking for:")

	for movie in movies:
		if movie["title"] == search_title:
			print_movies(movie)


user_options = {
	"a": add_movies,
	"l": show_movies,
	"f": find_movies
}


def menu():
	selection = input(MENU_PROMPT)
	while selection != 'q':
		if selection in user_options:
			selected_function = user_options[selection]
			selected_function()
		else:
			print('Unknown command. Please try again.')

		selection = input(MENU_PROMPT)

menu()
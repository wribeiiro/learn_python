import requests
import json 

def search_movie(movie_name = 'interestellar'):
    try:
        response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=20d0453e2b57cb10e3203c454698e785&language=en-US&query=' + movie_name)
        return json.loads(response.text)
    except Exception as e:
        print('Chama o amir', e)
        return None

def print_details(movie):
    print('Title:', movie['title'])
    print('Year:', movie['release_date'])
    print('Overview:', movie['overview'])
    print('Vote:', movie['vote_count'])
    print('----------------------------')

exit = False

while not exit:
    option = input('Informe o nome de um filme, ou SAIR para fechar: ')

    if option.upper() == 'SAIR':
        exit = True
        print('Exiting...')
    else:
        search_film = search_movie(option)

        if int(search_film['total_results']) <= 0 or search_film == None:
            print('Movie not found')
            exit = False
        else:
            for movie in search_film['results']:
                print_details(movie)
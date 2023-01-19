#-----------------------------------------------------
#Code has been written by 
# Harsh Priteshkumar Mistry, Roll Number = 2022200: 
# Aditya Jagdale, Roll Number = 2022032: 
# Vimal Jayant S., Roll Number = 2022571
#-----------------------------------------------------

from tmdbv3api import Movie
from tmdbv3api import TMDb
import requests
import json


#function to get the spotify url from api
def songs(movie):
    url = "https://musicapi13.p.rapidapi.com/search"
    payload = {
        "album": movie,#movie album
        "type": "album",
        "sources": ["spotify", "youtube"]#checking the album on youtube and spotify
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "89ac92ecf8msh9e4b2587e611d9dp159cabjsndbbd9e51e3d1",
        "X-RapidAPI-Host": "musicapi13.p.rapidapi.com"#api used
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    rec = json.loads(response.text)

    return(rec['albums'][0]['data']['url'])#returning the url

#function to get the information of the movie
def movie_info(movie,movie_title):
    search_movie = movie.search(movie_title)
    for res in search_movie:
        return res.id, res.title, res.overview#getting movie_id, movie_title, and movie_overview

#printing similar movies
def movie_similar(movie,movie_id):
    similar = movie.similar(movie_id)
    c = 1
    for rec in similar:
        if c == 6:#printing top 5 similar movies
            break
        print(str(c)+"."+rec.title+":")
        print("Synopsis:",rec.overview)
        print()
        c+=1

def main():
    #taking input of movietitle
    movietitle = input("Please input your desired movie title : ")
    #api key of the movie db api
    tmdb_api_key = '573a2dd54f20f9462c862d5d9b9b42c3'
    movie = Movie()
    tmdb = TMDb()
    #setting api key
    tmdb.api_key = tmdb_api_key
    #checking if the movie is there in the api
    try:
        movie_id,movie_title,movie_overview = movie_info(movie,movietitle)
        print("\n"+movie_title+":")
        print(movie_overview)
        print("\nSpotify Album link:",songs(movie_title)+"\n")
        print("--------------------------------------------------------------------------------------------------------")
        movie_similar(movie,movie_id)
    #if the movie is not there:
    except:
        print("No such movie available")

main()
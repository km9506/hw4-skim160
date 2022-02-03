import flask

app = flask.Flask(__name__)

#making list of favorite tv shows
tvShows = ["Rick and Morty","Family Guy","Bob's Burger","South Park","The Simpsons"]

#making list of url of picture of shows
urlp = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAe8TTP-orp9mtoPq0bh3FehQiFrKwShbL5s_rl1uVD4xayuNK", "https://m.media-amazon.com/images/M/MV5BODEwZjEzMjAtNjQxMy00Yjc4LWFlMDAtYjhjZTAxNDU3OTg3XkEyXkFqcGdeQXVyOTM2NTM4MjA@._V1_.jpg", "https://m.media-amazon.com/images/M/MV5BZGJiNmM1NDctNWUxYS00YzE4LWJjNTgtYTJhYzE0NjFmMTMwXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg", "https://m.media-amazon.com/images/M/MV5BOGE2YWUzMDItNTg2Ny00NTUzLTlmZGYtNWMyNzVjMjQ3MThkXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_FMjpg_UX1000_.jpg", "https://m.media-amazon.com/images/M/MV5BYjFkMTlkYWUtZWFhNy00M2FmLThiOTYtYTRiYjVlZWYxNmJkXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg"]

@app.route("/")  # Python decorator
def main():
    return flask.render_template("index.html", len = len(tvShows), tvShows = tvShows)
    return flask.render_template("index.html", len = len(urlp), urlp = urlp)

app.run(
    debug=True
)
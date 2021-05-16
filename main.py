import json

from flask import Flask, jsonify, render_template, request

import lyrics_extractor


app = Flask(__name__)


@app.route("/")
def check():
    return render_template("index.html")


@app.route("/output", methods=["POST"])
def output():
    url = request.json["url"]
    song_name, lyrics = lyrics_extractor.get_lyrics(lyrics_url=url)
    return_data = {"song_name": song_name, "lyrics": lyrics}

    return jsonify(ResultSet=json.dumps(return_data))


if __name__ == "__main__":
    app.run(debug=True)

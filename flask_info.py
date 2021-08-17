

from flask import Flask
from flask_cors import CORS
import pandas as pd
import json

from recommender import return_song_suggestion

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)
print(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to my Spotify Recommender API!<br/>")

@app.route("/api/search/<query>")
def search_query(query=None):

    print('it is working')
    
    try:
        print('ttest1')
        results = return_song_suggestion(query)
        print('test2')
        print('test3')
        results = {"song": "My song"}
        data = json.dumps(results, ensure_ascii=False, indent=4)
        print("returning data")

        return (
            data
        )

    except Exception as e:
        print('exception')
        return (
            f"{e}"
    )

if __name__ == '__main__':
    app.run()
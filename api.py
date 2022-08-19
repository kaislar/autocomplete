from flask import Flask
from flask import request
from Trie import Trie
import json
import random

def load_queries_from_file(path, max_size=10**6):
    data = []
    i=0
    # Read the first max_size rows
    with open(path) as f:
        for line in f:
            data.append(json.loads(line)['keyphrase'])
            i+=1
            if i== max_size:
                break;
    # Generate random frequencies
    queries = { i : random.randint(1, 1000) for i in data }
    return queries

app = Flask(__name__)


@app.route('/autocomplete', methods=['GET'])
def hello():
    query = request.args.get('query')
    res = t.query(query)
    return res


max_size = 10**6

path = "./keyphrases.json"

t = Trie()
queries = load_queries_from_file(path)
t.build_tree(queries)
app.run(debug=False, host="0.0.0.0")
from flask import Flask, jsonify, Response
from autocomplete import trie

app = Flask(__name__)


@app.route('/query/<string:query>')
def execute_query(query: str) -> Response:
    return jsonify({'results': trie.get_words(query)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_human_earth_alive_characters():
    url = "https://rickandmortyapi.com/api/character/"
    characters = []
    while url:
        response = requests.get(url)
        data = response.json()
        for character in data['results']:
            if (character['species'] == 'Human' and
                character['status'] == 'Alive' and
                'Earth' in character['origin']['name']):
                characters.append({
                    'Name': character['name'],
                    'Location': character['location']['name'],
                    'Image': character['image']
                })
        url = data['info']['next']
    return characters

@app.route('/characters', methods=['GET'])
def characters():
    chars = get_human_earth_alive_characters()
    return jsonify(chars)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

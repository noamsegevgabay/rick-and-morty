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
    try:
        # Perform a request to the /characters endpoint
        response = requests.get('http://localhost:5000/characters')
        
        # Check if the request was successful
        if response.status_code == 200:
            return jsonify({'status': 'ok'})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to fetch characters'}), 500
    except requests.RequestException as e:
        # Handle request exceptions
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

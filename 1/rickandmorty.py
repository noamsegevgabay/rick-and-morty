import requests
import csv

# Function to fetch data
def get_human_earth_alive_characters():
    url = "https://rickandmortyapi.com/api/character/"  # Define the initial URL
    characters = []
    while url:
        response = requests.get(url)
        data = response.json()
        
        # Print all the characters found
        for character in data['results']:
            origin = character['origin']['name']
          #  print(f"Name: {chracter['name']}, Species: {character['species']}, Status: {character['status']}, Origin: {origin}")
            
            # Filter characters based on conditions
            if (character['species'] == 'Human' and 
                character['status'] == 'Alive' and 
                'Earth' in origin):
                characters.append([character['name'], character['location']['name'], character['image']])
                
        url = data['info']['next']  # Move to the next page in the API
    
    #print(characters)
    return characters

# Write the results to a CSV file
def write_to_csv(characters):
    with open('characters.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Location', 'Image'])
        writer.writerows(characters)

# Execute the script
if __name__ == "__main__":
    characters = get_human_earth_alive_characters()
    write_to_csv(characters)

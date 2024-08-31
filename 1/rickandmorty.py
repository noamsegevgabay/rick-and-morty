import requests
import csv

# פונקציה לשליפת נתונים
def get_human_earth_alive_characters():
    url = "https://rickandmortyapi.com/api/character/"  # הגדרת ה-URL ההתחלתי
    characters = []
    while url:
        response = requests.get(url)
        data = response.json()
        
        # הדפסת כל הדמויות שנמצאו
        for character in data['results']:
            origin = character['origin']['name']
          #  print(f"Name: {chracter['name']}, Species: {character['species']}, Status: {character['status']}, Origin: {origin}")
            
            # סינון הדמויות לפי התנאים
            if (character['species'] == 'Human' and 
                character['status'] == 'Alive' and 
                'Earth' in origin):
                characters.append([character['name'], character['location']['name'], character['image']])
                
        url = data['info']['next']  # עובר לעמוד הבא ב-API
    
    #print(characters)
    return characters

# כתיבת התוצאות לקובץ CSV
def write_to_csv(characters):
    with open('characters.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Location', 'Image'])
        writer.writerows(characters)

# הפעלת הסקריפט
if __name__ == "__main__":
    characters = get_human_earth_alive_characters()
    write_to_csv(characters)

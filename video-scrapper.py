import requests
import os
import time
from pystyle import Colors, Colorate

def fetch_tiktok_data(video_url):
    while True:
        video_id = video_url.split("/video/")[-1]
        api_url = f"https://countik.com/api/videoinfo/{video_id}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()

            if 'create_date' in data:
                print(Colorate.Color(Colors.blue, f"Date de création : {data['create_date']}"))
            if 'creator' in data:
                print(Colorate.Color(Colors.blue, f"Créateur de la vidéo : {data['creator']}"))
            if 'desc' in data:
                print(Colorate.Color(Colors.blue, f"Description de la vidéo : {data['desc']}"))
            if 'id' in data:
                print(Colorate.Color(Colors.blue, f"ID : {data['id']}"))
            if 'likes' in data:
                print(Colorate.Color(Colors.blue, f"Likes : {data['likes']}"))
            if 'plays' in data:
                print(Colorate.Color(Colors.blue, f"Views : {data['plays']}"))
            if 'shares' in data:
                print(Colorate.Color(Colors.blue, f"Partages : {data['shares']}"))
            if 'comments' in data:
                print(Colorate.Color(Colors.blue, f"Commentaires : {data['comments']}"))

            time.sleep(5)
            os.system('cls')
        else:
            print(Colorate.Color(Colors.red, "Erreur lors de la récupération des données de la vidéo TikTok."))

if __name__ == "__main__":
    tiktok_url = input("Veuillez entrer l'URL de la vidéo TikTok : ")
    fetch_tiktok_data(tiktok_url)

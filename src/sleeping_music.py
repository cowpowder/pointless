
import urllib.parse
import subprocess
import requests
import time
import schedule

def autoplay_sleeping_music():
    path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    query = 'sleeping music'
    encoded_query = urllib.parse.quote(query)

    url = f"https://www.youtube.com/results?search_query={encoded_query}&sp=EgJAAQ%253D%253D"

    response = requests.get(url).text
    b_list = []
    for i in response.split(','):
        if "/watch?v" in i:
            b_list.append(i)

    tmp = b_list[0].split("/watch?v")[1]
    play_url = "https://www.youtube.com/watch?v"+tmp

    subprocess.Popen([path, play_url])

schedule.every().day.at("22:45").do(autoplay_sleeping_music)


while True:
    schedule.run_pending()
    time.sleep(1)

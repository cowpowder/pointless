
import urllib.parse
import subprocess
import requests
import time
import schedule


def open_url():
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

def play(some_time):
    schedule.every().day.at(some_time).do(open_url)

    while True:
        schedule.run_pending()
        time.sleep(1)


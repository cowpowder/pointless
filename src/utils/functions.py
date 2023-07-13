
import urllib.parse
import subprocess
import requests
import time
import schedule
import datetime

path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def open_url(path):

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

def play_youtube(some_time):
    schedule.every().day.at(some_time).do(open_url)

    while True:
        schedule.run_pending()
        time.sleep(1)


def set_alarm(alarm_time, path=path):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            url = 'https://www.youtube.com/watch?v=GWXLPu8Ky9k&ab_channel=TheMSsoundeffects'
            subprocess.Popen([path, url])
            break
        time.sleep(1)  # Check the time every second
        
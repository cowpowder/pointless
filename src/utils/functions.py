
import urllib.parse
import subprocess
import requests
import time
import schedule
import datetime
import os

class Func:
    def __init__(self):
        self.path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    def open_url():
        func.set_volume(vol=5)
        path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
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

    def play_youtube(self, some_time):
        schedule.every().day.at(some_time).do(Func.open_url)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def set_volume(self, vol, *args):
        os.system("""osascript -e 'set volume {}'""".format(vol))

    def set_alarm(self, alarm_time):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                func.set_volume(vol=7)
                print("Wake up!")
                url = 'https://www.youtube.com/watch?v=GWXLPu8Ky9k&ab_channel=TheMSsoundeffects'
                subprocess.Popen([self.path, url])
                break
            time.sleep(1)  # Check the time every second

func = Func()
from src.utils.functions import set_alarm
import sys
              
if __name__ == "__main__":

    command = sys.argv[0]

    if len(sys.argv) >= 3 and sys.argv[1] == '--time' or  sys.argv[1] == '-t':

        alarm_time = sys.argv[2] + ":00"

        alarm_hour = int(alarm_time.split(':')[0])
        alarm_minute = int(alarm_time.split(':')[1])

        if 0 <= alarm_hour < 24 and 0 <= alarm_minute < 60:
            print(f"Alarm set for {alarm_time}")
            set_alarm(alarm_time)

    else:
        print("Invalid parameter, try -t or --time")
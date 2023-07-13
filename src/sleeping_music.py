import sys
from src.scripts.sleeping_music import play

if __name__ == "__main__":

    command = sys.argv[0]

    if len(sys.argv) >= 3 and sys.argv[1] == '--time' or  sys.argv[1] == '-t':
        some_time = sys.argv[2]
        print(f"Setting youtube autoplay 'sleeping music' at {some_time} everyday.")
        play(some_time)
        
    else:
        print("Invalid parameter, try -t or --time")


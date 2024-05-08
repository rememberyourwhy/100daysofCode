import os
import time

path_to_watch = r"C:\Users\Hii\AppData\Roaming\Anki2\User 1\collection.media"
OUTPUT_PATH = r"C:\Users\Hii\PycharmProjects\100daysofCode\Day_60\Output\TXT\watch_events_output.txt"

before = dict([(f, None) for f in os.listdir(path_to_watch)])

with open(OUTPUT_PATH, mode="w"):
    pass
while 1:
    time.sleep(10)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if f not in before]
    removed = [f for f in before if f not in after]
    if added:
        print("Added: ", ", \n".join(added))
        with open(OUTPUT_PATH, mode="a") as finished_output:
            if added:
                for file_name in added:
                    if file_name[-4:] == ".mp3":
                        finished_output.write(file_name)
                        finished_output.write("\n")
            else:
                continue

    if removed:
        print("Removed: ", ", \n".join(removed))
    before = after

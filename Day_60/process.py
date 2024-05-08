#
# pydub example
# from pydub import AudioSegment
# dir_path = r"C:\Users\Hii\AppData\Roaming\Anki2\User 1\collection.media"
# path1 = dir_path + r"\17124369136770957.mp3"
# path2 = dir_path + r"\17124369103510984.mp3"
# sound1 = AudioSegment.from_file(path1, format="mp3")
# sound2 = AudioSegment.from_file(path2, format="mp3")
#
# # sound1 6 dB louder
# louder = sound1 + 6
#
#
# # sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
# combined = sound1 + sound2
#
# # simple export
# file_handle = combined.export("./Output/output.mp3", format="mp3")

import os
from pydub import AudioSegment


# --------------------------------------- AUDIO SETTINGS --------------------------------------- #
REPLAY_TIMES = 3
WAITING_TIME_INNER_LOOPED_SEGMENT = 1500
WAITING_TIME_BETWEEN_LOOPED_SEGMENT = 3000  # in millisecond
SILENT_START = 1000
SILENT_END = 1000


# --------------------------------------- FILE NAMES & FILE PATHS --------------------------------------- #
# FILE_NAME = "QUEEN_OF_TEARS_part_1"
# FILE_NAME = "INTERVIEW  EP28 Doctor Slump Park Hyung sik Park Shin hye part 7"
# FILE_NAME = "INTERVIEW__EP14_Lee_Jeong_eun__Park_Bo_young part 2"
# FILE_NAME = "INTERVIEW_EP_32_Kim_Soo_hyun_Kim_Ji_won_Salon_Drip_2 part 1"
# FILE_NAME = "Hyel club Park Hyung sik Park Shin hye part 2"
# FILE_NAME = "Hyel club Miyeon part 2"
# FILE_NAME = "Doraemon s15 ep 1 part 3"
# FILE_NAME = "Ddeun ddeun IU part 1"
# FILE_NAME = "HEOPOP 돌멩이 part 2"
# FILE_NAME = "HEOPOP 요즘 로봇청소기 part 1"
# FILE_NAME = "HEOPOP 붕어빵 part 2"
# FILE_NAME = "RUNON_EP_1_part_3"
FILE_NAME = "HEOPOP 통치즈"

YOUTUBE_LINK = "https://www.youtube.com/watch?v=294Z8yobbxA"

FILE_NAME = FILE_NAME.replace(' ', '_')

SUBTITLES_OUT_PATH = fr"C:\Users\Hii\PycharmProjects\100daysofCode\Day_60\Output\Audio\{FILE_NAME}.txt"
AUDIO_OUT_PATH = fr"C:\Users\Hii\PycharmProjects\100daysofCode\Day_60\Output\Audio\{FILE_NAME}.mp3"

SUBTITLES_IN_PATH = r"C:\Users\Hii\Documents\randomsub.txt"


# --------------------------------------- RUN ONLY SETTINGS --------------------------------------- #

# RUN_ONLY_FILE_NAME = "INTERVIEW__EP14_Lee_Jeong_eun__Park_Bo_young_part_2"
RUN_ONLY_FILE_NAME = "Hyel_club_Shinee_Key_part_2"
# RUN_ONLY_FILE_NAME = "QUEEN_OF_TEARS_part_1"
# RUN_ONLY_FILE_NAME = "INTERVIEW__EP29_Key_and_Hyunyoung_Joo_Salon_Drip_2_part_4" #1
# RUN_ONLY_FILE_NAME = "INTERVIEW__EP28_Doctor_Slump_Park_Hyung_sik_Park_Shin_hye_part_5"
# RUN_ONLY_FILE_NAME = "Doraemon_s15_ep_1_part_3"
RUN_ONLY_SUBTITLES_OUT_PATH = fr"C:\Users\Hii\PycharmProjects\100daysofCode\Day_60\Output\Audio\{RUN_ONLY_FILE_NAME}.txt"
RUN_ONLY_AUDIO_OUT_PATH = fr"C:\Users\Hii\PycharmProjects\100daysofCode\Day_60\Output\Audio\{RUN_ONLY_FILE_NAME}.mp3"


# --------------------------------------- PROCESS --------------------------------------- #

dir_path = r"C:\Users\Hii\AppData\Roaming\Anki2\User 1\collection.media"

with open(r"C:\Users\Hii\PycharmProjects\100daysofCode\Day_60\Output\TXT\watch_events_output.txt",
          mode="r") as audio_name_input_file:
    file_names_no_dir = audio_name_input_file.readlines()
file_names_w_dir = [(dir_path + "\\" + no_dir_path[:-1]) for no_dir_path in file_names_no_dir]


def process_audio():

    sounds = []
    for file_path in file_names_w_dir:
        sounds.append(AudioSegment.from_file(file_path, format="mp3"))

    combined = AudioSegment.empty()
    combined += AudioSegment.silent(duration=SILENT_START)

    for sound in sounds:
        multiplied_sound = (sound + AudioSegment.silent(duration=WAITING_TIME_INNER_LOOPED_SEGMENT)) * REPLAY_TIMES
        combined += multiplied_sound
        combined += AudioSegment.silent(duration=WAITING_TIME_BETWEEN_LOOPED_SEGMENT)

    combined += AudioSegment.silent(duration=SILENT_END)

    combined.export(AUDIO_OUT_PATH, format="mp3")


def process_text():
    with open(SUBTITLES_IN_PATH, mode="r", encoding="utf-8") as subtitles_file:
        subtitles = subtitles_file.read()
    with open(SUBTITLES_OUT_PATH, mode="w", encoding="utf-8") as text_out_file:
        text_out_file.write(subtitles)
        for name in file_names_no_dir:
            text_out_file.write(f"\n{name}")


def process():
    process_audio()
    process_text()


# --------------------------------------- RUN --------------------------------------- #
def run_text_and_audio():
    os.startfile(SUBTITLES_OUT_PATH)
    os.startfile(AUDIO_OUT_PATH)


def run_only():
    os.startfile(RUN_ONLY_SUBTITLES_OUT_PATH)
    os.startfile(RUN_ONLY_AUDIO_OUT_PATH)


# --------------------------------------- MAIN --------------------------------------- #
process()
run_text_and_audio()
# run_only()

import os
import pysubs2
import time
from faster_whisper import WhisperModel


def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result

    return wrapper


@time_function
def transcribe_audio_to_srt(model, file_path, output_path):
    """Transcribe a single audio file to an SRT file."""

    ####################################
    # Modify this
    ####################################

    segments, info = model.transcribe(file_path,
                                      beam_size=5,
                                      initial_prompt="",
                                      language="ko",
                                      condition_on_previous_text=False,
                                      vad_filter=True,
                                      vad_parameters=dict(min_silence_duration_ms=500)
                                      )

    subs = pysubs2.SSAFile()
    for segment in segments:
        start = int(segment.start * 1000)  # milliseconds
        end = int(segment.end * 1000)
        event = pysubs2.SSAEvent(start=start, end=end, text=segment.text)
        subs.append(event)
    subs.save(output_path, encoding='utf-8')
    print(
        f"Transcribed '{os.path.basename(file_path)}' to '{output_path}'. Detected language: {info.language} with probability {info.language_probability:.2f}")


@time_function
def process_folder(input_folder, output_folder, model):
    """Process all audio files in the specified folder."""
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.mp3', '.wav', '.m4a', '.flac', '.ogg', '.opus')):
            file_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.srt')
            transcribe_audio_to_srt(model, file_path, output_path)


def main():
    ####################################
    # Modify this
    ####################################

    model_size = "tiny"

    model = WhisperModel(model_size,
                         device="cuda",
                         compute_type="int8_float16"
                         )

    input_folder = fr"C:\Users\Hii\Downloads\Video"
    output_folder = fr"C:\Users\Hii\Downloads\Video"
    process_folder(input_folder, output_folder, model)


if __name__ == "__main__":
    main()

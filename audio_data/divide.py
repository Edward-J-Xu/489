from pydub import AudioSegment
import os

def divide_audio(input_file, output_directory, num_segments=10):
    audio = AudioSegment.from_file(input_file)

    segment_duration = len(audio) // num_segments

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration

        segment = audio[start_time:end_time]

        output_file = os.path.join(output_directory, f"segment_{i + 1}.wav")
        segment.export(output_file, format="wav")


    # # Call the function to divide the audio
    # divide_audio(input_audio_file, output_directory, num_segments)

if __name__ == "__main__":

    for name in ["crepe", "dio", "harvest", "pm", "rmvpe", "original"]:
        input_audio_file = f"source/{name}.wav"
        if name == "original":
            input_audio_file = f"source/{name}.mp3"
        output_directory = f"sun/{name}"

        num_segments = 20

        divide_audio(input_audio_file, output_directory, num_segments)

        print(f"Audio divided into {num_segments} segments and saved in {output_directory}")
    # input_audio_file = f"source/original.mp3"
    # output_directory = f"sun/original"

    # # Number of segments to divide the audio into
    # num_segments = 20

    # # Call the function to divide the audio
    # divide_audio(input_audio_file, output_directory, num_segments)

    # print(f"Audio divided into {num_segments} segments and saved in {output_directory}")

import os
from pydub import AudioSegment
AudioSegment.converter = r"C:\Users\TM3070Ti\Downloads\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
folderPath = r"C:\Users\TM3070Ti\Music\Messiah PCH 2023\Pieces\wav"
print(os.listdir(folderPath))
files = os.listdir(folderPath)
print(files)
 
for file in files:
    InputFileName = f"{folderPath}\{file}"
    newAudio = AudioSegment.from_wav(InputFileName)
    newAudio.converter = r"C:\Users\TM3070Ti\Downloads\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
    outputFileName = InputFileName.replace('wav','mp3')
    newAudio.export(outputFileName, format="mp3")
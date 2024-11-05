@echo off
setlocal enabledelayedexpansion

:: Define the path where your videos are stored
set "video_folder=D:\Samay\OutPut"

:: Define the path to the Arial font (ensure the path is correct)
set "font_path=C:\\Windows\\Fonts\\arial.ttf"

:: Output folder
set "output_folder=D:\Samay\LabeledParts"

:: Check if output directory exists, create if necessary
if not exist "%output_folder%" mkdir "%output_folder%"

:: Loop through the video parts
for /l %%i in (14,1,67) do (
    set "part_name=Part %%i"
    echo Processing Part %%i...

    :: Define the input and output file paths with quotes
    set "input_file=%video_folder%\Part_%%i.mkv"
    set "output_file=%output_folder%\Labeled_Part_%%i.mkv"

    :: Debugging: Echo input and output paths
    echo Input: "!input_file!"
    echo Output: "!output_file!"

    :: Use FFmpeg to add text overlay at top-center with specified font
    ffmpeg -i "!input_file!" -vf "drawtext=text='!part_name!':fontfile='!font_path!':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=30" -codec:a copy "!output_file!"

    echo Finished processing Part %%i
)

echo All parts processed!
pause

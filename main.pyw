# Keyboard Shortcut Notifier
# Created By Jack Levin 
# 1/17/2022

# Imports
import pygame
import keyboard
import time
from pathlib import Path

# Start pygame
pygame.mixer.init()
run = True

# Key Combos
copy = "ctrl+c" # Copied
paste = "ctrl+v" # Pasted
cut = "ctrl+x" # Cutted
caps_lock = "caps_lock" # Caps lock on and off
undo = "ctrl+z" # Undo
redo = "ctrl+y" # Redo
select_all = "ctrl+a" # Select all
close_program = "alt+f4" # Closed Program
find = "ctrl+f" # Find Text
print_doc = "ctrl+p" # Print Document

# Input List
inputs = [copy, paste, cut, undo, redo, select_all, close_program, find, print_doc, caps_lock]

# Audio folder path
audio_folder_path = Path(__file__).with_name("sfx")

# Audio combo paths
copy_sfx = str(audio_folder_path) + "/copy.mp3"
paste_sfx = str(audio_folder_path) + "/paste.mp3"
cut_sfx = str(audio_folder_path) + "/cut.mp3"
caps_lock_on_sfx = str(audio_folder_path) + "/caps_lock_on.mp3"
caps_lock_off_sfx = str(audio_folder_path) + "/caps_lock_off.mp3"
undo_sfx = str(audio_folder_path) + "/undo.mp3"
redo_sfx = str(audio_folder_path) + "/redo.mp3"
select_all_sfx = str(audio_folder_path) + "/select_all.mp3"
close_program_sfx = str(audio_folder_path) + "/close_program.mp3"
find_sfx = str(audio_folder_path) + "/find.mp3"
print_doc_sfx = str(audio_folder_path) + "/print.mp3"
volume_up_sfx = str(audio_folder_path) + "/volume_up.mp3"
volume_down_sfx = str(audio_folder_path) + "/volume_down.mp3"
volume_max_sfx = str(audio_folder_path) + "/volume_max.mp3"
volume_min_sfx = str(audio_folder_path) + "/volume_min.mp3"
exit_sfx = str(audio_folder_path) + "/exit.mp3" 
mute_sfx = str(audio_folder_path) + "/mute.mp3" 
unmute_sfx = str(audio_folder_path) + "/unmute.mp3"
audio_is_muted_sfx = str(audio_folder_path) + "/audio_is_muted.mp3"
audio_sfx = str(audio_folder_path) + "/audio.mp3"
first_boot_sfx = str(audio_folder_path) + "/first_boot.mp3"

# Audio List
audio_list = [copy_sfx, paste_sfx, cut_sfx, undo_sfx, redo_sfx, select_all_sfx, close_program_sfx, find_sfx, print_doc_sfx, caps_lock_on_sfx, caps_lock_off_sfx]

#Variables
    # Set for Caps lock off when program runs
caps_lock_toggle = 1
volume = 0.5
mute_toggle = 1
first_boot = False
run = False

# Functions
def verify_input(key):
    if keyboard.is_pressed(key) == True:
        print(str(key) + " is true")
    else:
        print(str(key) + " is false")

def play_audio(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)

if first_boot == False:
    play_audio(first_boot_sfx)
    first_boot = True

if first_boot == True:
    run = True

while run == True:
    time.sleep(0.1)
    
# Main loop for audio to play when keyshorcut is pressed

    # All normal key shortcuts 
    for key_combo in range(len(inputs)):
        if keyboard.is_pressed(inputs[key_combo]) == True:
            time.sleep(0.2)
            if keyboard.is_pressed(inputs[key_combo]) == True:
                pass
            else:
                if mute_toggle % 2 == 0:
                    pygame.mixer.music.set_volume(volume)
                    play_audio(audio_is_muted_sfx)
                    
                    time.sleep(4)
                    pygame.mixer.music.set_volume(0)
                else:
                    play_audio(audio_list[key_combo])

# Special Actions

        # Caps Lock 
        if keyboard.is_pressed(inputs[9]):
            time.sleep(0.2)
            caps_lock_toggle += 1
            if caps_lock_toggle % 2 == 0: 
                if mute_toggle % 2 == 0:
                    pygame.mixer.music.set_volume(volume)
                    play_audio(audio_is_muted)
                else:
                    play_audio(audio_list[9])
            else:
                if mute_toggle % 2 == 0:
                    pygame.mixer.music.set_volume(volume)
                    audio_play(audio_is_muted_sfx)
                else:
                    play_audio(audio_list[10])


        # Volume Up
    if keyboard.is_pressed("ctrl") == True and keyboard.is_pressed("up") == True:
        time.sleep(0.2)
        if keyboard.is_pressed("ctrl") == True and keyboard.is_pressed("up") == True:
            pass
        else:
            if mute_toggle % 2 == 0:
                    pygame.mixer.music.set_volume(volume)
                    play_audio(audio_is_muted_sfx)
            else:
                volume += 0.1

                if volume > 1.0:
                    volume = 1.0

                if volume != 1.0 and mute_toggle % 2 != 0:
                    play_audio(volume_up_sfx)
                    pygame.mixer.music.set_volume(volume)
                if volume == 1.0:
                    play_audio(volume_max_sfx)


        # Volume Down
    if keyboard.is_pressed("ctrl") == True and keyboard.is_pressed("down") == True:
        time.sleep(0.2)
        if keyboard.is_pressed("ctrl") == True and keyboard.is_pressed("down") == True:
            pass
        else:
            if mute_toggle % 2 == 0:
                    pygame.mixer.music.set_volume(volume)
                    play_audio(audio_is_muted_sfx)
            else:
                volume += -0.1

                if volume < 0.1:
                    volume = 0.1

                if volume != 0.1 and mute_toggle % 2 != 0:
                    play_audio(volume_down_sfx)
                    pygame.mixer.music.set_volume(volume)
                if volume == 0.1:
                    play_audio(volume_min_sfx)
                
        # Mute Audio
    if keyboard.is_pressed("ctrl") == True and keyboard.is_pressed("m") == True:
        time.sleep(0.2)
        if keyboard.is_pressed("ctrl") == True and keyboard.is_pressed("m") == True:
            pass
        else:
            mute_toggle += 1
            if mute_toggle % 2 == 0:
                play_audio(mute_sfx)
                time.sleep(0.6)

                play_audio(audio_sfx)
                time.sleep(0.6)

                pygame.mixer.music.set_volume(0)
            else:
                pygame.mixer.music.set_volume(volume)
                play_audio(unmute_sfx)
                
                time.sleep(0.6)
                play_audio(audio_sfx)
                

        # Closing Program
    if keyboard.is_pressed("esc") == True:
        time.sleep(1.5)
        if keyboard.is_pressed("esc") == True:
            pygame.mixer.music.set_volume(volume)
            play_audio(exit_sfx)

            time.sleep(2)
            exit()
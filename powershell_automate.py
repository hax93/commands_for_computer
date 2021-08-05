"""some function for open, read logs and
select directory where we have all scripts"""
import subprocess
import pyautogui as py
import time

def powershell_open(locate_powershell):
    # for find location powershell use this: (Get-Process -Id $pid).Path
    subprocess.Popen(f'{locate_powershell}', shell=True)
    py.hotkey('winleft', 'up') #maximize window
    time.sleep(1)

def commands_with_log(locate_folder, locate_txt, command):
    time.sleep(3)
    py.write(f'cd {locate_folder}'), py.hotkey('enter')
    time.sleep(2)

    py.write(f'Start-Transcript -Path {locate_txt}'), py.hotkey('enter')
    py.write(f"{command}"), py.hotkey('enter')

    py.write('Stop-Transcript'), py.hotkey('enter')

def back_directory(locate_folder):
    py.write(f'cd {locate_folder}'), py.hotkey('enter')
    time.sleep(2)

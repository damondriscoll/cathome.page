import os
import shutil

directory = os.path.dirname(os.path.abspath(__file__))

gif_files = [f for f in os.listdir(directory) if f.endswith('.gif')]

for index, file_name in enumerate(gif_files, start=1):
    new_name = f'cat{index}.gif'
    old_path = os.path.join(script_directory, file_name)
    new_path = os.path.join(script_directory, new_name)
    shutil.move(old_path, new_path)
    print(f'Renamed {file_name} to {new_name}')

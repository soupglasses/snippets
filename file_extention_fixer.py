"""
# Image file extention fixer

image_extention_fixer.py - Fix wrong image file extentions.

Usage:
    Create a "photos" folder  where the python file is located. Put all files
    you want to try to fix into the "photos" folder.

    Open a terminal window in the folder where this python file is located and
    run: `python3 image_extention_fixer.py` or `python image_extention_fixer.py`
    (without the `)

    You will see copies of your files in a new "output" folder.

    You may also get some failed files, which will be shown at the end of
    running this script. You may manually try to fix theese yourself. Or they
    might not be pictures at all.
"""
import imghdr
import os
import shutil

photo_dir = os.path.join(os.getcwd(), 'photos')
output_dir = os.path.join(os.getcwd(), 'output')

os.makedirs(photo_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

failed_files = []

for root, _, files in os.walk(photo_dir):
    for file in files:
        path_to_output = os.path.join(
            output_dir,
            os.path.relpath(root, start=photo_dir)
        )
        os.makedirs(path_to_output, exist_ok=True)

        file_ext = imghdr.what(os.path.join(root, file))
        file_name = os.path.splitext(file)[0]

        file_src = os.path.join(root, file)
        file_dst = os.path.join(path_to_output, f"{file_name}.{file_ext}")

        if file_ext:
            print(f'{os.path.relpath(file_src)} '.ljust(40, '-')
                  + f'-> {os.path.relpath(file_dst)}')
            shutil.copyfile(file_src, file_dst)
        else:
            failed_files.append(file_src)
if failed_files:
    print('\nFailed to move files:')
    print('\n'.join(failed_files))

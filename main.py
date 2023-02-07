import os
import shutil
import tempfile
from argparse import ArgumentParser

import functions as f

# parser = ArgumentParser(description="Modify old recorder package by new. Fixed for STADA project")
# parser.add_argument("--path", help="Full path of the folder where bot export .zip files are located")
# args = parser.parse_args()
# path = str(args.path)
path = r"C:\Users\Andoni_Aguirre_Arang\Desktop\TEST_RECORDER_CHANGER"
os.chdir(path)

for filename in os.listdir(os.getcwd()):
    print(filename)
    full_file_path = os.path.join(os.getcwd(), filename)
    filename_no_extension = os.path.splitext(full_file_path)[0].split('\\')[-1]
    with tempfile.TemporaryDirectory() as temp_dir:
        # 1) Unzip
        f.unzip(full_file_path, temp_dir)
        # 2) Modify
        f.modify_bot_export(temp_dir)
        # 3) ZIP folder again (overwriting original .zip file)
        shutil.make_archive(filename_no_extension, 'zip', temp_dir)

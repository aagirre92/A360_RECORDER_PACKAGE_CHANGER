import os
import shutil
from argparse import ArgumentParser

import functions as f

parser = ArgumentParser(description="Modify old recorder package by new. Fixed for STADA project")
parser.add_argument("--path", help="Full path of the folder where bot export .zip files are located")
args = parser.parse_args()
path = str(args.path)
os.chdir(path)

for filename in os.listdir(os.getcwd()):
    print(filename)

    full_file_path = os.path.join(os.getcwd(), filename)
    filename_no_extension = os.path.splitext(full_file_path)[0].split('\\')[-1]
    print(filename_no_extension)
    print(full_file_path)
    # 1) Unzip
    print(os.path.splitext(full_file_path)[0])
    f.unzip(full_file_path, os.path.splitext(full_file_path)[0])
    # 2) Modify
    f.modify_bot_export(os.path.splitext(full_file_path)[0])
    # 3) ZIP (overwriting)
    shutil.make_archive(filename_no_extension, 'zip', os.path.splitext(full_file_path)[0])
    # 4) Delete folder
    shutil.rmtree(filename_no_extension)

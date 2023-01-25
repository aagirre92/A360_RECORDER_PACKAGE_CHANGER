import json
import io
import os
import re
import zipfile


def unzip(path_to_zip_file, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))


def get_task_bot_paths(manifest_json_path):
    # RETURN LIST WITH ABSOLUTE PATHS TO TASK BOT FILES
    with io.open(manifest_json_path, 'r', encoding='utf-8-sig') as f:
        manifest_json = json.load(f)

    task_bot_paths = []
    for file in manifest_json["files"]:
        if file["contentType"] == "application/vnd.aa.taskbot":
            task_bot_paths.append(os.path.join(os.path.dirname(manifest_json_path), file["path"]))

    return task_bot_paths


def modify_bot_export(bot_export_file_path):
    manifest_path = os.path.join(bot_export_file_path, "manifest.json")
    task_bot_paths = get_task_bot_paths(manifest_path)
    new_recorder_version = "2.9.2-20221122-181034"
    old_recorder_version_1 = "2.0.10-20201222-083014"
    old_recorder_version_2 = "2.1.0-20210311-002508"
    # 1) MODIFY BOT FILES TO REPLACE 'OLD' RECORDER BY NEW
    for file in task_bot_paths:
        with io.open(file, 'r', encoding='utf-8-sig') as f:
            contents = json.load(f)
        contents_str = json.dumps(contents).replace(old_recorder_version_1, new_recorder_version)
        contents_str = json.dumps(contents).replace(old_recorder_version_2, new_recorder_version)
        with open(file, 'w') as f:
            f.write(contents_str)

    # 2) DELETE 'RECORDER' PACKAGE FROM MANIFEST.JSON
    with io.open(manifest_path, 'r', encoding='utf-8-sig') as f:
        manifest_json = json.load(f)
        
    elements_to_remove=["Recorder"]
    manifest_json["packages"] = [d for d in manifest_json["packages"] if d['name'] not in elements_to_remove]

    with open(manifest_path, "w") as f:
        f.write(json.dumps(manifest_json))

    # 3) DELETE THE POTENTIAL RECORDER .JAR FILES
    pattern = "bot-command-recorder-.*\.jar"
    purge(bot_export_file_path, pattern)
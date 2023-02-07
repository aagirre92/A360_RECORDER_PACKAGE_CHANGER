# INTRO
This script has the aim of substituting following 'Recorder' package versions:

* bot-command-recorder-2.0.10-20201222-083014.jar
* bot-command-recorder-2.1.0-20210311-002508.jar

By the newest one at this date (2.9.2-20221122-181034)

# USAGE (powershell)
The script accepts one key argument called --path, which indicates a folder where all
bot exports (.zip) files are located
```
.\main.py --path="C:\....\BOT_EXPORT_PATH"

```

For each file in that folder script will:
* Unzip to a (temporary) folder
* With the folder it will:
  * Loop through all bot files and change the recorder package
  * Change the manifest.json file to remove the recorder key
* It will zip the modified files, overwriting the original zip file

Finally script will delete **all the recorder packages within the exported folder, following
this regex pattern: "bot-command-recorder-.*\.jar"**
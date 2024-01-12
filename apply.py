import glob
import os
import pathlib
import subprocess
import shutil
import sys

if not sys.platform == "linux":
    print("This code can be only executed from linux")
    sys.exit(0)

CURRENT_DIRECTORY = os.path.realpath(os.path.dirname(__file__))

# Apply font files
FONT_DIRECTORY = pathlib.Path(CURRENT_DIRECTORY, "fonts")
for file in FONT_DIRECTORY.glob("*py"):
    subprocess.call(["python", file])


# Work with config directory
CONFIG_DIRECTORY = pathlib.Path(CURRENT_DIRECTORY, ".config")
for file in CONFIG_DIRECTORY.glob("**/*"):
    if not file.is_file():
        continue

    new_config_file = file.relative_to(CURRENT_DIRECTORY)
    old_config_file = os.path.expanduser("~/" + new_config_file)
    if os.path.isfile(old_config_file):
        ask = input(
            f"Old config file for {new_config_file}. Do you want to replace?"
        ).lower()
        if "n" in ask:
            continue

        shutil.move(src=new_config_file, dst=old_config_file)

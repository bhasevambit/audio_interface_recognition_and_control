# Audio Interface Recognition and Control

This repository is Audio Interface and Sound Device Test Code.

## Python Version

This repository is used "**Python 3.11**".
I recommend setting up "**venv**" with python version = "3.11".
venv setup is below commands.

`python -m venv .venv`

## pip Requirements

pip requirements install command is below.

`pip install -r ./requirements.txt`

## Usage

- **All Audio Device Listing (Microphone/Speaker)**

  ```
  python check_All-Audio-Device.py
  ```

- **Microphone Device Listing**

  ```
  python check_Audio-Input-Device.py
  ```

- **Speaker Device Listing**
  ```
  python check_Audio-Output-Device.py
  ```

## Note

This repository is used direnv.
Please install `direnv` and execute `direnv allow` commands at Repository Top directory.
(If you use Windows, please execute `.\.venv\Scripts\activate` commands)

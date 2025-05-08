# Audio Interface Recognition and Control

This repository is Audio Interface and Sound Device Test Code.

## Usage

### python environment deployment

```
cd "$(git rev-parse --show-toplevel)"

python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### python execution

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

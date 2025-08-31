cd docs
cd tools
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 rename-folder.py 'PR-FAQ' "$images" "$images2" 
python3 rename-folder.py '../PR-FAQ' '4 ⚙️ ⏳ Solution' '4 ⚙️ Solution'
python3 rename-folder.py '../PR-FAQ/4 ⚙️ Solution' '00 Intro' '1 Solution intro'
python3 rename-folder.py '../PR-FAQ/4 ⚙️ Solution' '6 💼 Biz edge blocks' '6 💼 Biz edge blocks'
python3 rename-folder.py '../PR-FAQ' '3.8 🕓 User Timeline' '3.8 🕓 User Timeline'
python3 rename-folder.py '../PR-FAQ' '3.8 🕓 User Timeline' '3.8 🕓 User Timeline'
python3 unquote.py # remove % symbols
python3 malformed-links.py
python3 malformed-links.py > malformed-links.md 

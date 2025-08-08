cd docs
cd tools
python rename-folder.py 'PR-FAQ' "$images" "$images2" 
python rename-folder.py '../PR-FAQ' '4 ⚙️ ⏳ Solution' '4 ⚙️ Solution'
python rename-folder.py '../PR-FAQ/4 ⚙️ Solution' '00 Intro' '1 Solution intro'
python rename-folder.py '../PR-FAQ/4 ⚙️ Solution' '6 💼 Biz edge blocks' '6 💼 Biz edge blocks'
python rename-folder.py '../PR-FAQ' '3.8 🕓 User Timeline' '3.8 🕓 User Timeline'
python rename-folder.py '../PR-FAQ' '3.8 🕓 User Timeline' '3.8 🕓 User Timeline'
python unquote.py # remove % symbols
python malformed-links.py
python malformed-links.py > malformed-links.md 

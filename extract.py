import glob
import os
import sys

for f in glob.glob("out/__output__.*"):
    os.remove(f)

cmd = """
yt-dlp\
    -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"\
    -o out/__output__\
    --download-sections "*%(start)s-%(end)s"\
    --force-keyframes-at-cuts\
    "%(vid)s"
"""

vid, start, end = sys.argv[1:]

meta = {"vid": vid, "start": start, "end": end}
os.system(cmd % meta)

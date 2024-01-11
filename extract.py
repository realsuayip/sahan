import glob
import os
import sys

for f in glob.glob("out/__output__.*"):
    os.remove(f)

cmd = """
yt-dlp\
    -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"\
    -S vcodec:h264\
    -o out/__output__\
    --download-sections "*%(start)s-%(end)s"\
    --force-keyframes-at-cuts\
    --concurrent-fragments 4\
    "%(vid)s"
"""


def to_seconds(value: str) -> float:
    # 1:27 -> 87.0
    # 1:27.5 -> 87.5
    # 27 -> 27.0
    try:
        return float(value)
    except ValueError:
        m, s = value.split(":")
        return (int(m) * 60) + float(s)


def main() -> None:
    vid, start, end = sys.argv[1:4]
    meta = {
        "vid": vid,
        "start": to_seconds(start),
        "end": to_seconds(end),
    }
    os.system(cmd % meta)
    os.system("open out/__output__.mp4")


if __name__ == "__main__":
    main()

# fix_train.py
from pathlib import Path
import pandas as pd

# project root = location of this file
ROOT = Path(__file__).resolve().parent
DATA_CSV = ROOT / "data" / "processed" / "mock_lyrics.csv"
TRAIN_TXT = ROOT / "data" / "processed" / "train.txt"

df = pd.read_csv(DATA_CSV)
df = df[df["lyrics"].notna()]
df = df[df["lyrics"].str.len() > 10]

with TRAIN_TXT.open("w", encoding="utf-8") as f:
    for lyric in df["lyrics"]:
        for line in str(lyric).splitlines():
            line = line.strip()
            if line:
                f.write(line + "\n")
        f.write("\n")

print(f"Wrote training text to {TRAIN_TXT} with {len(df)} samples.")

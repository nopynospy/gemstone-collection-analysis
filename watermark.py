import os
import cv2
import pandas as pd
import json

os.makedirs("docs/assets/thumbnails", exist_ok=True)
os.makedirs("docs/assets/figures", exist_ok=True)

# 1. Generate downscaled, watermarked web thumbnail
def make_web_thumbnail(input_path, output_path, max_width=480):
    img = cv2.imread(input_path)
    if img is None:
        return
    h, w = img.shape[:2]
    scale = max_width / float(w)
    resized = cv2.resize(img, (max_width, int(h * scale)), interpolation=cv2.INTER_AREA)
    
    # Burn-in subtle watermark
    cv2.putText(resized, "TOM LOV DM9 / SPECIMEN ANALYSIS", (15, int(h * scale) - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Save as compressed JPEG
    cv2.imwrite(output_path, resized, [cv2.IMWRITE_JPEG_QUALITY, 75])

make_web_thumbnail("data/raw/tigers_eye/tiger_diffused_001.png", "docs/assets/thumbnails/specimen_a_thumb.jpg")
make_web_thumbnail("data/raw/tigers_eye_side_b/tiger_b_001.png", "docs/assets/thumbnails/specimen_b_thumb.jpg")

# 2. Convert CSV to web-ready JSON for GitHub Pages
df = pd.read_csv("tigers_eye_characterization.csv")
records = df.to_dict(orient="records")
with open("docs/data.json", "w") as f:
    json.dump(records, f, indent=2)

print("Web assets prepared in ./docs/")
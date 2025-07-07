import base64

with open("ai-news-sheet-ea23a0541b63.json", "rb") as f:
    encoded = base64.b64encode(f.read()).decode("utf-8")

with open("encoded.txt", "w") as out:
    out.write(encoded)

print("✅ Successfully created encoded.txt. Copy this string into Render.")

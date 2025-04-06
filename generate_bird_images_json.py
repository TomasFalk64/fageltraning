import os
import json

# Går igenom mappen birdPicts och skriver lista i birdImages.json
# Behövs för att index.html ska hitta bilder i mappen

def generate_image_list(image_folder="birdPicts", output_file="birdImages.json"):
    supported_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

    image_files = [
        filename for filename in os.listdir(image_folder)
        if os.path.splitext(filename)[1].lower() in supported_extensions
    ]

    image_files.sort(key=lambda x: x.lower())  # Sortera alfabetiskt, skiftlägesokänsligt

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(image_files, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(image_files)} sorterade bildfiler sparades till '{output_file}'.")

generate_image_list()

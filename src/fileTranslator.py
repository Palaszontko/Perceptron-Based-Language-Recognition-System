import os
import json
import requests
from pathlib import Path

base_dir = Path("data")
polish_dir = base_dir / "polish"
language_dirs = {
    "cs": base_dir / "czech",
    "en": base_dir / "english",
    "de": base_dir / "german",
    "it": base_dir / "italian",
    "es": base_dir / "spanish"
}

language_codes = {
    "cs": "czech",
    "en": "english",
    "de": "german",
    "it": "italian",
    "es": "spanish"
}

def translate_text(text, target_lang):
    url = "http://localhost:5001/translate"
    payload = {
        "q": text,
        "source": "pl",
        "target": target_lang,
        "format": "text",
        "alternatives": 1,
        "api_key": ""
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status() 
        result = response.json()
        return result.get("translatedText", "")
    except Exception as e:
        print(f"Error during translation to {target_lang}: {e}")
        return ""

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        file_name = file_path.stem
        file_extension = file_path.suffix
        
        for lang_code, lang_dir in language_dirs.items():
            os.makedirs(lang_dir, exist_ok=True)
            
            translated_text = translate_text(content, lang_code)
            
            if translated_text:
                new_file_name = f"{file_name.split('_')[0]}_{lang_code}{file_extension}"
                output_path = lang_dir / new_file_name
                
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(translated_text)
                    
                print(f"Saved translation to {output_path}")
            else:
                print(f"Failed to translate {file_path} to {language_codes[lang_code]}")
    
    except Exception as e:
        print(f"Error while processing file {file_path}: {e}")

def main():
    if not polish_dir.exists() or not polish_dir.is_dir():
        print(f"The folder {polish_dir} does not exist!")
        return
    
    for file_path in polish_dir.glob('*.txt'):
        if "test" in file_path.name:
            print(f"Processing file: {file_path}")
            process_file(file_path)
    
    print("File translation completed.")

if __name__ == "__main__":
    main()

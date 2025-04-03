# Perceptron-Based Language Recognition System

## Overview

This repository contains a **Perceptron-Based Language Recognition System**, designed to identify the language of a given text input. The project employs machine learning techniques, specifically the perceptron algorithm, to classify text into predefined language categories. It also includes a file translation feature, leveraging Docker and LibreTranslate for seamless language translation.

### Key Features
- **Language Detection**: Uses a perceptron-based model to classify text into languages.
- **File Translation**: Allows users to translate text files between supported languages using LibreTranslate (Helps with collecting train data).
- **Extensible Design**: The system can be expanded with additional languages or features.

---

## Installation and Setup

### Prerequisites
1. Python 3.x installed on your system.
2. (optional) Docker installed for the file translation feature. 

### Clone the Repository
```
git clone https://github.com/Palaszontko/Perceptron-Based-Language-Recognition-System.git
cd Perceptron-Based-Language-Recognition-System
```

## File Translation with LibreTranslate

To use the file translation functionality, you must set up LibreTranslate using Docker. Follow these steps:

1. **Pull the LibreTranslate Docker Image**
```
docker pull libretranslate/libretranslate
```
2. **Run LibreTranslate**
   (on mac port 5000 is used by some kind of AirPlay service so I used 5001)
```
docker run -it --rm -p 5001:5000 libretranslate/libretranslate --load-only en,cs,de,pl,it,es
```
This command starts LibreTranslate with support for the following languages:
- English (`en`)
- Czech (`cs`)
- German (`de`)
- Polish (`pl`)
- Italian (`it`)
- Spanish (`es`)

3. Once the container is running, you can use the `fileTranslator` script in this repository to translate files.

## Usage

### Language Detection
1. Place your text data in the `data` folder or provide a path to your input file.
2. Run the main script to detect the language:
```
python src/language_detector.py
```

### File Translation
1. Ensure that LibreTranslate is running as described above.
2. Use the `fileTranslator` script to translate your files (whole idea is to put your files in data/polish folder using name_pl.txt format and then fileTranslator will translate it to other languages. It makes collecting learining data easier :) ):
```
python3 src/fileTranslator.py
```

## Project Structure
```
Perceptron-Based-Language-Recognition-System/
├── data/ # Folder for input (training) files
├── src/ # Source code for language detection and translation
│ ├── language_detector.py # Main script for language recognition
│ ├── fileTranslator.py # Script for file translation using LibreTranslate
├── test/ # Folder with files to test network 
└── README.md # Project documentation (this file)
```
## Supported Languages

The system currently supports:
- English (`en`)
- Czech (`cs`)
- German (`de`)
- Polish (`pl`)
- Italian (`it`)
- Spanish (`es`)

More languages can be added by extending the training dataset or configuring LibreTranslate.

---


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

---

## License

This project is open-source and available under the [MIT License](LICENSE).














# Anki Thai Writing Practice Script

This script generates a daily **Thai Writing Practice Worksheet** from Anki cards. It selects up to **15 words** (or fewer if there aren't enough), creates a **PDF worksheet**, and then prompts the user to **grade each word** based on difficulty.

## Features
- **Fetch due cards** from your Anki deck.
- **Fallback to all cards** if no due cards are available.
- **Randomly selects 15 words** for the worksheet.
- **Generates a PDF** where you can write Thai translations.
- **Prompts for grading** after practice (1 = Again, 2 = Hard, 3 = Good, 4 = Easy).
- **Updates Anki** with your difficulty ratings.

## Requirements
- Python 3
- [AnkiConnect](https://ankiweb.net/shared/info/2055492159) installed in Anki (Anki plugin required)
- Required Python libraries:
  ```sh
  pip install -r requirements.txt
  ```

## Usage
1. **Start Anki** and ensure AnkiConnect is running.
2. **Run the script**:
   ```sh
   python writer.py
   ```
3. **Print the generated PDF** (`anki_writing_worksheet.pdf`) and write the translations.
4. **Enter difficulty ratings** when prompted.
5. **Anki updates automatically** based on your responses.

## Customization
- Change `DECK_NAME` to match your Anki deck:
  ```python
  DECK_NAME = "Your Deck Name"
  ```
- Adjust the number of words per day:
  ```python
  WORDS_COUNT = 20 
  ```

## Example Output
```
PDF generated: anki_writing_worksheet.pdf

### Grade Each Word ###
1 = Again (forgot), 2 = Hard (struggled), 3 = Good (normal), 4 = Easy (knew instantly)
1. apple: 3
2. banana: 4
...
All words graded and updated in Anki!
```

## Notes
- Ensure Anki is **running** before executing the script.
- The script **prioritizes due cards** but falls back to all cards if none are due.
- Spaced repetition is maintained by **updating Anki with difficulty ratings**.

## License
This script is free to use and modify.

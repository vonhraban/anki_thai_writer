import json
import requests
import random
from fpdf import FPDF

ANKI_CONNECT_URL = "http://localhost:8765"
DECK_NAME = "Thai Writing"
WORDS_COUNT = 15

def get_cards():
    # First try to get due cards
    payload = {
        "action": "findCards",
        "version": 6,
        "params": {
            "query": f'deck:"{DECK_NAME}" is:due'
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload).json()
    due_cards = response.get("result", [])

    # Fallback - if no due cards, fetch all cards in the deck
    if not due_cards:
        payload["params"]["query"] = f'deck:"{DECK_NAME}"'  # Get all cards
        response = requests.post(ANKI_CONNECT_URL, json=payload).json()
        due_cards = response.get("result", [])

    return due_cards

def get_card_info(card_ids):
    payload = {
        "action": "cardsInfo",
        "version": 6,
        "params": {
            "cards": card_ids
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload).json()
    return response.get("result", [])

def set_review_grade(card_id, grade):
    payload = {
        "action": "answerCards",
        "version": 6,
        "params": {
            "answers": [
                {
                    "cardId": card_id,
                    "ease": grade  # 1 = Again, 2 = Hard, 3 = Good, 4 = Easy
                }
            ]
        }
    }
    requests.post(ANKI_CONNECT_URL, json=payload)

# Fetch due cards
card_ids = get_cards()
if not card_ids:
    print("No cards found!")
    exit()

cards = get_card_info(card_ids)
word_map = {card["fields"]["Front"]["value"]: card["cardId"] for card in cards}

# Select WORDS_COUNT words
selected_words = random.sample(list(word_map.keys()), min(WORDS_COUNT, len(word_map)))

# Time to generate the PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, "Thai Writing Practice", ln=True, align='C')
pdf.ln(10)
pdf.set_font("Arial", size=12)

for i, word in enumerate(selected_words, 1):
    pdf.cell(0, 10, f"{i}. {word} ___________________________", ln=True)

pdf.output("anki_writing_worksheet.pdf")
print("PDF generated: anki_writing_worksheet.pdf")

# Step 5: Grade each word after writing
print("\n### Grade Each Word ###")
print("1 = Again (forgot), 2 = Hard (struggled), 3 = Good (normal), 4 = Easy (knew instantly)")

for i, word in enumerate(selected_words, 1):
    while True:
        try:
            grade = int(input(f"{i}. {word}: "))
            if grade in [1, 2, 3, 4]:
                card_id = word_map[word]
                set_review_grade(card_id, grade)
                break
            else:
                print("Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 4.")

print("All words graded and updated in Anki!")

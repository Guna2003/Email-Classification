import re
import spacy
import subprocess

def ensure_spacy_model():
    try:
        spacy.load("en_core_web_sm")
    except OSError:
        print("Downloading spaCy model...")
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

ensure_spacy_model()
nlp = spacy.load("en_core_web_sm")

def detect_regex_entities(text):
    entities = []

    patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b\d{10,12}\b',
        'aadhar': r'\b\d{4}\s\d{4}\s\d{4}\b',
        'expiry': r'\b(0[1-9]|1[0-2])\/?([0-9]{2})\b',
        'cvv': r'\b[0-9]{3}\b',
    }

    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            entities.append({
                'start': match.start(),
                'end': match.end(),
                'entity': match.group(),
                'label': label
            })

    return entities

def detect_name_entities(text):
    entities = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities.append({
                'start': ent.start_char,
                'end': ent.end_char,
                'entity': ent.text,
                'label': 'name'
            })
    return entities

def mask_pii(text):
    regex_entities = detect_regex_entities(text)
    name_entities = detect_name_entities(text)
    all_entities = regex_entities + name_entities

   
    entities_sorted = sorted(all_entities, key=lambda x: x['start'])

    masked_text = ""
    current_pos = 0
    for ent in entities_sorted:
        start, end = ent['start'], ent['end']
        label = ent['label'].upper()

        if start >= current_pos:  
            masked_text += text[current_pos:start] + f"<{label} MASKED>"
            current_pos = end

    
    masked_text += text[current_pos:]

    return masked_text, all_entities

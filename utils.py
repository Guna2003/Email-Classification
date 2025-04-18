import re

def detect_entities(text):
    entities = []

    patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b\d{10,12}\b',
        'name': r'\b(John Doe|Gunasekhar|Vaishnavi)\b',
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

def mask_pii(text):
    entities = detect_entities(text)
    entities_sorted = sorted(entities, key=lambda x: x['start'], reverse=True)
    for ent in entities_sorted:
        label = ent['label'].upper()
        text = text[:ent['start']] + f"<{label} MASKED>" + text[ent['end']:]
    return text, entities

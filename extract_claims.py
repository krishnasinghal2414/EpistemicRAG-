
import re

def extract_claims(document_id, text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    claims = []

    for sentence in sentences:
        sentence = sentence.strip()

        if sentence:
            claims.append({
                "id": "C" + str(len(claims) + 1),
                "document_id": document_id,
                "text": sentence
            })

    return claims

document = {
    "id": "D1",
    "source": "Library Schedule",
    "content": "The library opens at 9 AM. It closes at 6 PM."
}

claims = extract_claims(document["id"], document["content"])

for claim in claims:
    print(claim)

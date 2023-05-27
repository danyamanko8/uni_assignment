import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def get_emotional_color(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    polarities = []
    for sentence in sentences:
        blob = TextBlob(sentence)
        polarity = blob.sentiment.polarity
        polarities.append(polarity)

    average_polarity = sum(polarities) / len(polarities)
    if average_polarity > 0:
        return "Positive"
    elif average_polarity < 0:
        return "Negative"
    else:
        return "Neutral"


text = input("Enter the text: ")

emotional_color = get_emotional_color(text)

print("Emotional Color: " + emotional_color)

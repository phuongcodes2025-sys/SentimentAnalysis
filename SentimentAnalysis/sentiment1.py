from collections import Counter

from dataset import load_dataset
from tokenizer import tokenize

# Come up with some terms the
# represent positive sentiment
# and negative sentiment
SENTIMENT_TERMS = {
    "bad": "negative",
    "good": "positive",
}


def main():
    texts, labels = load_dataset("dataset.json")

    for text, label in zip(texts, labels):
        # For each text, tokenize it and then
        # count the number of positive and negative
        # terms
        counts = Counter()
        tokens = tokenize(text)
        for token in tokens:
            if token in SENTIMENT_TERMS:
                counts[SENTIMENT_TERMS[token]] += 1

        positive_count = counts.get("positive", 0)
        negative_count = counts.get("negative", 0)

        # Is this the best? How do we handle neutral
        # (no sentiment) tweets?
        # Is 1 positive and 2 negative a negative tweet?
        sentiment = positive_count - negative_count
        if sentiment > 0:
            predicted = "positive"
        elif sentiment < 0:
            predicted = "negative"
        else:
            predicted = "neutral"

        print(f"{text}: predicted={predicted} actual={label}")

    # Calculate the accuracy (number of correctly predicted / total examples)
    acc = 0
    print(f"Accuracy = {acc:.2f}")


if __name__ == "__main__":
    main()

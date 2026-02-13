from dataset import load_dataset
from naive_bayes import SimpleNaiveBayes


def main():
    texts, labels = load_dataset("dataset.json")

    classifier = SimpleNaiveBayes()

    # To test our model we want to separate our
    # data into training (what the model sees)
    # and testing (what the model does not see)
    # to determine how well it will do on new
    # data
    split = int(len(texts) * 0.8)
    training_texts = texts[:split]
    training_labels = labels[:split]
    test_texts = texts[split:]
    test_labels = labels[split:]

    # Train the model
    classifier.train(training_texts, training_labels)

    # Check the predictions
    for text, label in zip(test_texts, test_labels):
        prediction = classifier.predict(text)
        print(text, label, prediction)

    # Calculate the accuracy (number of correctly predicted / total examples)
    acc = 0
    print(f"Accuracy = {acc:.2f}")


if __name__ == "__main__":
    main()

import math

from tokenizer import tokenize


class SimpleNaiveBayes:
    def __init__(self):
        self.log_priors = {}
        self.word_probs = {}
        self.vocab = set()
        self.classes = set()

    def train(self, documents, labels):
        self.classes = set(labels)

        class_counts = {c: 0 for c in self.classes}
        word_counts = {c: {} for c in self.classes}
        total_docs = len(documents)

        for doc, label in zip(documents, labels):
            class_counts[label] += 1
            words = tokenize(doc)

            for word in words:
                self.vocab.add(word)
                if word not in word_counts[label]:
                    word_counts[label][word] = 0
                word_counts[label][word] += 1

        # Calculate Log Priors (The baseline probability of a class)
        # We use Log to avoid "arithmetic underflow" (multiplying tiny numbers)
        for c in self.classes:
            self.log_priors[c] = math.log(class_counts[c] / total_docs)

        # Calculate Word Likelihoods (P(word | class)) with Laplace Smoothing
        # Smoothing adds +1 to counts so unseen words don't crash the probability to 0
        self.word_probs = {c: {} for c in self.classes}

        for c in self.classes:
            total_words_in_class = sum(word_counts[c].values())
            vocab_size = len(self.vocab)

            for word in self.vocab:
                count = word_counts[c].get(word, 0)
                # (Count + 1) / (Total Words in Class + Unique Vocab Size)
                probability = (count + 1) / (total_words_in_class + vocab_size)
                self.word_probs[c][word] = math.log(probability)

    def predict(self, text):
        words = tokenize(text)
        scores = {c: self.log_priors[c] for c in self.classes}

        for word in words:
            if word in self.vocab:
                for c in self.classes:
                    scores[c] += self.word_probs[c][word]
        best_class = max(scores, key=scores.get)  # type: ignore
        return best_class

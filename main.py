import math
from collections import Counter
from text_preprocess import preprocess_text, load_articles

# File paths
REAL_PATH = "data/real_news.txt"
FAKE_PATH = "data/fake_news.txt"


# =========================
# TRAIN MODEL
# =========================
def train_model():
    real_data = load_articles(REAL_PATH)
    fake_data = load_articles(FAKE_PATH)

    if not real_data or not fake_data:
        print("Error: Dataset not found or empty.")
        return None

    real_words = []
    fake_words = []

    for line in real_data:
        real_words.extend(preprocess_text(line))

    for line in fake_data:
        fake_words.extend(preprocess_text(line))

    real_counts = Counter(real_words)
    fake_counts = Counter(fake_words)

    total_real = sum(real_counts.values())
    total_fake = sum(fake_counts.values())

    vocab = set(real_words + fake_words)
    vocab_size = len(vocab)

    print("\nModel trained successfully!")
    print(f"Vocabulary size: {vocab_size}")

    return real_counts, fake_counts, total_real, total_fake, vocab_size


# =========================
# PREDICTION
# =========================
def predict(text, real_counts, fake_counts, total_real, total_fake, vocab_size):
    words = preprocess_text(text)

    if not words:
        return "Invalid input", 0, []

    real_score = math.log(0.5)
    fake_score = math.log(0.5)

    contributions = []

    for word in words:
        real_prob = (real_counts.get(word, 0) + 1) / (total_real + vocab_size)
        fake_prob = (fake_counts.get(word, 0) + 1) / (total_fake + vocab_size)

        real_score += math.log(real_prob)
        fake_score += math.log(fake_prob)

        contributions.append((word, real_prob, fake_prob))

    # Avoid overflow issue (IMPORTANT FIX)
    max_score = max(real_score, fake_score)
    real_prob_final = math.exp(real_score - max_score)
    fake_prob_final = math.exp(fake_score - max_score)

    total = real_prob_final + fake_prob_final
    real_final = real_prob_final / total
    fake_final = fake_prob_final / total

    prediction = "FAKE NEWS 🚨" if fake_final > real_final else "REAL NEWS ✅"
    confidence = max(real_final, fake_final)

    # Sort by impact
    contributions.sort(key=lambda x: abs(x[2] - x[1]), reverse=True)

    return prediction, confidence, contributions[:5]


# =========================
# SHOW STATS
# =========================
def show_stats(real_counts, fake_counts):
    print("\nTop REAL words:")
    for word, count in real_counts.most_common(5):
        print(f"{word} → {count}")

    print("\nTop FAKE words:")
    for word, count in fake_counts.most_common(5):
        print(f"{word} → {count}")


# =========================
# TEST FROM FILE
# =========================
def test_from_file(real_counts, fake_counts, total_real, total_fake, vocab_size):
    path = input("Enter file path: ")

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            print("\nInput:", line.strip())

            prediction, confidence, _ = predict(
                line, real_counts, fake_counts, total_real, total_fake, vocab_size
            )

            print("Prediction:", prediction)
            print(f"Confidence: {confidence:.2f}")

    except Exception as e:
        print("Error reading file:", e)


# =========================
# MAIN MENU
# =========================
def main():
    model = train_model()

    if model is None:
        return

    real_counts, fake_counts, total_real, total_fake, vocab_size = model

    while True:
        print("\n===== Fake News Detection System =====")
        print("1. Test News")
        print("2. Show Word Statistics")
        print("3. Test from File")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            text = input("\nEnter news text: ")

            prediction, confidence, words = predict(
                text, real_counts, fake_counts, total_real, total_fake, vocab_size
            )

            print("\n--- RESULT ---")
            print("Prediction:", prediction)
            print(f"\nProcessed words: {words}")
            print(f"Confidence: {confidence:.2f}")

            print("\nReason:")
            for word, r, f in words:
                if f > r:
                    print(f"- '{word}' → contributes strongly to FAKE classification")
                else:
                    print(f"- '{word}' → contributes strongly to REAL classification")

        elif choice == "2":
            show_stats(real_counts, fake_counts)

        elif choice == "3":
            test_from_file(real_counts, fake_counts, total_real, total_fake, vocab_size)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()
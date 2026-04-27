📌 Fake News Detection System

A ground-up Python project that implements a Naive Bayes–based text classifier from scratch, without using any external machine learning libraries.
This project focuses on understanding core ML concepts, probability, and text processing through first-principles implementation.

💡 Why This Project
Demonstrates machine learning fundamentals without libraries
Implements Naive Bayes classifier manually
Shows text processing and feature extraction skills
Applies probability theory to real-world problems
Highlights clean coding and modular design
📋 Project Overview

This system classifies news articles as:

👉 REAL NEWS ✅
👉 FAKE NEWS 🚨

using a probabilistic approach based on Naive Bayes classification.

⚙️ Tech Stack
Python (Core only)
Data Structures (Dictionaries, Lists, Sets)
Probability & Statistics
Command Line Interface (CLI)
🎯 Key Features
1. Custom Naive Bayes Classifier
Word frequency–based learning
Conditional probability: P(word | class)
Laplace smoothing for unseen words
Log probabilities for stability
2. Text Preprocessing Pipeline
Lowercase conversion
Punctuation removal
Tokenization
Stopword removal (custom implementation)
3. Intelligent Classification Output
Predicts REAL / FAKE
Confidence score
Shows top contributing words
Transparent reasoning
4. Interactive CLI
Test custom news input
View word statistics
Batch test from file
Simple menu-driven interface
📁 Project Structure
fake-news-detector/
├── main.py
├── text_preprocess.py
├── data/
│   ├── real_news.txt
│   └── fake_news.txt
├── README.md
🚀 Getting Started
Prerequisites
Python 3.7+
Run the Project
cd fake-news-detector
python main.py
📖 How It Works
🔹 Training Phase
Load real & fake datasets
Preprocess text
Build word frequency dictionaries
Calculate probabilities
🔹 Prediction Phase

For a new input:

Preprocess input text
Compute probabilities for:
Real
Fake
Apply Naive Bayes:
P(class | text) ∝ P(class) × Π P(word | class)
Choose class with highest probability
📊 Example Output
Input:
Government announces new healthcare initiative
Output:
Prediction: REAL NEWS ✅
Confidence: 0.87

Reason:
- 'government' strongly indicates REAL
- 'announces' strongly indicates REAL
Input:
Aliens secretly found living underground
Output:
Prediction: FAKE NEWS 🚨
Confidence: 0.94

Reason:
- 'aliens' strongly indicates FAKE
- 'secretly' strongly indicates FAKE
🧠 Algorithm Summary
Naive Bayes classification
Assumes word independence
Uses Laplace smoothing
Uses log probabilities
📈 Performance Notes
Fast due to dictionary-based computation
Accuracy depends on dataset quality
Lightweight and efficient
🔒 Limitations
Assumes independence between words
Small dataset → limited accuracy
No deep semantic understanding
English-only support
🚀 Future Improvements
TF-IDF weighting
N-grams (bigrams/trigrams)
Larger dataset
Web interface (Flask)
Real-time news analysis
🎓 Learning Outcomes

This project demonstrates:

Probability & Bayes’ theorem
Text preprocessing techniques
Feature extraction
Algorithm design from scratch
Core NLP fundamentals
📌 Project Status

✅ Completed core implementation
🔄 Open for future improvements

🎉 Conclusion

This project shows that machine learning systems can be built from first principles using only Python.
It emphasizes understanding over dependency, making it a strong foundation for advanced ML and NLP work.

📄 License

Educational use — free to modify and extend.
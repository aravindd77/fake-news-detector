📌 Fake News Detection System

A ground-up educational project that implements a Naive Bayes-based text classification system using only core Python concepts. No external machine learning libraries are used, making it a strong demonstration of fundamental ML principles, probability theory, and text processing techniques.

💡 Why This Project
Demonstrates understanding of core Machine Learning principles without using ML libraries
Implements Naive Bayes classifier from scratch using probability theory
Shows ability to process and analyze text data programmatically
Builds strong foundation for Natural Language Processing (NLP) concepts
Highlights problem-solving and algorithm design skills
📋 Project Overview

This system classifies news articles as "Fake" or "Real" using a probabilistic approach inspired by the Naive Bayes algorithm.

It demonstrates:

Probability theory and conditional probability
Text preprocessing and feature extraction
Custom machine learning logic from scratch
Clean modular Python programming
Data-driven decision making
⚙️ Tech Stack
Python (Core)
Data Structures (Dictionaries, Lists, Sets)
Probability & Statistics (Naive Bayes concept)
Command Line Interface (CLI)
🎯 Key Features
1. Custom Naive Bayes Classifier
Word frequency-based probability calculation
Conditional probability estimation P(word | category)
Laplace smoothing to handle unseen words
Log probability for numerical stability
2. Text Preprocessing Pipeline
Lowercase conversion
Punctuation removal
Tokenization (word splitting)
Stopword removal using custom list
3. Classification with Insights
Binary classification: Real or Fake
Confidence score for predictions
Explanation of important contributing words
Transparent reasoning for results
4. Interactive CLI System
Train model on dataset
Test custom news input
View word statistics
Save/load trained model
Easy menu-driven interface
5. Model Persistence
Save trained model using JSON
Load previously trained models
No external serialization libraries used
📁 Project Structure
fake-news-detector/
├── main.py                 # Entry point and CLI interface
├── classifier.py           # High-level classification logic
├── model.py               # Naive Bayes implementation
├── text_preprocess.py     # Text cleaning & preprocessing
├── utils.py               # Helper functions
├── data/
│   ├── real_news.txt      # Training data (real articles)
│   └── fake_news.txt      # Training data (fake articles)
└── README.md              # Project documentation
🚀 Getting Started
Prerequisites
Python 3.7+
Run the Project
cd fake-news-detector
python main.py
📖 How It Works
1. Training Phase
Input: Labeled dataset (real & fake news)
Process:
Clean and tokenize text
Remove stopwords
Build word frequency dictionary
Compute prior probabilities
Output: Trained probabilistic model
2. Prediction Phase

For a new article:

Preprocess text
Compute probability for each class:
Real
Fake
Apply Naive Bayes formula:
P(class | text) ∝ P(class) × Π P(word | class)
Use log probabilities to avoid underflow
Choose class with highest score
📊 Example Output
Input:
Government announces new healthcare initiative for public welfare
Output:
Prediction: REAL
Confidence: 87.3%

Top contributing words:
- government
- announces
- healthcare
Input:
Aliens secretly found living under pyramid structures worldwide
Output:
Prediction: FAKE
Confidence: 94.1%

Top contributing words:
- aliens
- secretly
- pyramid
🧠 Algorithm Summary
Uses Naive Bayes classification
Assumes independence between words
Applies Laplace smoothing for unseen words
Uses log probabilities for numerical stability
📈 Performance Notes
Fast execution due to dictionary-based computation
Accuracy depends on quality and size of dataset
Lightweight memory usage
Scalable with larger datasets
🔒 Limitations
Assumes word independence (Naive assumption)
Limited dataset size affects accuracy
No deep contextual understanding
Works only on English text
Simple frequency-based features only
🚀 Future Improvements
Implement TF-IDF weighting
Add n-gram (bigram/trigram) support
Improve dataset size and diversity
Build web interface using Flask
Add real-time news scraping
Introduce sentiment analysis
📌 Project Status

Completed as an educational implementation of Naive Bayes classification from scratch.
Currently focused on improving dataset quality and expanding features.

🎓 Learning Outcomes

This project helped in understanding:

Probability and Bayes’ theorem
Text preprocessing techniques
Feature extraction from raw text
Algorithm design from scratch
Modular Python programming
Basics of Natural Language Processing
📄 License

This is an educational project created for learning purposes. Free to use and modify.

🎉 Conclusion

This project demonstrates that machine learning concepts can be implemented from first principles using only Python. It focuses on understanding how ML works internally, rather than relying on external libraries.

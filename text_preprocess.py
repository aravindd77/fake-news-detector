"""
preprocess.py
Text preprocessing module for cleaning and tokenizing articles.
Demonstrates core Python text processing without external libraries.
"""

import string


# Define common stopwords that don't contribute much to classification
STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'is', 'was', 'are', 'be', 'been', 'being', 'have', 'has', 'had',
    'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
    'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it',
    'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why', 'how',
    'as', 'if', 'by', 'from', 'up', 'about', 'out', 'into', 'through', 'with'
}


def remove_punctuation(text):
    """
    Remove punctuation from text.
    
    Args:
        text (str): Input text string
        
    Returns:
        str: Text without punctuation
    """
    # Use string.punctuation to get all punctuation characters
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def lowercase_text(text):
    """
    Convert text to lowercase.
    
    Args:
        text (str): Input text string
        
    Returns:
        str: Lowercase text
    """
    return text.lower()


def tokenize(text):
    """
    Split text into words (tokens).
    
    Args:
        text (str): Input text string
        
    Returns:
        list: List of word tokens
    """
    # Split by whitespace and return non-empty tokens
    tokens = text.split()
    return [token for token in tokens if token]  # Remove empty strings


def remove_stopwords(tokens):
    """
    Remove common stopwords from token list.
    
    Args:
        tokens (list): List of word tokens
        
    Returns:
        list: Tokens with stopwords removed
    """
    return [token for token in tokens if token not in STOPWORDS]


def preprocess_text(text):
    """
    Complete preprocessing pipeline.
    Apply all cleaning steps in sequence.
    
    Args:
        text (str): Raw input text
        
    Returns:
        list: Cleaned and tokenized words
    """
    # Step 1: Convert to lowercase
    text = lowercase_text(text)
    
    # Step 2: Remove punctuation
    text = remove_punctuation(text)
    
    # Step 3: Tokenize into words
    tokens = tokenize(text)
    
    # Step 4: Remove stopwords
    tokens = remove_stopwords(tokens)
    
    return tokens


def load_articles(file_path):
    """
    Load articles from a file (one article per line).
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        list: List of article strings
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read all lines and remove trailing newlines
            articles = [line.strip() for line in file.readlines()]
            # Filter out empty lines
            articles = [article for article in articles if article]
            return articles
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []

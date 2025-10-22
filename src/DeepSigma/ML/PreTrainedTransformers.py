from transformers import pipeline
from typing import List, Dict

# Supported models mapping
MODEL_CHOICES: Dict[str, str] = {
    "distilbert": "distilbert-base-uncased-finetuned-sst-2-english",
    "bert": "nlptown/bert-base-multilingual-uncased-sentiment",
    "roberta": "cardiffnlp/twitter-roberta-base-sentiment"
}


def analyze_sentiment(text: str, model_name: str = "distilbert") -> List[Dict]:
    """
    Perform sentiment analysis on a text input using a selected model.

    Args:
        text (str): Input text to analyze.
        model_name (str): Key from MODEL_CHOICES to select the model.

    Returns:
        List[Dict]: Sentiment analysis result(s).
    """
    if not text.strip():
        raise ValueError("Input text cannot be empty.")

    if model_name not in MODEL_CHOICES:
        raise ValueError(f"Unsupported model '{model_name}'. Choose from: {list(MODEL_CHOICES.keys())}")

    # Load the selected model
    model_id = MODEL_CHOICES[model_name]
    classifier = pipeline("sentiment-analysis", model=model_id)

    # Run sentiment analysis
    result = classifier(text)
    return result
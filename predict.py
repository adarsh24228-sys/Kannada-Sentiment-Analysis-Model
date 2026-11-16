import os
import sys

# Ensure root directory is on the path.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from agents.prediction_agent import PredictionAgent


def main() -> None:
    """
    Quick CLI prediction utility as described in the project guide.
    """
    model_dir = "models"
    
    if not os.path.exists(model_dir):
        print(f"[ERROR] Models directory '{model_dir}' not found. Please train the model first with 'python train.py'.")
        sys.exit(1)

    print("[CLI Predictor] Initializing PredictionAgent...")
    try:
        agent = PredictionAgent(model_dir=model_dir)
    except Exception as exc:
        print(f"[ERROR] Failed to initialize PredictionAgent: {exc}")
        sys.exit(1)

    # Hardcoded test sentences from the project guide.
    test_sentences = [
        "ನಾನು ತುಂಬಾ ಸಂತೋಷವಾಗಿದ್ದೇನೆ",  # happy
        "ನನಗೆ ತುಂಬಾ ದುಃಖವಾಗಿದೆ",        # sad
        "ಇದು ತುಂಬಾ ಕೋಪ ತರಿಸುತ್ತದೆ",    # anger
        "ಅದು ತುಂಬಾ ಭಯಂಕರವಾಗಿದೆ",      # fear
        "ಇದು ತುಂಬಾ ಅಸಹ್ಯವಾಗಿದೆ",        # disgust
        "ಇಂದು ಹವಾಮಾನ ಸಾಮಾನ್ಯವಾಗಿದೆ"    # neutral
    ]

    print("\n--- Running Predictions on Guide Examples ---")
    results = agent.predict_texts(test_sentences)

    for res in results:
        print(f"\nText       : {res['text']}")
        print(f"Cleaned    : {res['cleaned']}")
        print(f"Sentiment  : {str(res['sentiment']).upper()}")
        print(f"Confidence : {res['confidence']:.2f}%")
    print("\n---------------------------------------------")


if __name__ == "__main__":
    main()

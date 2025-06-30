import matplotlib.pyplot as plt
import json

def plot_entropy(prediction, threshold=4.0):
    path = prediction["path"]
    entropy = prediction["entropy"]

    plt.figure(figsize=(12, 5))
    plt.plot(entropy, marker='o', color='blue', label='Entropy')
    plt.xticks(range(len(path)), path, rotation=45)
    plt.axhline(y=threshold, color='red', linestyle='--', label=f'Threshold = {threshold}')
    
    # Mark sentence end positions where entropy exceeds threshold
    added_label = False
    for i, val in enumerate(entropy):
        if val >= threshold:
            plt.axvline(x=i, color='green', linestyle=':', label='Sentence End' if not added_label else "")
            plt.text(i, val + 0.2, '⬆', ha='center', va='bottom', color='green', fontsize=12)
            added_label = True

    plt.title(f"Sentence ID {prediction['sentence_id']} Entropy Plot")
    plt.xlabel("Token")
    plt.ylabel("Entropy")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage
with open("outputs/predicted_boundaries.json") as f:
    preds = json.load(f)

plot_entropy(preds[0])

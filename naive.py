from collections import defaultdict

# -----------------------------
# Training Data
# -----------------------------
data = [
    {"fever": "yes", "cough": "yes", "disease": "flu"},
    {"fever": "yes", "cough": "no",  "disease": "flu"},
    {"fever": "yes", "cough": "yes", "disease": "flu"},
    {"fever": "no",  "cough": "yes", "disease": "cold"},
    {"fever": "no",  "cough": "yes", "disease": "cold"},
]

# -----------------------------
# Training Function
# -----------------------------
def train_naive_bayes(data):
    class_counts = defaultdict(int)
    feature_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    total = len(data)

    for row in data:
        cls = row["disease"]
        class_counts[cls] += 1

        for feature in ["fever", "cough"]:
            value = row[feature]
            feature_counts[cls][feature][value] += 1

    return class_counts, feature_counts, total

# -----------------------------
# Prediction Function
# -----------------------------
def predict(class_counts, feature_counts, total, sample):
    best_class = None
    best_score = -1

    for cls in class_counts:

        # Prior probability P(Class)
        score = class_counts[cls] / total

        # Likelihood P(Features | Class)
        for feature, value in sample.items():
            count = feature_counts[cls][feature][value]
            class_total = class_counts[cls]

            # simple probability (no smoothing here)
            prob = count / class_total if class_total > 0 else 0

            score *= prob

        if score > best_score:
            best_score = score
            best_class = cls

    return best_class, best_score

# -----------------------------
# Train Model
# -----------------------------
class_counts, feature_counts, total = train_naive_bayes(data)

# -----------------------------
# Test Sample
# -----------------------------
sample = {
    "fever": "yes",
    "cough": "yes"
}

# -----------------------------
# Predict
# -----------------------------
prediction, score = predict(class_counts, feature_counts, total, sample)

print("Prediction:", prediction)
print("Score:", score)
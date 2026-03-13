# Function to calculate Precision, Recall and F-Measure
def calculate_metrics(retrieved_set, relevant_set):

    # Calculate True Positive, False Positive, False Negative
    true_positive = len(retrieved_set.intersection(relevant_set))
    false_positive = len(retrieved_set.difference(relevant_set))
    false_negative = len(relevant_set.difference(retrieved_set))

    # Display values
    print("True Positive:", true_positive)
    print("False Positive:", false_positive)
    print("False Negative:", false_negative)
    print()

    # Calculate Precision
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) != 0 else 0

    # Calculate Recall
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) != 0 else 0

    # Calculate F-Measure
    f_measure = (2 * precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    return precision, recall, f_measure


# Predicted (Retrieved) documents
retrieved_set = {"doc1", "doc2", "doc3"}

# Actual relevant documents
relevant_set = {"doc1", "doc4"}

# Calculate metrics
precision, recall, f_measure = calculate_metrics(retrieved_set, relevant_set)

# Display results
print("Precision:", precision)
print("Recall:", recall)
print("F-measure:", f_measure)

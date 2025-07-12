# Protein Methylation Site Prediction

This project implements a deep learning model that predicts whether a given protein sequence is methylated or not. It uses a hybrid CNN-LSTM architecture trained on encoded amino acid sequences to identify methylation patterns with high accuracy.

---

## Objective

Classify protein sequences as methylated (1) or non-methylated (0) based on their amino acid patterns using sequence-based features and deep learning.

---

## Key Features

- Binary classification of sequences (Methylated vs. Non-Methylated)
- Uses BLOSUM62 and physicochemical property-based encoding
- CNN extracts local features; LSTM captures sequential patterns
- Achieves high prediction accuracy (85–90%)
- Performance evaluated with accuracy, precision, recall, and F1-score

---

## Input Format

The model accepts a CSV file in the following format:

```csv
sequence,label
ACDEFGHIKLMNPQRSTVWY,1
MKTLLILAVVVAAILATYAA,0
sequence: String of 21 amino acids (fixed-length, pre-padded or truncated)

label: 1 for methylated, 0 for non-methylated

Model Architecture
Encoding layer using BLOSUM62 and physicochemical properties

Convolutional layers to detect local motifs

LSTM layers to capture long-term dependencies

Dense layer with sigmoid activation for binary output

How to Run
Install requirements:

bash
Copy
Edit
pip install numpy pandas scikit-learn tensorflow matplotlib
Prepare your dataset.csv in the required format.

Run the notebook or script:

bash
Copy
Edit
python train_model.py
Predict methylation status:

python
Copy
Edit
predict_methylation("ACDEFGHIKLMNPQRSTVWY")  # Returns 1 (Methylated) or 0 (Non-Methylated)
Results
Training Accuracy: ~89%

Validation Accuracy: ~85–90%

Performs well on unseen sequences

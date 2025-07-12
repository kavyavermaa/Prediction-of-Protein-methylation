# Protein Methylation Site Prediction

This project is implemented as a Google Colab notebook that predicts whether a given protein sequence is methylated (1) or non-methylated (0). It uses a hybrid CNN-LSTM architecture with custom encoding to analyze amino acid patterns and identify methylation sites with high accuracy.

---

## Objective

To classify protein sequences as methylated (1) or non-methylated (0) using sequence-based features, including BLOSUM62 and physicochemical properties, in a deep learning framework.

---

## Key Features

- Binary classification of sequences (Methylated vs. Non-Methylated)
- BLOSUM62 and physicochemical property-based encoding
- CNN layers to extract local motifs
- LSTM layers to capture sequential dependencies
- Achieves approximately 85–90% prediction accuracy
- Evaluated using accuracy, precision, recall, and F1-score

---

## Input Format

- `sequence`: String of amino acids (fixed-length, pre-padded or truncated as needed)
- `label`: 1 for methylated, 0 for non-methylated

---

## How to Use

1. Upload your `dataset.csv` file to Google Colab.
2. Open the notebook.
3. Follow the cells in order to:
   - Load and preprocess data
   - Encode sequences using BLOSUM62 and physicochemical properties
   - Train the CNN-LSTM model
   - Evaluate model performance
   - Predict methylation status for new sequences

---

## Results

- Training Accuracy: ~89%
- Validation Accuracy: ~85–90%
- Performs well on unseen sequences

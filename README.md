# AI/ML Internship — DecodeLabs (Batch 2026)

This repo contains the 4 projects I completed during my AI/ML internship at DecodeLabs. Each project builds on the last — starting from basic control flow logic and ending with an actual computer vision pipeline. Below is a quick rundown of what each one does and how to run it.

---

## Project 1: Rule-Based AI Chatbot

A simple chatbot that responds to user input using dictionary-based lookup instead of a messy if-elif ladder. Handles greetings, small talk, and a few mood-based follow-ups.

**Concepts covered:** control flow, dictionary lookups (`.get()`), input sanitization, basic pattern matching.

**How to run:**
```bash
python chatbot.py
```
Type anything to chat, or `bye` / `exit` / `quit` to leave.

**A few things worth knowing:**
- Uses `.lower().strip()` so it doesn't care about capitalization or extra spaces.
- Has basic partial matching, so it can catch phrases even if they're not an exact match.
- Remembers the last topic briefly, so if you say something like "I am sad" and then just "why", it responds in context.

---

## Project 2: Data Classification Using AI (Iris Dataset)

A K-Nearest Neighbors classifier trained on the classic Iris dataset to predict flower species based on petal/sepal measurements.

**Concepts covered:** train-test split, feature scaling (StandardScaler), KNN classification, model evaluation (accuracy, confusion matrix, F1 score).

**How to run:**
```bash
python classifier.py
```

**Results:**
- Accuracy: 1.0 on the test set
- F1 Score: 1.0
- All 30 test samples classified correctly (see confusion matrix in the script output)

Note: Iris is a small, well-separated dataset, so near-perfect accuracy is expected here — not a sign of overfitting, just an easy dataset to work with.

---

## Project 3: AI Recommendation Logic (Tech Stack Recommender)

Takes a list of user skills as input and recommends the top 3 most relevant career paths using TF-IDF vectorization and cosine similarity.

**Concepts covered:** TF-IDF weighting, cosine similarity, content-based filtering, ranking and filtering results.

**How to run (notebook, run cells in order):**
```
Cell 1 → imports
Cell 2 → job roles dataset (18 roles)
Cell 3 → user input (edit this to test different skills)
Cell 4 → prepare data for TF-IDF
Cell 5 → vectorization
Cell 6 → cosine similarity scoring
Cell 7 → ranked top-3 output
```

**Example:**
Input: `["Python", "Cloud Computing", "Automation"]`
Output: Cloud Architect, DevOps Engineer, Site Reliability Engineer (in that order, ranked by match score)

To test other skill combinations, just change the `user_skills` list in Cell 3.

---

## Project 4: Image or Text Recognition (OCR)

A basic OCR pipeline that extracts text from an image using Tesseract, with proper image pre-processing and a confidence threshold filter.

**Concepts covered:** image pre-processing (grayscale, Gaussian blur, adaptive thresholding), OCR with pytesseract, confidence-based filtering.

**Requirements:**
- Python packages: `opencv-python`, `pytesseract`
- Tesseract OCR engine installed separately on your system ([Windows installer here](https://github.com/UB-Mannheim/tesseract/wiki))

**How to run:**
```bash
python ocr.py
```
Make sure to update `image_path` in the script to point to your own image, and update `tesseract_cmd` if Tesseract isn't in your system PATH.

**Pipeline:**
```
Raw Image → Grayscale → Gaussian Blur → Adaptive Threshold → Tesseract OCR → Filter by 80% confidence → Output
```

Only words with confidence ≥ 80% are included in the final output, matching the accuracy threshold that was part of the project spec.

---

## Setup (all projects)

```bash
pip install scikit-learn opencv-python pytesseract
```

Each project is self-contained — you don't need to run them in order, though they do get progressively more advanced (rule-based logic → ML classification → recommendation systems → computer vision).

---

## About this internship

4-week AI/ML internship at DecodeLabs (Batch 2026), covering foundational AI engineering concepts — from deterministic logic building to supervised learning to basic computer vision. Each project was designed to build on core concepts before moving into more complex territory like neural networks.

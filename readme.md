# Yarn Count Calculator

A simple and professional Streamlit web application for Textile Engineering students.

## Features

- Calculate yarn count using length and weight.
- Convert between Tex, Denier, dtex, Nm, Ne, Worsted and Yorkshire woollen count.
- Supports meters, kilometers, yards, feet and centimeters.
- Supports grams, kilograms, milligrams, pounds and ounces.
- Displays calculation formulas and conversion results.
- Includes input validation and a responsive layout.

## Technologies

- Python
- Streamlit

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt` and `README.md`.
3. Open https://share.streamlit.io/
4. Sign in with GitHub.
5. Select your repository and branch.
6. Set the main file path to `app.py`.
7. Click Deploy.

## Formula Reference

- Tex = Weight (g) / Length (m) × 1000
- Denier = Weight (g) / Length (m) × 9000
- dtex = Weight (g) / Length (m) × 10000
- Nm = 1000 / Tex
- Ne ≈ 590.541 / Tex

Worsted and Yorkshire woollen conversions use conventional approximate constants.

## Purpose

This application is designed for educational use by textile engineering students.

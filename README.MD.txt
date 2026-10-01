# AI Email & Message Rewriter

An AI-powered application that rewrites emails and messages in different tones using Google's Gemini AI.

## Features

- Rewrite messages using Gemini AI
- Choose between Polite, Direct, and Friendly tones
- Display rewritten messages in the notebook
- Copy rewritten text for use in other applications

## Technologies Used

- Python
- Jupyter Notebook
- Google Gemini API
- ipywidgets
- python-dotenv

## Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's URL.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your Gemini API key

Create a `.env` file in the project folder containing:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own Gemini API key. Never upload your `.env` file to GitHub.

### 4. Run the notebook

Open `AI_Email_Message_Rewriter.ipynb` in Jupyter Notebook and run the cells in order.

## Security

Keep your API key private. Do not commit `.env` files or real API keys to GitHub.
# 🩺 Summer Disease Scraper – Care Health Insurance

## 📝 Project Overview

This scraper extracts structured health information from the [Care Health Insurance blog](https://www.careinsurance.com/blog/health-insurance-articles/most-common-diseases-in-summer-season), a site run by an Indian health insurance provider. The blog outlines the most common diseases during the summer season and provides associated prevention tips.

The script scrapes two core pieces of information:

1. **Disease/Symptom Names** – extracted from `<h3>` tags  
2. **Prevention Tips** – extracted from `<p>` tags that follow a specific pattern and contain phrases like "tips to prevent"

These elements are stored in corresponding lists and presented to the user via a simple terminal interface. The user can choose a disease from a numbered list and receive the related prevention tip based on index alignment between the two scraped lists.

---

## 🌐 Why This Website?

We selected the Care Health Insurance blog because:
- It follows a predictable and clean HTML structure, making it suitable for beginner scraping logic.
- It had not been used by another group.
- It focuses on health education, aligning well with our goal of scraping real-world medical content.

The site uses:
- `<h3>` tags for disease names  
- `<p>` tags with associated text after headers for prevention tips  

This consistency made the scraping process reliable and repeatable.

---

## ⚙️ How to Run This Project

1. (Mac users) If you're using a virtual environment, run:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

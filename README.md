# 🎬 Movie Recommender System

This is a beginner-friendly **Content-Based Movie Recommendation System** built using **Streamlit**, **scikit-learn**, and the **TMDB 5000 Movies Dataset** from Kaggle. The app recommends similar movies based on genres, keywords, and overviews.

---

## ✅ Features

- Select a movie title from a dropdown list
- Get top 5 similar movie recommendations
- View movie descriptions (overviews) for each suggestion
- Built with clean and easy-to-understand ML logic
- Interactive web UI using Streamlit

---

## 🧠 How It Works

1. **Text Preprocessing**  
   Combines the movie's `genres`, `keywords`, and `overview` into one text field.

2. **TF-IDF Vectorization**  
   Converts the combined text into numerical vectors (removes common stopwords like "the", "and", etc).

3. **Cosine Similarity**  
   Measures how similar one movie is to another based on their vectorized text data.

4. **Streamlit Interface**  
   Lets users select a movie and view 5 similar movie recommendations with their overviews.

---
The dataset used for training and testing the sentiment analysis model is included in this repository.

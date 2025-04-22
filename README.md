# Movie-Recommender-System
https://colab.research.google.com/drive/1BMeRqN5PN_2DOOdJGXIMTlYKoZvBxRiJ#scrollTo=YKBIk1Rk2SCi

---
<img width="1470" alt="Screenshot 2025-04-22 at 10 41 53 PM" src="https://github.com/user-attachments/assets/19ae1cbb-5352-4482-98d3-5847d5e396c2" />
<img width="1470" alt="Screenshot 2025-04-22 at 10 42 00 PM" src="https://github.com/user-attachments/assets/37d15129-9a67-4dda-9605-90aa3d02ec2e" />
<img width="1470" alt="Screenshot 2025-04-22 at 10 42 09 PM" src="https://github.com/user-attachments/assets/a83224d2-9ab9-4edc-90d3-bbd157267141" />
<img width="1470" alt="Screenshot 2025-04-22 at 10 42 16 PM" src="https://github.com/user-attachments/assets/67b296a9-9dd1-4499-ad6f-acfa195cac03" />

---
**Data Sources**

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
* movies.csv: Contains metadata such as movie titles, genres, overviews, etc.
* credits.csv: Contains additional details like cast and crew.
---
**Workflow Overview**

1. Data Loading & Merging
2. Feature Engineering
* Extract and clean important metadata:
    * Genres
    * Keywords
    * Cast Members
* Combine all relevant features into a single column called tags.
3. Text Processing
* Remove spaces and special characters.
* Vectorize the text data using CountVectorizer to create feature vectors.
4. Similarity Calculation
* Calculate cosine similarity between all movies based on their tag vectors.
5. Recommendation Function
* Given a movie title, retrieve its most similar movies.
* Display top 5 recommendations.
---
**Output**

* A function to fetch top 5 movie recommendations.
* Cosine similarity matrix for movie similarity.

---
**Tech-Stack**

1.**Data Science & Machine Learning Python** : Core language for data processing and modeling.
Pandas: Data manipulation.
NumPy: Numerical computations.


2.**Scikit-learn** : i.CountVectorizer - Text vectorization , ii.cosine_similarity - To measure movie similarity.


3.**NLTK** : For advanced text preprocessing like stemming.


4.**Streamlit** : for basic web UI and application.

---

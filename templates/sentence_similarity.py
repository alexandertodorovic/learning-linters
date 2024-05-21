from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(sentence1, sentence2):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Vectorize the sentences
    tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])
    
    # Calculate cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    return similarity

def print_similarity_percentage(similarity):
    # Convert similarity to percentage
    percentage = similarity * 100
    
    # Print the percentage
    print(f"Similarity: {percentage:.2f}%")

# Example usages
sentence1 = "I love programming in Python."
sentence2 = "I enjoy coding in Python."

similarity_score = calculate_similarity(sentence1, sentence2)
print_similarity_percentage(similarity_score)

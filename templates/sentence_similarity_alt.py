from difflib import SequenceMatcher

def calculate_similarity(sentence1, sentence2):
    return SequenceMatcher(None, sentence1, sentence2).ratio()

def print_similarity_percentage(similarity):
    percentage = similarity * 100
    print(f'{percentage}%')

if __name__ == "__main__":
    sentence1 = "I love programming in Python."
    sentence2 = "I enjoy coding in Python."
    similarity = calculate_similarity(sentence1, sentence2)
    print_similarity_percentage(similarity)
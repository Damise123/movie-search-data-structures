import os
import re
from turtle import title
class DataLoader:
        def __init__(self, file_path):
            self.file_path = file_path
        def load_words(self, clean=True):
            """Generator that yields words from file."""
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"{self.file_path} notfound")
            with open(self.file_path, "r", encoding="utf-8")as f:
                for line in f:
                    word = line.strip()
                    if clean:
                        word = self._clean_word(word)
                    if word:
                        yield word
        def load_into_trie(self, trie, clean=True,progress=False):
            """Load words directly into a Trie."""
            count = 0
            for count, word in enumerate(self.load_words(clean=clean), start=1):
                trie.insert(word)
                if progress and count % 10000 == 0:
                    print(f"Loaded {count} words...")
                if progress:
                    print(f"Finished loading {count} words.")
                return count
        def _clean_word(self, word):
            """Normalize words (lowercase + remove non-letters)."""
            return re.sub(r'[^a-z]', '', word.lower())

class MovieDataLoader:
    def __init__(self, filepath, delimiter=','):
        self.filepath = filepath
        self.delimiter = delimiter
        self.movies = []
    def load_movies(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            next(file)
            for line in file:
                parts = line.strip().split(',')
                if len(parts) < 3:
                    continue
                movie_id = int(parts[0])
                title = self._clean_title(parts[1])
                genres = parts[2].split('|')
                self.movies.append({
                        "id": movie_id,
                        "title": title,
                        "genres": genres
                        })
        return self.movies
    def _clean_title(self, title):
        """Remove year from movie title."""
        data = re.sub(r'\s*\(\d{4}\)\s*$', '', title).strip()
        return data
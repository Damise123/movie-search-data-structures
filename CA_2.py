import time
from trie.trie import Trie
from hash_table import HashTable
import time
from data_loader.data_loader import MovieDataLoader


#EXPERIMENTATION
def run_experiments():
    
    loader = MovieDataLoader("data/movies.csv")
    print("Loading movies...")
    

    h_table = HashTable(size=20000)
    trie = Trie()
    movies = loader.load_movies()

    # 1. Benchmark Insertion
    print("--- Insertion Performance ---")
    start = time.perf_counter()
    for m in movies: h_table.insert(m)
    print(f"Hash Table Insertion: {time.perf_counter() - start:.4f}s")

    start = time.perf_counter()
    for m in movies: trie.insert(m['title'], m)
    print(f"Trie Insertion:     {time.perf_counter() - start:.4f}s")

    # 2. Benchmark Exact Search
    target = movies[len(movies)//2]['title'] # Pick a movie from the middle
    print(f"\n--- Exact Search Performance (Target: {target}) ---")
    
    start = time.perf_counter()
    res_h = h_table.search(target)
    print(f"Hash Table (O(1)):    {time.perf_counter() - start:.8f}s")

    start = time.perf_counter()
    res_t = trie.search_exact(target)
    print(f"Trie (O(k)):        {time.perf_counter() - start:.8f}s")

    start = time.perf_counter()
    res_l = next((m for m in movies if m['title'] == target), None)
    print(f"Linear Scan (O(n)): {time.perf_counter() - start:.8f}s")

    # 3. Benchmark Prefix Search
    prefix = "Toy"
    print(f"\n--- Prefix Search Performance (Prefix: '{prefix}') ---")
    
    start = time.perf_counter()
    trie_results = trie.starts_with(prefix)
    print(f"Trie Prefix Search: {time.perf_counter() - start:.8f}s (Found {len(trie_results)})")

    start = time.perf_counter()
    linear_results = [m for m in movies if m['title'].lower().startswith(prefix.lower())]
    print(f"Linear Scan:        {time.perf_counter() - start:.8f}s (Found {len(linear_results)})")

if __name__ == "__main__":
    run_experiments()
Movie Search Data Structures Analysis

An empirical comparison of Hash Map, Trie, and Linear Search performance for movie title lookup, built for the Algorithms & Data Structures module (TU850, Assignment 2).

Overview

This project implements and benchmarks three approaches to searching movie titles in the MovieLens dataset (87,585 records):

Hash Map — O(1) average-case exact lookup
Trie (Prefix Tree) — O(k) prefix-based search, where k is the length of the search term
Linear Scan — O(n) baseline for comparison
Project Structure
├── data/
│   └── movies.csv           # MovieLens dataset (movieId, title, genres)
├── data_loader/
│   └── data_loader.py       # Loads and cleans movie records from CSV
├── trie/
│   ├── trie.py               # Trie implementation (insert, exact search, prefix search)
│   └── trie_node.py          # TrieNode class
├── hash_table.py             # Custom hash table implementation
├── CA_2.py                   # Runs the benchmarking experiments
└── Assignment2_Report.docx   # Full report with methodology and results
Methodology
Dataset: MovieLens — 87,585 movie records
Experiments run at increasing dataset sizes (1,000 / 5,000 / 10,000 / 20,000 / 50,000 / 87,585 records)
Timed using Python's time.perf_counter() for high-resolution measurement
Exact search tested against the middle record of each size tier
Prefix search tested against five prefixes of varying result-set sizes
Key Results
Test	Hash Table	Trie	Linear Scan
Insert (87,585 records)	0.064s	2.187s	—
Exact search (87,585 records)	0.0000088s	0.0000048s	0.00268s
Prefix search "Toy" (full dataset)	—	0.000078s	0.0215s

Findings: The Hash Map is fastest for exact lookups. The Trie is far faster than a linear scan for prefix search, though insertion is significantly more expensive. In practice, a combination of both would give the best of exact and prefix search performance.

Running it
python CA_2.py
Tech used

Python, custom hash table implementation, Trie/prefix tree, algorithmic complexity analysis, empirical benchmarking

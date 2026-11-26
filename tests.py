from search_index import SearchIndex


catalog = [
    "catalog",
    "catch",
    "catdog",
    "batdog",
    "catalog",
    "catlog",
    "catdog",
    "dog",
    "ratdog",
    "catdog"
]

index = SearchIndex()

index.build_index(catalog)

print("=" * 50)
print("TEST 1 : AMBIGUITY TEST")
print("=" * 50)

result = index.search_with_stats("cat", "og")

if result:
    print(f"Winner -> {result}")
else:
    print("No Match")


print("\n")
print("=" * 50)
print("TEST 2 : DUPLICATE TITLE TEST")
print("=" * 50)

result = index.search_with_stats("cat", "log")

if result:
    print(f"Winner -> {result}")
else:
    print("No Match")


print("\n")
print("=" * 50)
print("TEST 3 : NO MATCH TEST")
print("=" * 50)

result = index.search_with_stats("abc", "xyz")

if result:
    print(result)
else:
    print("No Match")


print("\n")
print("=" * 50)
print("TEST 4 : MANY QUERY TEST")
print("=" * 50)

queries = [

    ("cat", "og"),
    ("ca", "og"),
    ("ca", "ch"),
    ("cat", "log"),
    ("bat", "og"),
    ("dog", "og"),
    ("rat", "og"),
    ("c", "g"),
    ("cat", "dog"),
    ("abc", "og")
]

query_count = 1

for prefix, suffix in queries:

    print(f"\nQuery {query_count}")
    print(f"Prefix = {prefix}")
    print(f"Suffix = {suffix}")

    result = index.search(prefix, suffix)

    if result:
        print(
            f"Matched => "
            f"{result.title} "
            f"(ID={result.id})"
        )
    else:
        print("No Match")

    query_count += 1


print("\n")
print("=" * 50)
print("TEST 5 : LATEST MATCH WINS")
print("=" * 50)

print("\nCatalog Entries:\n")

for i, word in enumerate(catalog):
    print(f"{i} -> {word}")

print("\nSearching:")
print("Prefix = cat")
print("Suffix = og")

result = index.search("cat", "og")

print("\nExpected Latest Match:")

if result:
    print(result)
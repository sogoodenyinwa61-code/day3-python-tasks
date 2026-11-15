# Task 4: Collect tags until the user types done, store unique tags in a set

tags = set()    # empty set (not {}, which would be an empty dictionary)

while True:
    tag = input("Enter a tag (or 'done' to finish): ").strip().lower()
    if tag == "done":
        break               # stop the loop
    if tag:                 # skip empty input
        tags.add(tag)

print("\nUnique tags:", tags)
print("Number of unique tags:", len(tags))
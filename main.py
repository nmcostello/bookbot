def main():
  book_path = "books/frankenstein.txt"
  generate_report(book_path)

def generate_report(path):
  text = get_book_text(path)
  char_map = get_unique_chars(text)
  word_count = get_word_count(text)

  print(f"{word_count} words found in document\n")

  sorted_map = {k: v for k, v in sorted(char_map.items(), key=lambda item: -item[1])}
  for c in sorted_map:
    print(f"The '{c}' character was found {sorted_map[c]} times")
  
  print("--- End report ---")

def get_word_count(text):
  return len(text.split())

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_unique_chars(text: str) -> dict:
  contains = {}
  lower = text.lower()

  for c in lower:
    if not c.isalpha():
      continue
    contains[c] = contains.get(c, 0) + 1

  return contains

main()
def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  char_map = get_unique_chars(text)

  print(f"total words = {get_word_count(text)}")
  print(f"characters = {char_map}")

def get_word_count(text):
  return len(text.split())

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_unique_chars(text: str) -> dict:
  contains = {}
  lower = text.lower()

  for c in lower:
    if c == " ":
      continue
    contains[c] = contains.get(c, 0) + 1

  return contains

main()
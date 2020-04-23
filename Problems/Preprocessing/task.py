text = input()
print(text.strip(",.!?").replace(",", "").replace(".", "")
      .replace("!", "").replace("?", "").lower())
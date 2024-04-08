def is_palindrome_iterative(word: str) -> bool:
    if not word:
        return False
    size = len(word)
    for i in range(0, size // 2):
        if word[i] != word[size - i - 1]:
            return False
    return True

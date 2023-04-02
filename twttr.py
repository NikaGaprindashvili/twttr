def shorten(word):
    """
    Removes all vowels (A, E, I, O, and U) from the given word, whether inputted in uppercase or lowercase.
    """
    vowels = ["a", "e", "i", "o", "u"]
    return "".join([letter for letter in word if letter.lower() not in vowels])


def main():
    """
    Prompts the user to input a string and prints the shortened version of that string.
    """
    text = input("Input: ")
    shortened_text = shorten(text)
    print("Output:", shortened_text)


if __name__ == "__main__":
    main()
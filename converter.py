from morse_dict import TEXT_TO_MORSE, MORSE_TO_TEXT, WORD_SEPARATOR

def text_to_morse(text: str):
    """
    Convert normal text to Morse code.
    Words seperated by '/'
    Letters are seperated by space.
    """
    text = text.upper()
    morse_output = []

    for word in text.split():
        letters = []
        for char in word:
            letters.append(TEXT_TO_MORSE[char])
        morse_output.append(" ".join(letters))
    return f"{WORD_SEPARATOR}".join(morse_output)

def morse_to_text(morse: str):
    """
    Convert Morse Code to Text
    
    USER INPUT RULES:
    0 = Dot
    1 = Dash
    space = letter separator
    / = word separator
    """
    
    morse = morse.replace("0", ".").replace("1", "-").replace(" ", " ").replace("/", WORD_SEPARATOR)

    words = morse.split(WORD_SEPARATOR)
    decoded_words = []

    for word in words:
        letters = []
        for symbol in word.strip().split():
            if symbol in MORSE_TO_TEXT:
                letters.append(MORSE_TO_TEXT[symbol])
            else:
                letters.append("?")
        decoded_words.append("".join(letters))

    return " ".join(decoded_words)
# Should we use dictionary or list ?
# i think list is better since it is in alphabetic order

alphs = [i for i in "abcdefghijklmnopqrstuvwxyz1234567890 "]
morse_alph = [
    ".-",   # A
    "-...", # B
    "-.-.", # C
    "-..",  # D
    ".",    # E
    "..-.", # F
    "--.",  # G
    "....", # H
    "..",   # I
    ".---", # J
    "-.-",  # K
    ".-..", # L
    "--",   # M
    "---",   # N
    "-.",   # O
    ".--.", # P
    "--.-", # Q
    ".-.",  # R
    "...",  # S
    "-",    # T
    "..-",  # U
    "...-", # V
    ".--",  # W
    "-..-", # X
    "-.--", # Y
    "--..", # Z
    ".----",    
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
    "-----",
    ""
]

def text_to_morse(text: str):
    """Text to morse code encoder
    :param str text: Plaintext to be encoded to morse code
    """
    return "".join([(morse_alph[alphs.index(i)] + " ") for i in text.lower()])

def morse_to_text(morse: str):
    """Morse code to text decoder
    :param str morse: A Morse code to be decoded to plaintext
    """
    accepted_char = "-. "
    parsed = []
    temp = []
    for i in range(len(morse)):
        if morse[i] not in accepted_char:
            raise TypeError("Character {} is not acceptable. only dot(.) and dash(-) allowed".format(morse[i]))
        temp.append(morse[i])
        if morse[i] == " ":
            temp.pop()
            parsed.append("".join(temp.copy()))
            temp = []
        
        if i >= len(morse)-1: # THIS FIX IS SO FUCKED UP!
            parsed.append("".join(temp.copy()))
            temp = []

    decoded = []
    for i in parsed:
        if i == '':
            decoded.append(" ")
        else:
            decoded.append(alphs[morse_alph.index(i)])
    
    return "".join(decoded)

def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])




def test():
    assert remove_vowels("Milliways") == "Mllwys"
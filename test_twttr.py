from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("xyz") == "xyz"
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert shorten("BCDFGHJKLMNPQRSTVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_shorten_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_shorten_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("Lorem ipsum dolor sit amet") == "Lrm psm dlr st mt"
    assert shorten("The quick brown fox jumps over the lazy dog") == "Th qck brwn fx jmps vr th lzy dg"

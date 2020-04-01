def clean_str(s):
    s = s.strip()
    specials = ["\r", "\n", "\t"]
    for each in specials:
        s = s.replace(each, "")
    return s
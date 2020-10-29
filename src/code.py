def to_camel_case(text):
    answer = ""
    if text == "":
        return answer
    is_character = 0
    i = 0
    first = 0
    for character in text:
        if character != "-" or character != "_":
            is_character += 1
            i += 1
        else:
            if first == 0:
                first += 1
                is_character = 0
                continue
            else:
                answer += text[i-is_character].upper()
                answer += text[(i-is_character)+1:i]
                is_character = 0
                i += 1
    return answer

if __name__ == "__main__":
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
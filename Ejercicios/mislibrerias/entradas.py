def get_int(hint):
    valid_answer = False
    while not valid_answer:
        try:
            answer = int(input(hint))
            valid_answer = True
        except Exception as e:
            print("No has introducido un número:", e)
    return answer

def get_str(hint):
    return input(hint)

def get_bool(hint):
    new_hint = hint.strip() + " [y/n]"
    valid_answers = ['s', 'si', 'y', 'yes', 'n', 'no']
    is_valid = False
    while not is_valid:
        answer = input(new_hint).lower()
        is_valid = answer in valid_answers
    return answer in valid_answers[:4]
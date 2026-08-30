"""
def condition_checker(content, condition):
    triggered = False
    in_quote = False
    bool_reverse = False
    in_check = False
    end_check = False
    start_check = False
    is_ckeck = False
    check_word = ""
    trigger = ""
    and_condition = False
    or_condition = False
    for symbol in condition:
        if symbol == "'":
            in_quote = not in_quote
        if symbol == "&":
            and_condition = True
        if symbol == "|":
            or_condition = True
        if not in_quote and not any(symbol == w for w in ["'", " ", "|", "&"]):
            check_word += symbol
            if check_word == "not":
                bool_reverse = True
                check_word = ""
            if check_word == "in":
                in_check = True
                check_word = ""
            if check_word == "end":
                end_check = True
                check_word = ""
        if in_quote and symbol != "'":
            trigger += symbol
        if trigger != "" and not in_quote:
            current_triggered = False
            if in_check:
                current_triggered = trigger in content
                in_check = False
            if end_check:
                current_triggered = content.endswith(trigger)
                end_check = False
            if bool_reverse:
                current_triggered = not current_triggered
                bool_reverse = False
            if not and_condition and not or_condition:
                triggered = current_triggered
            if and_condition:
                triggered = triggered and current_triggered
                and_condition = False
            if or_condition:
                triggered = triggered or current_triggered
                or_condition = False
            trigger = ""
    return triggered
"""

def condition_checker(content, condition):
    triggered = False
    in_quote = False
    bool_reverse = False
    in_check = False
    end_check = False
    start_check = False
    is_check = False
    check_word = ""
    trigger = ""
    and_condition = False
    or_condition = False
    for symbol in condition:
        if symbol == "'":
            in_quote = not in_quote
        if symbol == "&":
            and_condition = True
        if symbol == "|":
            or_condition = True
        if not in_quote and not any(symbol == w for w in ["'", " ", "|", "&"]):
            check_word += symbol
            if check_word == "not":
                bool_reverse = True
                check_word = ""
            if check_word == "in":
                in_check = True
                check_word = ""
            if check_word == "end":
                end_check = True
                check_word = ""
            if check_word == "start":
                start_check = True
                check_word = ""
            if check_word == "is":
                is_check = True
                check_word = ""
        if in_quote and symbol != "'":
            trigger += symbol
        if trigger != "" and not in_quote:
            current_triggered = False
            if in_check:
                current_triggered = trigger in content
                in_check = False
            if end_check:
                current_triggered = content.endswith(trigger)
                end_check = False
            if start_check:
                current_triggered = content.startswith(trigger)
                start_check = False
            if is_check:
                current_triggered = content == trigger
                is_check = False
            if bool_reverse:
                current_triggered = not current_triggered
                bool_reverse = False
            if not and_condition and not or_condition:
                triggered = current_triggered
            if and_condition:
                triggered = triggered and current_triggered
                and_condition = False
            if or_condition:
                triggered = triggered or current_triggered
                or_condition = False
            trigger = ""
    return triggered
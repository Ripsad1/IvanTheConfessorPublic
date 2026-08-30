import random

def block_interpreter(msg, block):
    content = msg.content.lower()
    if block == "last":
        return content.rstrip("!?.,").split()[-1]
    if block == "msg":
        return content
    if block == "author":
        return f"<@{msg.author.id}>"
    if block.startswith("replace//"):
        original, changed = block[9:].split("//", 1)
        return content.replace(original,changed)
    if block.startswith("random//"):
        options = block[8:].split("//")
        choice = random.choice(options)
        return choice
    if block.startswith("sub(") and block.endswith(")"):
        args = block[4:-1].split(",")
        if len(args) != 2:
            return None
        try:
            i = int(args[0]) if args[0].strip() else None
            j = int(args[1]) if args[1].strip() else None
        except ValueError:
            return None
        return content[i:j]
    return None


def interpreter(msg, write):
    to_send = ""
    in_block = False
    block = ""
    for letter in write:
        if letter == "[":
            in_block = True
        if letter == "]":
            in_block = False
        if in_block and letter != "[":
            block += letter
        if not in_block and letter != "]":
            to_send += letter
        if not in_block and letter == "]":
            to_send += block_interpreter(msg,block)
            block = ""
    return to_send
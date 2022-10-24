def show_tokens(obj) -> None:
        for idx, tok in enumerate(obj.tokens):
            print(f"{idx: <4}{tok.ttype: <12} {tok.line}:{tok.charidx} {tok.value}")

def show_register(obj) -> None:
    for idx, (identifier, reg) in enumerate(obj.register.items()):
        print(f"{idx: <4}{identifier:<10}: {reg.type} = {reg.value}")
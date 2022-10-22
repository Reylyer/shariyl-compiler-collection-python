
def fragment(file_path) -> list:
    with open(file_path, 'r') as f:
        content = f.read()
        lines = content.split('\n')[::-1]
        delimiter = (
            "program",
            "procedure",
            "function",
            "KAMUS LOKAL",
            "KAMUS",
            "ALGORITMA"
        )
        sections = []
        section = []
        for line in lines:
            section.append(line)
            if line.startswith(delimiter):
                sections.append("\n".join(section[::-1]))
                section = []
        sections = sections[::-1]
        return sections
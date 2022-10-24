
def fragment(file_path) -> list:
    with open(file_path, 'r') as f:
        content = f.read()
        lines = reversed(content.split('\n'))
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
        line_count = 0
        char_count = 0
        for line in lines:
            section.append(line)
            line_count += 1
            if line.startswith(delimiter):
                section = "\n".join(reversed(section))
                char_count += len(section)
                sections.append([section, line_count, char_count])
                section = []
        sections = list(reversed(sections))
        return sections
#TODO: kelarin Array

class ArrayDataTypes: # Kontigu 
    # ngikut ae lah namanya
    wadah = []
    size = 0

    def __str__(self) -> str:
        return f"<{', '.join([str(a) for a in self.wadah])}>"

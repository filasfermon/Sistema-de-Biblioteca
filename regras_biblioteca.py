class Livro:
    def __init__(self, titulo, autor, ano, copias):
        self.titulo = titulo
        self.autor = autor
        self.ano = str(ano)
        self.copias = int(copias)
        self.copias_totais = int(copias)

    def emprestar(self):
        if self.copias > 0:
            self.copias -= 1
            return True
        return False
    
    def devolver(self):
        if self.copias < self.copias_totais:
            self.copias += 1
            return True
        else:
            return False
        
    def __str__(self):
        return f"📖 {self.titulo} "
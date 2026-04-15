# Minha grade de matérias em ADS 2026 🎓
# Criando uma LISTA (usando os colchetes [])
materias = [
    "Educação Ambiental", 
    "Pensamento Lógico Computacional com Python",
    "Infraestrutura Computacional",
    "Tecnologia da Informação e da Comunicação",
    "Ética, Cidadania e Sustentabilidade", 
    "Estatística"
]
print("---MINHA GRADE ATUAL EM ADS---")
# O laço 'for' percorre a lista e imprime cada matéria
for m in materias:
    print(f"📚 Matéria: {m}")

    print("_" * 32)
    print(f"Total de disciplinas: {len(materias)}" )
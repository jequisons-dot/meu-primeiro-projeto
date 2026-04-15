import pandas as pd 

data = {
    'Matéria': ['Lógica de Programação Python', 'Estatística', 'Infraestrutura Computacional', 'Tecnologia da informação', 'Ética e Cidania' ],
    'Nota': [7.5, 4.3, 7.0, 8.0, 10.0]

}
df = pd.DataFrame(data)
print("Minha média atual:", df['Nota'].mean())

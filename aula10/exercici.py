import json

# String original
texto = "joão da Silva - Rua A, 123; Maria dos Santos - Rua B, 225"

lista_pessoas = []

# 1. Separar os registros por ponto e vírgula
registros = texto.split("; ")

for registro in registros:
    # 2. Separar o nome do restante do endereço (usando o hífen)
    dados_pessoais, endereco_completo = registro.split(" - ")
    
    # Ajustar a capitalização do nome (ex: "joão" para "João")
    nome = dados_pessoais.strip().title()
    nome = nome.replace("Da ", "da ").replace("Dos ", "dos ")
    
    # 3. Separar a rua do número (usando a vírgula)
    rua, numero = endereco_completo.split(", ")
    
    # 4. Criar o dicionário com a estrutura desejada
    dicionario_pessoa = {
        "nome": nome,
        "endereço": rua.strip(),
        "numero": numero.strip()
    }
    
    lista_pessoas.append(dicionario_pessoa)

# 5. Converter a lista de dicionários para uma string formatada em JSON
json_resultado = json.dumps(lista_pessoas, ensure_ascii=False, indent=5)

print(json_resultado)
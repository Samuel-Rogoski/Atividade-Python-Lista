produtos = [
    [1, "Notebook", 3500.00],
    [2, "Smartphone", 1500.00],
    [3, "Mouse", 80.00]
]

print("--- 1. Lista Inicial de Produtos ---")
for p in produtos:
    print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f}")

id_busca = 2
print(f"\n--- 2. Buscando produto com ID {id_busca} ---")
encontrado = False
for p in produtos:
    if p[0] == id_busca:
        print(f"Produto Encontrado -> Nome: {p[1]}, Preço: R$ {p[2]:.2f}")
        encontrado = True
        break
if not encontrado:
    print("Produto não encontrado.")

id_remover = 2
print(f"\n--- 3. Removendo produto com ID {id_remover} ---")
for p in produtos:
    if p[0] == id_remover:
        produtos.remove(p)
        print(f"Produto com ID {id_remover} removido com sucesso.")
        break

print("\n--- 4. Lista Após a Remoção ---")
print(produtos)


print("\n--- Vamos cadastrar um novo produto ---")

print("Cadastrando novo produto...")
novo_id = 4
novo_nome = "Teclado Mecânico"
novo_preco = 250.00

novo_produto = [novo_id, novo_nome, novo_preco]
produtos.append(novo_produto)
print(f"Lista após append(): {produtos}")

id_alterar = 1
novo_valor = 3200.00
print(f"\nAlterando o preço do produto de ID {id_alterar} para R$ {novo_valor:.2f}...")

for p in produtos:
    if p[0] == id_alterar:
        p[2] = novo_valor
        break

print("Lista final atualizada:")
for p in produtos:
    print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f}")

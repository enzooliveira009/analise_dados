import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

cells.append(nbf.v4.new_markdown_cell(
"""# Análise da Tabela 3 — Censo Demográfico 2022 (IBGE)
**Tabela 10063** — Pessoas com nível superior completo, por áreas gerais, específicas e
detalhadas de formação do curso de graduação concluído, segundo os grupos de idade, o sexo
e a cor ou raça (recorte: Brasil, Grandes Regiões e Unidades da Federação, por sexo).

Fonte: IBGE, Censo Demográfico 2022.

> Observação: o ambiente de execução deste notebook não tem acesso de rede ao site do IBGE
> (sidra.ibge.gov.br), então os dados brutos foram reconstruídos a partir da imagem da tabela
> fornecida pelo usuário e salvos em `data/tabela3_censo_superior_raw.csv`. Se você tiver o
> arquivo oficial do SIDRA, basta substituir esse CSV mantendo as mesmas colunas."""
))

cells.append(nbf.v4.new_code_cell(
"""import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 140)

RAW_PATH = "data/tabela3_censo_superior_raw.csv"
OUT_DIR = "output"

df = pd.read_csv(RAW_PATH)
df.head(10)"""
))

cells.append(nbf.v4.new_markdown_cell("## 1. Tabela — Total geral (homens e mulheres por região/UF com curso superior)"))

cells.append(nbf.v4.new_code_cell(
"""total_geral = df[["Local", "Nivel", "Regiao", "Total_Total", "Total_Homens", "Total_Mulheres"]].copy()
total_geral = total_geral.rename(columns={
    "Total_Total": "Total",
    "Total_Homens": "Homens",
    "Total_Mulheres": "Mulheres",
})
total_geral.to_excel(f"{OUT_DIR}/total_geral.xlsx", index=False)
total_geral"""
))

cells.append(nbf.v4.new_markdown_cell(
"## 2. Tabela — Ciência, Tecnologia, Engenharias e Matemática (CTEM)"
))

cells.append(nbf.v4.new_code_cell(
"""tecnologia = df[["Local", "Nivel", "Regiao", "CTEM_Total", "CTEM_Homens", "CTEM_Mulheres"]].copy()
tecnologia = tecnologia.rename(columns={
    "CTEM_Total": "Total",
    "CTEM_Homens": "Homens",
    "CTEM_Mulheres": "Mulheres",
})
tecnologia.to_excel(f"{OUT_DIR}/tecnologia.xlsx", index=False)
tecnologia"""
))

cells.append(nbf.v4.new_markdown_cell(
"## 3. Tabela — Educação, Serviços pessoais, Saúde e Bem-estar"
))

cells.append(nbf.v4.new_code_cell(
"""educacao_saude = df[["Local", "Nivel", "Regiao", "ESP_Total", "ESP_Homens", "ESP_Mulheres"]].copy()
educacao_saude = educacao_saude.rename(columns={
    "ESP_Total": "Total",
    "ESP_Homens": "Homens",
    "ESP_Mulheres": "Mulheres",
})
educacao_saude.to_excel(f"{OUT_DIR}/educacao_saude.xlsx", index=False)
educacao_saude"""
))

cells.append(nbf.v4.new_markdown_cell("## 4. Estatísticas descritivas — `describe()`"))

cells.append(nbf.v4.new_code_cell(
"""print("=== Total geral ===")
display(total_geral.describe())

print("\\n=== Ciência, Tecnologia, Engenharias e Matemática ===")
display(tecnologia.describe())

print("\\n=== Educação, Serviços pessoais, Saúde e Bem-estar ===")
display(educacao_saude.describe())"""
))

cells.append(nbf.v4.new_markdown_cell(
"""### Comentários rápidos
- As três tabelas usam **34 linhas** (Brasil + 5 Grandes Regiões + 27 UFs — mas note que
  `describe()` aqui inclui Brasil e as Regiões junto com as UFs; se quiser estatísticas só
  das 27 UFs, filtre por `Nivel == "UF"` antes do `describe()`).
- Em todas as áreas, o número de **mulheres** com curso superior concluído é maior que o de
  homens no total do Brasil, exceto na área de **Ciência, Tecnologia, Engenharias e
  Matemática**, onde os homens são maioria.
- São Paulo concentra o maior volume absoluto em todas as três tabelas, como esperado pelo
  tamanho populacional do estado."""
))

cells.append(nbf.v4.new_markdown_cell("### Estatísticas descritivas apenas das 27 Unidades da Federação (UFs)"))

cells.append(nbf.v4.new_code_cell(
"""uf_mask = df["Nivel"] == "UF"

print("=== Total geral (UFs) ===")
display(total_geral[uf_mask].describe())

print("\\n=== CTEM (UFs) ===")
display(tecnologia[uf_mask].describe())

print("\\n=== Educação/Saúde (UFs) ===")
display(educacao_saude[uf_mask].describe())"""
))

nb["cells"] = cells

with open("analise_tabela3.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("notebook criado")

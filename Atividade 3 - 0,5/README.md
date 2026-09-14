# Análise — Tabela 3 (Censo Demográfico 2022 / IBGE)

Análise da **Tabela 10063** do Censo Demográfico 2022 do IBGE: pessoas com nível superior
completo, por sexo e Grande Região / Unidade da Federação, divididas em três recortes de
área de formação.

## Estrutura

```
.
├── analise_tabela3.ipynb          # notebook com todo o passo a passo
├── build_raw_data.py              # script que gera o CSV bruto (fonte)
├── data/
│   └── tabela3_censo_superior_raw.csv
└── output/
    ├── total_geral.xlsx           # homens e mulheres por região/UF, curso superior (total)
    ├── tecnologia.xlsx            # homens e mulheres — Ciência, Tecnologia, Engenharias e Matemática
    └── educacao_saude.xlsx        # homens e mulheres — Educação, Serviços pessoais, Saúde e Bem-estar
```

## Sobre a fonte dos dados

O ambiente usado para rodar este notebook não tem acesso de rede ao site do IBGE
(`sidra.ibge.gov.br`), então os dados brutos em `data/tabela3_censo_superior_raw.csv` foram
reconstruídos a partir da tabela fornecida (imagem/print da Tabela 10063). Os valores batem
exatamente com a soma Brasil = soma das 5 Grandes Regiões, o que confirma a consistência da
transcrição. Se você tiver o arquivo oficial exportado do SIDRA, basta substituir esse CSV
mantendo as mesmas colunas e re-executar o notebook.

Fonte original: IBGE, Censo Demográfico 2022 — Tabela Sidra 10063.

## Como rodar

```bash
pip install pandas openpyxl nbformat jupyter nbconvert
python build_raw_data.py
jupyter nbconvert --to notebook --execute --inplace analise_tabela3.ipynb
```

Os três arquivos `.xlsx` serão gerados/atualizados em `output/`.

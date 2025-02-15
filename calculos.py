from fatores import fatores_emissao, projetos_compensacao # type: ignore

# Função para calcular as emissões de uma determinada categoria de consumo
def calcular_emissao(tipo, quantidade):
    return quantidade * fatores_emissao.get(tipo, 0)

# Função para calcular o custo de compensação de carbono
def calcular_custo_compensacao(emissao_total, projeto):
    preco_por_tonelada = projetos_compensacao.get(projeto, 0)
    return (emissao_total / 1000) * preco_por_tonelada  # Conversão para toneladas

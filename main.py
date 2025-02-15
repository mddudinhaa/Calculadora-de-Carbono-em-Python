from entrada_dados import obter_dados_consumo # type: ignore
from calculos import calcular_emissao, calcular_custo_compensacao # type: ignore
from fatores import projetos_compensacao # type: ignore

def calcular_pegada_carbono(consumos):
    emissao_total = 0
    print("\nEmissões de CO2 por fonte:")
    for tipo, quantidade in consumos.items():
        emissao = calcular_emissao(tipo, quantidade)
        emissao_total += emissao
        print(f"- {tipo.capitalize()}: {emissao:.2f} kg CO2")

    print(f"\nPegada total de carbono: {emissao_total:.2f} kg CO2")
    return emissao_total

def escolher_projeto_compensacao(emissao_total):
    print("\nProjetos de Compensação Disponíveis:")
    for i, (projeto, preco) in enumerate(projetos_compensacao.items(), start=1):
        print(f"{i}. {projeto.capitalize()} - R$ {preco} por tonelada de CO2")

    opcao_projeto = input("\nEscolha o número do projeto de compensação: ")
    projeto_selecionado = list(projetos_compensacao.keys())[int(opcao_projeto) - 1]
    custo = calcular_custo_compensacao(emissao_total, projeto_selecionado)
    
    print(f"\nResumo Final:")
    print(f"Projeto de compensação escolhido: {projeto_selecionado.capitalize()}")
    print(f"Custo total para compensação: R$ {custo:.2f}")
    return projeto_selecionado, custo

# Execução da calculadora
consumos = obter_dados_consumo()
emissao_total = calcular_pegada_carbono(consumos)
projeto_escolhido, custo_compensacao = escolher_projeto_compensacao(emissao_total)

# Resumo final das escolhas do usuário
print("\n---- Resumo Completo ----")
print("Fontes de Emissão Selecionadas e Consumo:")
for tipo, quantidade in consumos.items():
    print(f"- {tipo.capitalize()}: {quantidade} unidades")
print(f"\nPegada Total de Carbono: {emissao_total:.2f} kg CO2")
print(f"Projeto de Compensação Escolhido: {projeto_escolhido.capitalize()}")
print(f"Custo para Compensação: R$ {custo_compensacao:.2f}")
print("-------------------------")

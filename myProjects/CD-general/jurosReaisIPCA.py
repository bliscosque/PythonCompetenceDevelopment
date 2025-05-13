import pandas as pd
import numpy as np
# r_real_liquido = ((1 + j) * (1 + i) * (1 - IR)) / (1 + i) - 1
taxa_ir = 0.15
juros_reais = np.arange(0.05, 0.081, 0.005)  # de 5% a 8% (5.0%, 5.5%, ..., 8.0%)
inflacoes = np.arange(0.05, 0.081, 0.005)

# Nova tabela
tabela = pd.DataFrame(index=[f"IPCA+{round(j*100,1)}%" for j in juros_reais],
                                 columns=[f"{round(i*100,1)}%" for i in inflacoes])

# Preencher a tabela com a fórmula correta
for j in juros_reais:
    for i in inflacoes:
        rendimento_nominal_bruto = (1 + j) * (1 + i) - 1
        rendimento_nominal_liquido = rendimento_nominal_bruto * (1 - taxa_ir)
        retorno_real_liquido = (1 + rendimento_nominal_liquido) / (1 + i) - 1
        tabela.loc[f"IPCA+{round(j * 100, 1)}%", f"{round(i * 100, 1)}%"] = round(retorno_real_liquido * 100, 2)

print(tabela)

faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53
faturamento_total = faturamento_outros + faturamento_sp + faturamento_es + faturamento_mg + faturamento_rj

percentual_sp = (faturamento_sp / faturamento_total) * 100
percentual_rj = (faturamento_rj / faturamento_total) * 100
percentual_mg = (faturamento_mg / faturamento_total) * 100
percentual_es = (faturamento_es / faturamento_total) * 100
percentual_outros = (faturamento_outros / faturamento_total) * 100

print(f'O estado São Paulo foi responsável por {percentual_sp :.2f}% do total do mês, O estado Rio de Janeiro foi responsável por {percentual_rj :.2f}% do total do mês, O estado Minas Gerais foi responsável por {percentual_mg :.2f}% do total do mês, o estado Espírito Santo foi responsável por {percentual_es :.2f}% do total do mês e os outros estados foram responsáveis por {percentual_outros :.2f}% do total do mês')
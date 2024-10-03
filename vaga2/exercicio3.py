class Faturmanto:
    def __init__(self, id, revenue, date) -> None:
        self.id = id
        self.revenue = revenue
        self.date = date

def verifica_faturamento(faturamentos):
    maior_faturamento = {}
    menor_faturamento = {}
    for id, faturamento, data in faturamentos:
        if faturamento == 0:
            continue
        else:
            if faturamento > maior_faturamento:
                maior_faturamento = {id : id, revenue : faturamento, date : data}
            elif faturamento < menor_faturamento:
                menor_faturamento = {id : id, revenue : faturamento, date : data}
        print(f'O maior faturamento foi no dia {maior_faturamento.date} com o valor de {maior_faturamento.revenue} e o menor faturamento foi no dia {menor_faturamento.date} com o valor de {menor_faturamento.revenue}')

faturamento1 = Faturmanto(0, 5000, '10/10/2024')
faturamento2 = Faturmanto(1, 15000, '11/10/2024')
faturamento3 = Faturmanto(2, 4000, '12/10/2024')
faturamento4 = Faturmanto(3, 10000, '13/10/2024')
faturamento5 = Faturmanto(4, 12000, '14/10/2024')

faturamentos = [faturamento1, faturamento2, faturamento3, faturamento4, faturamento5]
verifica_faturamento(faturamentos)
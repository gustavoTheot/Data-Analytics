import pandas as pd
from IPython.display import display
import plotly.express as px # pacote de gráficos 

# Passo 1 - Importar a base de dados

table = pd.read_csv('telecom_users.csv')

# Passo 2 - Visualizar a base de dados

print('--------------PRIMEIRA INFORMAÇÃO DA BASE DE DADOS--------------')
print(table.info())
display(table)
print('--------------FIM DA PRIMEIRA INFORMAÇÃO--------------')

# Passo 3 - Tratamento da base de dados

## 1° excluir arquivos inuteis

table = table.drop('Unnamed: 0', axis=1)

## 2° transform string in number

table['TotalGasto'] = pd.to_numeric(table['TotalGasto'], errors='coerce')

## 3° treating value null

table = table.dropna(how='all', axis=1) # excluir coluns(axis=1) que estejam todas vazias(how='all')

table = table.dropna(how='any', axis=0) # excluir linhas(axis=0) que pelo menos 1 vazio(how='any')

# Passo 4 - Analisar a base de dados depois de tratada 
print('--------------ULTIMA INFORMAÇÃO DA BASE DE DADOS--------------')
print(table.info())
display(table)

display(table['Churn'].value_counts())
display(table['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

print('--------------FIM DA ULTIMA INFORMAÇÃO--------------')

# Paso 5 - Identificar motivos de problemas 

for column in table.columns: # Percorrendo todos as table e comparando ela com a column
    print(column)

    grafic = px.histogram(table, x=column, color='Churn') # diferenciando os sim e os não
    grafic.show()

# Clientes com famílias maiores (casados e com dependentes) tendem a cancelar menos
    ##  Ideia para contribuir com esse tipo de clíente, dimiuindo mais ainda sua desistencia do produto

# Os meses 20 primeiros meses são os de maiores churn
    ##  Talves primeira experiência ruim, cliente serviço 
    ##  Talves a vinda de clientes desqualificados 
    ##  Ideia: Programa de incentivo, criando bonus para o cliente até o 20° mês

# Problema com a fibra, onde tem muitos clientes, mas muito churn
    ##  Verificar o serviço de fibra, pois deve ter algum problema

# Quem não tem serviço de segurança online, costuma cancelar muito mais que os outros
# Quem não tem serviço de backup online, costuma cancelar muito mais que os outros
# Quem não tem proteção de equipamento, costuma cancelar muito mais que os outros
# Quem não tem serviço de suporte tecnico, costuma cancelar muito mais que os outros
    ## Quanto mais serviços o cliente tem, menor a chance dele cancelar
    ## Ideia: criar um programa de incentivo aos outros serviços

# Quase todos os cancelamentos estão no serviço mensal 
    ## plano de insentivo ao contrato anual ou 2 anos -> desconto para planos anuais

# Evitar boleto eletronico
    ## incentivar os clientes mudarem pra cartão de crédito ou debito automatico -> bonus, etc.









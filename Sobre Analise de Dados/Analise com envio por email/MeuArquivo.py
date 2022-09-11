import pandas as pd
import win32com.client as win32

# Importar a base de dados

tabela_vendas = pd.read_excel('Vendas.xlsx')


# Visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# Faturamento por loja
print('=' * 50)
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
#print(faturamento)

# Quantidade de produtos vendidos por loja
print('=' * 50)
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

# Ticket Médio por produto em cada loja
# ().to_frame() para transformar em uma tabela
print('=' * 50)
ticket_medio = round((faturamento['Valor Final'] / quantidade['Quantidade']).to_frame(), 2)
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

# Enviar um email com o relatório

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.to = 'Seu e-mail'
mail.Subject = 'Titulo do Email'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatter={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos produtos em cada Loja:</p>
{ticket_medio.to_html(formatter={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou a disposição.</p>

<p>Att..</p>
<p>Borges</p>
'''

mail.Send()

print('=' * 20)
print('EMAIL ENVIADO')
print('=' * 20)

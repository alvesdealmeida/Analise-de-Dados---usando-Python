#inicio de c�digo:

# 1 importar a base de dados
import pandas as pd

# 2 visualizar a base de dados:
tabela = pd.read_csv("telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)

# 3 tratamento de dados: 
# valores que est�o reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")


# valores vazios

#deletando as colunas vazias
tabela = tabela.dropna(how="all", axis=1)
#deletando as linhas
tabela = tabela.dropna(how ="any", axis=0)
print(tabela.info())

# 4 an�lise inicial
#como est�o nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# 5 an�lise completa
#comparar cada coluna da tabela com a coluna de cancelamento
import plotly.express as px
# etapa 1 criar o grafico
for coluna in tabela.columns:
	#para edicoes: https://plotly.com/phyton/histogram
	#mudar cor : color_discrete_sequence=["blue,"green"]
	grafico = px.histogram(tabela, x= coluna , color="Churn")
	# etapa 2 exibir o grafico
	grafico.show()

"fim do c�digo

"Minha an�lise ap�s visualizar os gr�ficos e depois
"de todas as corre��es que o python fez na base de dados:


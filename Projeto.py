import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

acoes = ["TOTS3.SA","ASAI3.SA","VALE3.SA","PETR4.SA","PETR3.SA"]

def obter_cotacoes(acoes):
    dados = yf.download(acoes, start="2021-01-01", end="2021-12-31")
    return dados

def plotar_tendencia(dados):
    dados["Adj Close"].plot()
    plt.xlabel("Data")
    plt.ylabel("Cotação")
    plt.title("Tendência da Ação")
    plt.show()

def plotar_todas_tendencias(dados):
    dados["Adj Close"].plot(legend=True)
    plt.xlabel("Data")
    plt.ylabel("Cotação")
    plt.title("Todas as Tendências")
    plt.show()

def mostrar_cotacoes(dados):
    cotacoes = dados[["Date", "Adj Close"]]
    cotacoes = cotacoes.sort_values("Date", ascending=False)
    print(cotacoes)

dados = obter_cotacoes(acoes)
plotar_tendencia(dados)
plotar_todas_tendencias(dados)
mostrar_cotacoes(dados)


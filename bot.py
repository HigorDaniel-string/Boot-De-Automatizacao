# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui # para instalar: pip install e o nome da biblioteca
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto (somente texto, pois, numero pode dar erro)
# pyautogui.press -> apertaar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)
pyautogui.PAUSE = 0.3

# abrir o chorme
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(734,367, clicks=1)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") # passar para o campo de senha
pyautogui.write("sua senha aqui")

pyautogui.press("tab") # passei para o botão de login
pyautogui.press("enter")

time.sleep(3)

# Passo3: Importar a base de dados de produtos
#pip install pandas numpy openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    # Passo 4: Cadastrar um produto'10  2000.0  440.0

    pyautogui.click(1022,250, clicks=1)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    

    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(marca))
    pyautogui.press("tab")

    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    pyautogui.write(str(preco))
    pyautogui.press("tab")

    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # isna verifica se esta vazio
        pyautogui.write(str(obs))

    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)


    #nan = 

# Passo 5: Repetir o processo de cadastrar o produto


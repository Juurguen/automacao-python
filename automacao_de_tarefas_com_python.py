# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa (https://hashtagtreinamentos.com/python/intensivao/login)
# pip install pyautogui

import pyautogui 
import time

pyautogui.PAUSE = 0.5

# pyautogui.click = clicar na tela.
# pyautogui.write = escrever um texto.
# pyautogui.press = pressionar 1 tecla do teclado.

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Dar uma pausa após a entrada do site.
time.sleep(2)

# Passo 2: Fazer login.
pyautogui.click(x=626, y=507)
pyautogui.write("jurguenpython@python.com")
pyautogui.press("TAB")
pyautogui.write("12345678")
# Clicar no botão de logar.
pyautogui.press("TAB")
pyautogui.press("enter")
time.sleep(2)

# Passo 3: Importar dados.
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto. 
# Montar estrutura do for: 

time.sleep(1)
for linha in tabela.index:

    # Clicar no 1° campo: 
    pyautogui.click(x=632, y=365)
    # Código do produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("TAB")
    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("TAB")
    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("TAB")
    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("TAB")
    # Preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("TAB")
    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("TAB")
    # Observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("TAB")
    # Enviar o produto
    pyautogui.press("enter")
    pyautogui.scroll(5000)


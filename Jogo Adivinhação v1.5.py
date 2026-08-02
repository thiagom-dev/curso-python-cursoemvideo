import tkinter as tk
import random


# Criar a janela
janela = tk.Tk()
janela.title("Adivinhe o Número")
janela.geometry("400x300")
janela.resizable(False, False)


# Número que o computador pensou
computador = random.randint(0, 5)


def tentar():
    numero = int(campo.get())

    if numero == computador:
        resultado["text"] = "🎉 Você acertou!"
    else:
        resultado["text"] = f"❌ Você errou! Eu pensei em {computador}"


def novo_jogo():
    global computador
    computador = random.randint(0, 5)
    resultado["text"] = "Novo número escolhido!"


# Título
titulo = tk.Label(
    janela,
    text="Vou pensar em um número de 0 a 5",
    font=("Arial", 14)
)

titulo.pack(pady=20)


# Campo para digitar
campo = tk.Entry(
    janela,
    font=("Arial", 14),
    justify="center"
)

campo.pack()


# Botão tentar
botao = tk.Button(
    janela,
    text="Tentar",
    width=15,
    command=tentar
)

botao.pack(pady=10)


# Resultado
resultado = tk.Label(
    janela,
    text="Boa sorte!",
    font=("Arial", 12)
)

resultado.pack(pady=10)


# Novo jogo
botao_novo = tk.Button(
    janela,
    text="Novo jogo",
    command=novo_jogo
)

botao_novo.pack()


janela.mainloop()
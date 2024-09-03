import json
import tkinter as tk
from tkinter import messagebox, filedialog

# Função para adicionar uma nova rua e o número de lâmpadas queimadas ao relatório
def adicionar_rua():
    rua = rua_entry.get()  # Obtém o nome da rua do campo de entrada
    lampadas_queimadas = lampadas_queimadas_entry.get()  # Obtém o número de lâmpadas queimadas do campo de entrada
    
    # Verifica se o nome da rua não está vazio e se o número de lâmpadas queimadas é um número válido
    if rua and lampadas_queimadas.isdigit():
        relatorio[rua] = int(lampadas_queimadas)  # Adiciona ou atualiza a rua no dicionário de relatório
        atualizar_lista()  # Atualiza a lista exibida na interface gráfica
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, insira uma rua e uma lâmpada queimadas válida.")

# Função para remover uma rua do relatório
def remover_rua():
    rua = rua_entry.get()  # Obtém o nome da rua do campo de entrada
    if rua in relatorio:
        del relatorio[rua]  # Remove a rua do dicionário de relatório
        atualizar_lista()  # Atualiza a lista exibida na interface gráfica
    else:
        messagebox.showwarning("Rua não encontrada", "A rua que você tentou remover não está na lista.")

# Função para visualizar o relatório completo na área de texto
def visualizar_relatorio():
    visualizar_text.delete(1.0, tk.END)  # Limpa o conteúdo atual da área de visualização
    for rua, lampadas_queimadas in relatorio.items():
        visualizar_text.insert(tk.END, f"{rua}: {lampadas_queimadas}\n")  # Insere cada entrada do relatório na área de visualização

# Função para salvar o relatório em um arquivo JSON
def salvar_relatorio():
    nome_arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])  # Abre o diálogo para escolher o local e nome do arquivo
    if nome_arquivo:
        with open(nome_arquivo, "w") as arquivo:
            json.dump(relatorio, arquivo, indent=4)  # Salva o dicionário de relatório no arquivo JSON
        messagebox.showinfo("Salvo", f"Lista salva em {nome_arquivo}")  # Exibe uma mensagem de confirmação

# Função para carregar um relatório de um arquivo JSON
def carregar_relatorio():
    global relatorio  # Declara que a variável relatorio será usada globalmente
    nome_arquivo = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])  # Abre o diálogo para escolher o arquivo a ser carregado
    if nome_arquivo:
        with open(nome_arquivo, "r") as arquivo:
            relatorio = json.load(arquivo)  # Carrega o dicionário de relatório do arquivo JSON
        atualizar_lista()  # Atualiza a lista exibida na interface gráfica
        messagebox.showinfo("Carregado", f"Lista carregada de {nome_arquivo}")  # Exibe uma mensagem de confirmação

# Função para atualizar a lista exibida na interface gráfica
def atualizar_lista():
    lista_text.delete(1.0, tk.END)  # Limpa o conteúdo atual da área de texto da lista
    for rua, lampadas_queimadas in relatorio.items():
        lista_text.insert(tk.END, f"{rua}: {lampadas_queimadas}\n")  # Insere cada entrada do relatório na área de texto da lista

# Função para sair do aplicativo
def sair():
    root.destroy()  # Fecha a janela principal e encerra o aplicativo

# Criação da janela principal
root = tk.Tk()
root.title("Gerenciador de Relatório")

relatorio = {}  # Inicializa o dicionário que armazenará as informações das ruas e lâmpadas queimadas

# Layout da interface gráfica
frame = tk.Frame(root)
frame.pack(pady=10)

# Componentes da interface gráfica
rua_label = tk.Label(frame, text="Rua:")
rua_label.grid(row=0, column=0)
rua_entry = tk.Entry(frame)
rua_entry.grid(row=0, column=1)

lampadas_queimadas_label = tk.Label(frame, text="Lâmpadas queimadas:")
lampadas_queimadas_label.grid(row=1, column=0)
lampadas_queimadas_entry = tk.Entry(frame)
lampadas_queimadas_entry.grid(row=1, column=1)

# Botões de ação
adicionar_button = tk.Button(frame, text="Adicionar", command=adicionar_rua)
adicionar_button.grid(row=2, column=0, columnspan=2, pady=5)

remover_button = tk.Button(frame, text="Remover", command=remover_rua)
remover_button.grid(row=3, column=0, columnspan=2, pady=5)

visualizar_button = tk.Button(frame, text="Visualizar", command=visualizar_relatorio)
visualizar_button.grid(row=4, column=0, columnspan=2, pady=5)

salvar_button = tk.Button(frame, text="Salvar", command=salvar_relatorio)
salvar_button.grid(row=5, column=0, pady=5)

carregar_button = tk.Button(frame, text="Carregar", command=carregar_relatorio)
carregar_button.grid(row=5, column=1, pady=5)

sair_button = tk.Button(root, text="Sair", command=sair)
sair_button.pack(pady=10)

# Áreas de texto para exibição dos dados
lista_text = tk.Text(root, height=10, width=50)
lista_text.pack(pady=10)

visualizar_text = tk.Text(root, height=10, width=50)
visualizar_text.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()



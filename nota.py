import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Notas")
janela.geometry("400x200")
janela.configure(bg="Lightgrey")


vr = tk.StringVar()


tk.Label(janela, text= "Verificação de notas", font=("Arial", 16), bg="Lightgrey").pack(pady=10)

display = tk.Entry(janela, textvariable= vr, justify='center')
display.pack(pady=20)

def nota():
    try:
        valor = float(vr.get())

        if valor < 0 or valor > 10:
            raise ValueError  # Força erro se a nota for inválida

        if valor >= 7:
            resultado = "Aprovado"
        elif valor >= 5:
            resultado = "Recuperação"
        else:
            resultado = "Reprovado"

        messagebox.showinfo("Resultado", f"Aluno {resultado} com nota {valor:.1f}")
        vr.set("")

    except ValueError:
        messagebox.showerror("Erro", "Nota não condizente com o sistema")
    tk.Label()

tk.Button(janela, text="Verificar", bg= "lightGreen", command=nota).pack()

janela.mainloop()
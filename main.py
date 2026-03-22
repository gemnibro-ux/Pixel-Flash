import tkinter as tk
from PIL import Image, ImageTk
import PF

def run_vm():
    output_text.config(state="normal")
    code = input_text.get("1.0", tk.END)
    output, registers = vm.execute(code)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state="disabled")

def clear_console():
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")

vm = PF.VirtualMachine()
window = tk.Tk()
window.title("Pixel Flash")
window.geometry("700x500")
window.iconbitmap("assets/icon.ico")
window.resizable(width=False, height=False)

icon_original = Image.open("assets/icon.png")
icon_tk = ImageTk.PhotoImage(icon_original)
icon = tk.Label(window, image=icon_tk, height="30", width="30")
icon.place(x=5, y=5)

input_text = tk.Text(window, height=15, width=500, font=("Consolas", 10))
input_text.place(x=0, y=40)

tk.Button(window, text="▶ Запуск", command=run_vm, bg="#009920", relief="flat", fg="white").place(x=540, y=5)
tk.Button(window, text="🧹 Очистить", command=clear_console, bg="red", relief="flat", fg="white").place(x=610, y=5)

tk.Label(window, text="Результат:").place(x=0, y=300)
output_text = tk.Text(window, height=9.2, width=500, font=("Consolas", 12))
output_text.config(state="disabled")
output_text.place(x=0, y=330)

window.mainloop()
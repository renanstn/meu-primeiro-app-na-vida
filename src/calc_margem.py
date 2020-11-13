# Calculadora de margem

from Tkinter import *
import tkMessageBox


def calc():
	val = in1.get()
	val = float(val.replace(",","."))
	if op.get()==1:
		val_final = (val-(val*0.25))*1.4
	elif op.get()==2:
		val_final = (val-(val*0.25))*1.4
	elif op.get()==3:
		val_final = (val-(val*0.2))*1.4
	elif op.get()==4:
		val_final = val*1.4
	else:
		tkMessageBox.showerror("Erro", "Informe um fornecedor.")

	ret["text"]="R$ %.2f"%val_final


root=Tk()
root.title("Calculadora")
op=IntVar()

title=Label(root, text="Calculadora de Margem", bg="grey")
custo=Label(root, text="Custo bruto:")
in1=Entry(root)

op1=Radiobutton(root, text="Paulista", variable=op, value=1)
op2=Radiobutton(root, text="SM", variable=op, value=2)
op3=Radiobutton(root, text="Ipiranga", variable=op, value=3)
op4=Radiobutton(root, text="Acacia", variable=op, value=4)
bot=Button(root, text="Calcular", command=calc)
ret=Label(root, text="")

title.grid(row=0, column=0, columnspan=2, sticky=W+E)
custo.grid(row=1, column=0)
in1.grid(row=2, column=0)
op1.grid(row=1, column=1, sticky=W)
op2.grid(row=2, column=1, sticky=W)
op3.grid(row=3, column=1, sticky=W)
op4.grid(row=4, column=1, sticky=W)
bot.grid(row=3, column=0, sticky=W+E)
ret.grid(row=4, column=0, sticky=W+E)

root.geometry("+300+300")
root.mainloop()

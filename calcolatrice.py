import tkinter as tk

# Funzione per eseguire il calcolo 
def calcola(operazione):
    try:
        # Ottieni i valori dai campi di testo
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Esegui l'operazione selezionata
        if operazione == 'somma':
            risultato = num1 + num2
        elif operazione == 'sottrazione':
            risultato = num1 - num2
        elif operazione == 'moltiplicazione':
            risultato = num1 * num2
        elif operazione == 'divisione':
            if num2 != 0:
                risultato = num1 / num2
            else:
                risultato = "Errore: divisione per zero"
        else:
            risultato = "Operazione non riconosciuta"

        # Mostra il risultato
        label_risultato.config(text=f"Risultato: {risultato}")
    except ValueError:
        label_risultato.config(text="Errore: inserisci numeri validi")

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatrice Semplice")

# Creazione dei widget
label1 = tk.Label(root, text="Inserisci il primo numero:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Inserisci il secondo numero:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Etichetta per visualizzare il risultato
label_risultato = tk.Label(root, text="Risultato: ")
label_risultato.pack()

# Pulsanti per le operazioni
button_somma = tk.Button(root, text="Somma", command=lambda: calcola('somma'))
button_somma.pack()

button_sottrazione = tk.Button(root, text="Sottrazione", command=lambda: calcola('sottrazione'))
button_sottrazione.pack()

button_moltiplicazione = tk.Button(root, text="Moltiplicazione", command=lambda: calcola('moltiplicazione'))
button_moltiplicazione.pack()

button_divisione = tk.Button(root, text="Divisione", command=lambda: calcola('divisione'))
button_divisione.pack()

# Avvio dell'interfaccia grafica
root.mainloop()

import tkinter as tk
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mplcyberpunk

###########
prices = [1.0, 1.3, 1.1, 0.8, 0.6, 1.4, 1.5, 1.4, 0.9, 1.2, 1.3, 0.8, 1.2, 1.4, 1.5, 1.2, 0.8, 1.0, 1.1, 0.9, 1.0, 0.9, 1.0, 1.0, 1.1, 0.9, 1.0, 1.1, 1.2, 1.1, 1.4, 1.3, 1.3, 1.5, 1.5, 1.5, 1.6, 1.4, 1.5, 1.3, 1.2, 1.2, 1.1, 1.2, 1.2, 1.2, 1.0, 0.9, 1.0, 0.8, 0.8, 1.0, 0.9, 0.9, 1.0, 1.0, 1.2, 1.4, 1.3, 1.2, 1.5, 1.6, 1.6, 1.6, 1.5, 1.6, 1.5, 1.4, 1.5, 1.2, 1.3, 1.2, 1.2, 1.0, 1.1, 1.0, 0.9, 0.8, 1.0, 1.0, 1.1, 0.8, 0.9, 1.0, 1.3, 1.2, 1.4, 1.2, 1.3, 1.0]
updates = 3 #time in seconds
###########

it = 0
t = updates
root = tk.Tk()
height=root.winfo_screenheight()
width=root.winfo_screenwidth()
root.geometry(str(width)+"x"+str(height))
root.configure(bg='#212946')



title = tk.Label(root, text="Et Bou de Wall Street", font=("Helvetica Neue", 60, "bold"))
title.configure(bg='#212946', fg='white')
title.grid(row=0, column=0, columnspan=3)

price = tk.Label(root, text="Le jeton est actuellement à "+ str(prices[it]) +"€", font=("Helvetica Neue", 40))
price.configure(bg='#212946', fg='white')
price.grid(row=1, column=1)

counter = tk.Label(root, text="Prochaine mise à jour dans "+str(t)+" secondes", font=("Helvetica Neue", 20))
counter.configure(bg='#212946', fg='white')
counter.grid(row=2, column=1)

dpi=75
plt.style.use("cyberpunk")

graph = plt.Figure(figsize=(int(width/dpi), int(0.8*height/dpi)), dpi=dpi)
graphCanvas = FigureCanvasTkAgg(graph, root)

axes = graph.add_subplot()
axes.plot(prices[:it+1], marker='o')
axes.set_ylabel("Prix", fontsize = 20)
axes.set_xlabel("Temps", fontsize = 20)

mplcyberpunk.make_lines_glow(axes)

graphCanvas.get_tk_widget().grid(row=3, column=0, columnspan=3)

def update():
    global t, root, updates, axes, content, counter, graph, prices, axes, it, price
    t -= 1
    if t>1:
        counter.config(text="Prochaine mise à jour dans "+ str(t) +" secondes")
    elif t==1:
        counter.config(text="Prochaine mise à jour dans "+ str(t) +" seconde")
    else:
        t = updates
        it+=1
        counter.config(text="Prochaine mise à jour dans "+ str(t) +" secondes")
        price.config(text="Le jeton est actuellement à "+ str(prices[it]) +"€")
        graph.clear()
        axes = graph.add_subplot()
        axes.set_ylabel("Prix", fontsize = 20)
        axes.set_xlabel("Temps", fontsize = 20)
        axes.plot(prices[:it+1], marker='o')
        mplcyberpunk.add_glow_effects(axes, gradient_fill=True)
        graphCanvas.draw_idle()
    root.after(1000, update)

root.after(1000, update)
root.mainloop()

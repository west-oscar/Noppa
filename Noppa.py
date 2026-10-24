import random 
import tkinter as tk
class GraphicalDice:
    def __init__(self, root):
        self.root = root
        self.root.title("Graafinen Noppa")
        self.root.geometry("300x350")
        self.root.config(bg="#f0f0f0")

        # Otsikko
        self.label = tk.label(
            root,
            text="Heitä noppaa painamalla nappia",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        self.label.pack(pady=15)

        # Piirtoalusta nupille (Canvas)
        self.canvas = tk.canvas(
            root, width=150, height=150, bg="white", highlightthickness=2
        )
        self.canvas.pack(pady=10)

        # Heittonappi
        self.roll_button = tk.Button(
            root,
            text="Heitä noppaa",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=5,å
            command=self.roll_dice,
        )
        self.roll_button.pack(pady=15)

        # Piirretään aloitusnoppa (luku 1)
        self.draw_dice(1)
    def draw_dice(self, number):
        # Tyhjennetään alusta
        self.canvas.delete("all")

        # Pisteiden koordinaatit eri silmäluvuille (x, y)
        # Nopan koko on 150x150 joten koordinaatit skaalataan sen mukaan.
        r = 10 # Pisteen säde 
        # Pisteiden sijainnit: vasen, keski, oikea / ylä, keski, ala
        positions = {
            1: [(75, 75)],
            2: [(40, 40), (110, 110)],
            3: [(40, 40), (75, 75), (110, 110)],
            4: [(40, 40), (110, 40), (40, 110), (110, 110)],
            5: [(40, 40), (110, 40), (75, 75), (40, 110), (110, 110)],
            6: [(40, 40), (110, 40), (40, 75), (110, 75), (40, 110), (110, 110)],
        }

        # Piirretään pisteet valitun numeron mukaan
        for x, y in positions[number]:
            self.canvas.create_oval(
                x - r, y - r, x + r, y + r, fill="black", outline="black"
            )

        def roll_dice(self):
            # Arvotaan luku 1-6
            number = random.randint(1, 6)
            # Päivitetään teksti ja piirretään noppa uudelleen
            self.label.config(text=f"Heitit: {number}")
            self.draw_dice(number)

        # Ohjelman käynnistys
        if __name__ == "__main__":
            root = tk.TK()
            app = GraphicalDice(root)
            root.mainloop()
            
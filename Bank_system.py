#Bank system project using UI(tkinter etc...)
import tkinter as tk
from tkinter import messagebox

class BankSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank System")

        self.balance = 0.0

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.master, text="Bank System", font=("Helvetica", 16)).grid(row=0, column=1, pady=10)

        tk.Label(self.master, text="Balance: $").grid(row=1, column=0, sticky=tk.E)
        self.balance_label = tk.Label(self.master, text="0.0")
        self.balance_label.grid(row=1, column=1, sticky=tk.W)

        # Entry for amount
        tk.Label(self.master, text="Amount: $").grid(row=2, column=0, sticky=tk.E)
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(self.master, text="Deposit", command=self.deposit).grid(row=3, column=0, pady=10)
        tk.Button(self.master, text="Withdraw", command=self.withdraw).grid(row=3, column=1, pady=10)

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            self.balance += amount
            self.update_balance()

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            if self.balance >= amount:
                self.balance -= amount
                self.update_balance()
            else:
                messagebox.showwarning("Error", "Insufficient funds.")

    def get_amount(self):
        amount_str = self.amount_entry.get()
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            return amount
        except ValueError as e:
            messagebox.showwarning("Error", f"Invalid amount: {str(e)}")
            return None

    def update_balance(self):
        self.balance_label.config(text=f"{self.balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    bank_system = BankSystem(root)
    root.mainloop()

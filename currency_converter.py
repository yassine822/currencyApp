import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk

# -------------------- Currency List --------------------
currencies = {
    "USD": "US Dollar", "EUR": "Euro", "GBP": "British Pound", "JPY": "Japanese Yen",
    "CNY": "Chinese Yuan", "AUD": "Australian Dollar", "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc", "INR": "Indian Rupee", "BRL": "Brazilian Real",
    "ZAR": "South African Rand", "AED": "UAE Dirham", "SAR": "Saudi Riyal",
    "EGP": "Egyptian Pound", "MAD": "Moroccan Dirham", "RUB": "Russian Ruble",
    "TRY": "Turkish Lira", "SEK": "Swedish Krona", "NOK": "Norwegian Krone",
    "DKK": "Danish Krone", "SGD": "Singapore Dollar", "HKD": "Hong Kong Dollar",
    "KRW": "South Korean Won", "MXN": "Mexican Peso", "NZD": "New Zealand Dollar",
    "THB": "Thai Baht", "IDR": "Indonesian Rupiah", "PLN": "Polish Zloty",
    "CZK": "Czech Koruna", "HUF": "Hungarian Forint", "CLP": "Chilean Peso",
    "PHP": "Philippine Peso"
}

display_to_code = {f"{name} ({code})": code for code, name in currencies.items()}

def find_display_for_code(display_to_code, code):
    for display, c in display_to_code.items():
        if c == code:
            return display
    return list(display_to_code.keys())[0]

# -------------------- Conversion Function --------------------
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = display_to_code[from_combo.get()]
        to_currency = display_to_code[to_combo.get()]

        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response = requests.get(url, timeout=10).json()

        if response.get("result") == "success" and "rates" in response and to_currency in response["rates"]:
            rate = response["rates"][to_currency]
            result = amount * rate
            result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            messagebox.showerror("Error", f"Failed to fetch exchange rate.\nResponse: {response}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
    except requests.RequestException as e:
        messagebox.showerror("Connection Error", f"Failed to connect to exchange rate server.\n{e}")

# -------------------- GUI Setup --------------------
root = tk.Tk()
root.title("Currency Converter")
root.geometry("650x450")
root.resizable(False, False)

# ---------- Canvas for background ----------
canvas = tk.Canvas(root, width=650, height=450)
canvas.pack(fill="both", expand=True)

try:
    bg_img = Image.open("background.jpg")
    bg_img = bg_img.resize((650, 450), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
except Exception as e:
    print("Failed to load background:", e)
    canvas.config(bg="#2c3e50")  # fallback

# ---------- Title with Coin ----------
title_frame = tk.Frame(root, bg="#37a36d")  # solid color for readability
title_frame_window = canvas.create_window(325, 40, window=title_frame)

try:
    coin_img = Image.open("coin.png")
    coin_img = coin_img.resize((32,32), Image.Resampling.LANCZOS)
    coin_photo = ImageTk.PhotoImage(coin_img)
    coin_label = tk.Label(title_frame, image=coin_photo, bg="#37a36d")
    coin_label.pack(side="left", padx=(0,10))
except:
    coin_photo = None

title_label = tk.Label (title_frame, text="Currency Converter💰", font=("Arial", 22, "bold"),
                       fg="white", bg="#37a36d")
title_label.pack(side="left")

# ---------- Input Frame ----------
frame = tk.Frame(root, bg="#37a36d", padx=20, pady=20, relief="ridge", bd=3)
frame_window = canvas.create_window(325, 220, window=frame)

tk.Label(frame, text="Amount:", font=("Arial", 12), bg="#37a36d", fg="#ecf0f1").grid(row=0, column=0, padx=5, pady=5, sticky="w")
amount_entry = tk.Entry(frame, font=("Arial", 12), width=20, bd=2, relief="groove")
amount_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="From:", font=("Arial", 12), bg="#37a36d", fg="#ecf0f1").grid(row=1, column=0, padx=5, pady=5, sticky="w")
from_combo = ttk.Combobox(frame, values=list(display_to_code.keys()), width=27, font=("Arial", 11))
from_combo.set(find_display_for_code(display_to_code, "USD"))
from_combo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="To:", font=("Arial", 12), bg="#37a36d", fg="#ecf0f1").grid(row=2, column=0, padx=5, pady=5, sticky="w")
to_combo = ttk.Combobox(frame, values=list(display_to_code.keys()), width=27, font=("Arial", 11))
to_combo.set(find_display_for_code(display_to_code, "EUR"))
to_combo.grid(row=2, column=1, padx=5, pady=5)

# ---------- Convert Button ----------
convert_btn = tk.Button(root, text="Convert", command=convert_currency,
                        bg="#27ae60", fg="white", font=("Arial", 13, "bold"),
                        padx=12, pady=6, relief="raised", bd=3, activebackground="#2ecc71", activeforeground="white")
canvas.create_window(325, 370, window=convert_btn)

def on_enter(e):
    convert_btn['bg'] = '#2ecc71'
def on_leave(e):
    convert_btn['bg'] = '#27ae60'
convert_btn.bind("<Enter>", on_enter)
convert_btn.bind("<Leave>", on_leave)

# ---------- Switch Button ----------
def switch_currencies():
    from_value = from_combo.get()
    to_value = to_combo.get()
    from_combo.set(to_value)
    to_combo.set(from_value)

switch_btn = tk.Button(frame, text="⇄ Switch", command=switch_currencies,
                       bg="#27ae60", fg="white", font=("Arial", 11, "bold"),
                       padx=10, pady=3, relief="raised", bd=2, activebackground="#0de94b")
switch_btn.grid(row=1, column=2, padx=5, pady=5)


# ---------- Result Label ----------
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#37a36d", fg="#f1c40f")
canvas.create_window(325, 420, window=result_label)



root.mainloop()

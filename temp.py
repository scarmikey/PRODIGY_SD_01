import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def convert_temperature():
    temperature = float(temperature_entry.get())
    original_unit = original_unit_combobox.get().lower()

    if original_unit == 'celsius':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif original_unit == 'fahrenheit':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif original_unit == 'kelvin':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        result_label.config(text="Invalid unit of measurement.")
        return

    result_label.config(text=f"{temperature:.2f} {original_unit.capitalize()} is equal to:\n"
                              f"{fahrenheit:.2f} Fahrenheit\n"
                              f"{celsius:.2f} Celsius\n"
                              f"{kelvin:.2f} Kelvin")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Temperature entry
temperature_label = ttk.Label(root, text="Enter the temperature value:")
temperature_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
temperature_entry = ttk.Entry(root)
temperature_entry.grid(row=0, column=1, padx=5, pady=5)

# Original unit selection
original_unit_label = ttk.Label(root, text="Select the original unit of measurement:")
original_unit_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
original_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
original_unit_combobox.current(0)
original_unit_combobox.grid(row=1, column=1, padx=5, pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Result label
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

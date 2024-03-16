import gradio as gr
from datetime import datetime

class Bikeshop:
    def __init__(self, stock):
        self.stock = stock
        self.rental_history = []

    def display_bike(self):
        return f"Total available Bikes: {self.stock}"

    def rent_for_bike(self, quantity):
        if quantity <= 0:
            return "Enter valid value"
        elif quantity > self.stock:
            return "Sorry! Bike is unavailable"
        else:
            total_price = quantity * 100
            self.stock -= quantity
            self.rental_history.append((datetime.now(), quantity))
            return f"Total Price: {total_price}, Total available Bikes: {self.stock}"

    def return_bike(self, quantity):
        self.stock += quantity
        return f"Thank you for returning {quantity} bikes."

    def view_rental_history(self):
        history = "Rental History:\n"
        for rental in self.rental_history:
            history += f"- {rental[1]} bikes rented at {rental[0]}\n"
        return history

def bikeshop_interface(action, quantity):
    if action == "Display Bike":
        return bikeshop.display_bike()
    elif action == "Rent Bike":
        return bikeshop.rent_for_bike(quantity)
    elif action == "Return Bike":
        return bikeshop.return_bike(quantity)
    elif action == "View Rental History":
        return bikeshop.view_rental_history()

bikeshop = Bikeshop(100)

# Create Gradio Interface
iface = gr.Interface(fn=bikeshop_interface, 
                      inputs=[gr.Dropdown(["Display Bike", "Rent Bike", "Return Bike", "View Rental History"], label="Action"),
                              gr.Number(label="Quantity")],
                      outputs="text",
                      title="Bikeshop")

# Launch interface
iface.launch()

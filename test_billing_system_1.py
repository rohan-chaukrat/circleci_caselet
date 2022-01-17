from tkinter import*
from billing_system import Bill_App

def main():
    root = Tk()
    bill_app = Bill_App(root)
    bill_app.sanitizer = IntVar(root, value = 3)
    bill_app.thermal_gun = IntVar(root, value = 2)
    bill_app.wheat = IntVar(root, value = 20)
    bill_app.maggi = IntVar(root, value = 3)
    bill_app.sprite = IntVar(root, value = 2)
    bill_app.lassi = IntVar(root, value = 5)

    bill_app.total()

    assert bill_app.total_bill == 1404.8, "Error with Test 1"
    print("Test 1 passed")

if __name__ == "__main__":
    main()
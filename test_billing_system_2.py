from tkinter import*
from billing_system import Bill_App

def main():
    root = Tk()
    bill_app = Bill_App(root)
    bill_app.hand_gloves = IntVar(root, value = 10)
    bill_app.syrup = IntVar(root, value = 10)
    bill_app.rice = IntVar(root, value = 20)
    bill_app.flour = IntVar(root, value = 20)
    bill_app.mineral = IntVar(root, value = 10)
    bill_app.juice = IntVar(root, value = 10)

    bill_app.total()

    assert bill_app.total_bill == 2821.0, "Error with Test 2"
    print("Test 2 passed")

if __name__ == "__main__":
    main()
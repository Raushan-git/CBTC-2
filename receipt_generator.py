from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

class ReceiptGenerator:
    def __init__(self, filename='receipt.pdf'):
        self.filename=filename

    def generate_receipt(self, store_info, items, payment_info):
        try:
            c = canvas.Canvas(self.filename,pagesize=letter)
            width,height = letter


            #Header
            c.setFont("Helvetica-Bold",16)
            c.drawString(50, height - 50, store_info['name'])
            c.setFont("Helvetica", 12)
            c.drawString(50, height -70, store_info['address'])
            c.drawString(50, height-90, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            #Items
            c.drawString(50, height - 130, "Item")
            c.drawString(250, height - 130,"Quantity")
            c.drawString(350, height - 130, "Price")
            c.drawString(450, height -130, "Total")
            c.line(50, height -140, 500, height - 140)

            y = height - 160
            total_amount = 0
            for item in items:
                c.drawString(50, y, item['name'])
                c.drawString(250, y, str(item['quantity']))
                c.drawString(350, y, f"${item['price']:.2f}")
                total = item['quantity'] * item['price']
                c.drawString(450, y, f"${total:.2f}")
                total_amount += total
                y -= 20

            c.line(50, y - 10, 500, y - 10)

            # Total
            c.setFont("Helvetica-Bold", 12)
            c.drawString(350, y - 40, "Total Amount:")
            c.drawString(450, y - 40, f"${total_amount:2f}")

            # Pyment Info
            c.setFont("Helvetica", 12)
            c.drawString(50, y -80, f"Payment Method: {payment_info['method']}")
            c.drawString(50, y - 100, f"Receipt Number: {payment_info['receipt_number']}")

            # footer
            c.setFont("Helvetica-Oblique", 10)
            c.drawString(50, y -140, "Thnak you for your purchase!")
            c.save()
            print(f"Receipt saved as {self.filename}")

        except Exception as e:
            print(f"An error occurred while generating the receipt: {e}")

# Example usage

if __name__ == '__main__':
    store_info = {
        'name': 'BAZZAR INDIA',
        'address': '123 3Main Street, DElhi'

    }

    items = [
        {'name':'Apples', 'quantity': 2, 'price': 3.00},
        {'name': 'Bananas', 'quantity': 5, 'price': 1.50},
        {'name': 'Chocolate Bar', 'quantity': 1, 'price': 2.75}
    ]

    payment_info = {
        'method': 'Credit Card',
        'receipt_number': '9876543210'

    }


    receipt_gen = ReceiptGenerator('receipt.pdf')
    receipt_gen.generate_receipt(store_info, items, payment_info)









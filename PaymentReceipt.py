from reportlab.pdfgen import canvas
from datetime import datetime
import random
import string

width = 595.28
height = 841.89/2

def create_transactionID():
    characters = string.ascii_uppercase + string.digits 
    transactionID = ''.join(random.choice(characters) for _ in range(20))
    return 'T'+transactionID

def create_receipt(c):
    name = input("Enter the name: ")
    amt = float(input("Enter the amount: "))
    c.saveState()
    c.setFont("Times-Bold", 20)
    c.drawCentredString(595.28/2, height - 50,"Payment Receipt")

    c.rect(50, 160, width - 50-50, 200, stroke=1, fill=0)
    c.rect(51, 161, width - 51-51, 198, stroke=1, fill=0)

    c.setFont("Courier", 12)
    c.drawString(100,height - 100,"Transaction ID: " + create_transactionID())
    c.drawString(100,height - 115,"Date: " + datetime.now().strftime("%d.%m.%Y"))
    c.drawString(100,height - 130,"Payment Gateway: BILLDESK")
    c.drawString(100,height - 145,"Name: " + name.upper())
    c.drawString(100,height - 160,"Payment Mode: ONLINE")
    c.drawString(100,height - 175,"Subtotal: Rs. " + str(amt))
    c.drawString(100,height - 190,"TAX (18% GST): Rs. " + str((18/100)*amt))
    c.drawString(100,height - 205,"Received: Rs. " + str(amt + ((18/100)*amt)))
    
    c.setFont("Times-Roman", 12)
    c.drawCentredString(595.28/2,145,"Thank You for your Payment!")

    c.restoreState()
    print("Receipt created successfully!")

c = canvas.Canvas("CBT-CIP/Receipt.pdf", pagesize = (width, height))
c.setTitle("Receipt")
create_receipt(c)
c.showPage()
c.save()
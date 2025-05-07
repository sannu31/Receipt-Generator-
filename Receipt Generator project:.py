#Receipt Generator project:
# Set item quantities and prices
pen_qty = 5
pen_price = 12

book_qty = 4
book_price = 50

eraser_qty = 3
eraser_price = 5

# Calculate totals
pen_total = pen_qty * pen_price
book_total = book_qty * book_price
eraser_total = eraser_qty * eraser_price

total = pen_total + book_total + eraser_total

# Print receipt
print("==============================")
print("Welcome | to | My Shop")
print("==============================")

print("Item | Qty | Total")
print("Pen |", pen_qty, "| ₹", pen_total)
print("Book |", book_qty, "| ₹", book_total)
print("Eraser |", eraser_qty, "| ₹", eraser_total)

print("------------------------------")
print("Total | ₹", total)

print("==============================")
print("Thank ~ You ~ Visit Again! :)")
print("==============================")



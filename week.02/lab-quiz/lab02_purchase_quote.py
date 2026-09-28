item1_name = input("1. Ürün adı:")
item1_qty = int(input("1. Ürün adedi:"))
item1_price = float(input("1. Ürün birim fiyatı (TRY):"))

item2_name = input("2. Ürün adı:")
item2_qty = int(input("2. Ürün adedi:"))
item2_price = float(input("2. Ürün birim fiyatı (TRY):"))


delivery_fee = float(input("Teslimat ücreti (TRY):"))
tax_percentage = float(input("Vergi oranı (%):"))

item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
subtotal = item1_total + item2_total

tax_amount = subtotal * (tax_percentage / 100)
final_total = subtotal + tax_amount + delivery_fee

print("\n--- SİPARİŞ TEKLİFİ / HESAP DÖKÜMÜ ---")
print(f"{item1_name} ({item1_qty} adet): {item1_total:.2f} TRY")
print(f"{item2_name} ({item2_qty} adet): {item2_total:.2f} TRY")
print(f" Ara Toplam (Subtotal): {subtotal:.2f} TRY")
print(f" Vergi (%{tax_percentage:.0f}): {tax_amount:.2f} TRY")
print(f" Teslimat Ücreti: {delivery_fee:.2f} TRY")
print(f" Genel Toplam: {final_total:.2f} TRY")

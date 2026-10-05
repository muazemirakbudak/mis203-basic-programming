# lab03_order_approval.py

# Kullanıcıdan girdileri alıyoruz
order_amount = float(input("Sipariş tutarını girin (TRY): "))
available_stock = int(input("Mevcut stok miktarını girin: "))
requested_quantity = int(input("İstenen miktarı girin: "))
is_member_input = input("Müşteri üye mi? (evet/hayır): ").strip().lower()

is_member = is_member_input == "evet"

# Geçersiz miktar veya yetersiz stok kontrolü (Doğrulama / Hata Durumları)
if requested_quantity <= 0 or order_amount <= 0:
    print("Hata: Geçersiz miktar veya sipariş tutarı.")
elif requested_quantity > available_stock:
    print("Sipariş Reddedildi: Yetersiz stok.")
else:
    # Sipariş onaylandı, indirim hesabı
    discount = 0.0
    reason = "Sipariş onaylandı."

    # 'and' mantıksal operatörü ile 500 TRY ve üyelik şartı kontrolü
    if is_member and order_amount >= 500:
        discount = 0.10
        reason = "Sipariş onaylandı (%10 üye indirimi uygulandı)."

    final_price = order_amount * (1 - discount)
    
    print(reason)
    print(f"Nihai Fiyat: {final_price:.2f} TRY")

tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name_input = input("Customer name (or q to quit): ").strip()
    
    if name_input.lower() == 'q':
        break
        
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day_input = input("Day (weekday/weekend): ").strip().lower()
    if day_input not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    student_input = input("Student (yes/no): ").strip().lower()
    if student_input not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    # Taban fiyat belirleme
    if day_input == "weekday":
        base_price = 200.0
    else:
        base_price = 250.0

    # İndirim kurallarını kontrol etme (ÖNEMLİ: Sıralama hassastır)
    if age < 6:
        discount = 1.00
        category = "Free"
    elif age >= 65:
        discount = 0.50
        category = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40
        category = "Child"
    elif student_input == "yes" and age <= 25:
        discount = 0.30
        category = "Student"
    else:
        discount = 0.00
        category = "Standard"

    final_price = base_price * (1 - discount)

    # İstatistikleri güncelleme
    tickets_sold += 1
    total_revenue += final_price
    if category == "Free":
        free_tickets += 1

    # Müşteri sonucunu yazdırma
    print(f"{name_input}: {final_price:.2f} TRY ({category})")

# Özet raporu
if tickets_sold > 0:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold} Total revenue: {total_revenue:.2f} TRY Average price: {avg_price:.2f} TRY Free tickets: {free_tickets}")
else:
    print("No tickets sold.")

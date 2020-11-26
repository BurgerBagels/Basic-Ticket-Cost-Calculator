price = float(input("How much are tickets? (excluding service charge) £"))
people = int(input("How many people are going? "))
service = float(input("How much is the service charge? £"))

ticket_cost = round(price * people, 2)
service_charge = people * service
total_amount = round(ticket_cost + service_charge, 2)

print(f"The total amount will be £{total_amount}")
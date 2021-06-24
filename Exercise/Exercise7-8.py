sandwich_orders = ['A1', 'B2', 'pastrami', 'C3', 'D4', 'pastrami', 'E5', 'pastrami']
finished_sandwich = []

print("\nMarket's pastrami is None.")

i = 0
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    i = i + 1
    print(f"\nI del {i} pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        print(f"\nI del one {current_sandwich} sandwich.")
    elif current_sandwich != 'pastrami':
        print(f"\nI made your {current_sandwich} sandwich. ")
        finished_sandwich.append(current_sandwich)


print("\nI have made sandwich:")
for sandwich in finished_sandwich:
    print(f"{sandwich}")




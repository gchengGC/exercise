guestes = ['wang wei', 'zhuang ying', 'gong cheng']
print(guestes)

guestes.remove('wang wei')
guestes.append('zhang bi yue')
for guest in guestes:
    print(f"Hello {guest.title()},Please join the Party.")

print(guestes)
guestes.insert(0, 'gong guang feng')
guestes.insert(int(len(guestes)/2), 'wang hong')
guestes.insert(int(len(guestes)), 'wang wei')
guestes.append('li gen')
for guest in guestes:
    print(f"\tHello {guest.title()},because I find a larger table, please come on.")

while len(guestes) > 2:
    last_guest = guestes.pop()
    print(f"{last_guest.title()},I'm so sorry you can not join the party,")

while len(guestes) > 0:
    join_guest = guestes[int(len(guestes) - 1)]
    print(f"{join_guest.title()},please join the party. ")
    del guestes[int(len(guestes) - 1)]
    if guestes == []:
        print("The guestes is Null")

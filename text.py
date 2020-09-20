for i in range(1, 8):
    with open(f"es/{i}.txt") as txt:
        t = txt.read()
        t = t.lower()
    with open(f"es/{i}.txt", 'w') as txt:
        txt.write(t)
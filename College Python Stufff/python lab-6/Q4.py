d1 = {1: "hello", 2: "world", 3: "how are you"}
d2 = {2: "i am fine", 3: "how about you", 4: "i am fine too"}
d1.update(d2)
d2.update(d1)
print(d1)
print(d2)

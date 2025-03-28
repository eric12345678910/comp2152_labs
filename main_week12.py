from mammal import Mammal
from person2 import Person
from tick import Tick
from puma import Puma

m = Mammal(10)
m.speak()

# Mammal.speak(m) # same thing as above

print(m)

p = Person("John Doe", 20, 6)
p.speak()
print(p)
p.heart.beat()
print(p.heart)

print(m.heart == p.heart)

t = Tick()
t.suck_blood()
print(t)

pm = Puma(5, t)
pm.tick.suck_blood()
print(pm)

pm2 = Puma(3)
pm2.claw()
pm2.tick.suck_blood()

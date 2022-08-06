import random
def random_a_float():
    random_int = random.randint(0, 4)
    random_float = random.random()
    random_float_0_to_5 = random_int + random_float
    print(random_float_0_to_5)

for i in range(1,100):
    random_a_float()


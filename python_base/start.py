import hello
# import math
from mod import math
import random
hello.some()
print(math.pi)
r = random.randrange(0, 10)
user = "User"
user_random = user + str(r)
print(user_random)

from mod import some

some.sum(10, 5)
some.sub(10, 5)
import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special = "!(){}[]?;/?-_"


all = lower + upper + num + special
length = 16

password = "".join(random.sample(all,length))
print ("Your new password is: ", password, "\n")

initial = 1000
rate = 0.07

a10 = initial*((1+rate)**10)
a20 = initial*((1+rate)**20)
a30 = initial*((1+rate)**30)

print("Suppose you start with", initial, "dollars and that the annual rate is",
      rate)
print("After 10 years you will have", a10, "dollars in your account")
print("After 20 years you will have", a20, "dollars in your account")
print("After 30 years you will have", a30, "dollars in your account")
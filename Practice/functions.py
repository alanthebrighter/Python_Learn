# positional args
def concat_name(fname, mname, lname):
  return f"{fname} {mname} {lname}"

print(concat_name("John", "James", "Jaison"))

# default args
def min_age(year, day=15, month=6, ):
  if (2025>=18):
    return f"{month}/{day}/{year} pass!"

print(min_age(2000, 15))

# keyword args
def greetings(greeting, title, lname):
  return f"{greeting} {title} {lname}!"

print(greetings(greeting="Welcome", title="Sr.", lname="Smith"))

# *args args
def listOfInvites(*args):
  for arg in args:
    print(arg, end=", ")

listOfInvites("john", "mary", "clair", "michael", "marceline")
print()

# **kwargs args
def address(**kwargs):
  print(f"City: {kwargs.get('city')}, State: {kwargs.get("state")}, Country: {kwargs.get("country")}")

address(
  city="Curitiba",
  state="Parana",
  country="Brazil"
)


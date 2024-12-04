import re

texto = "O email é exemplo@dominio.com"
email = re.search(r'\S+@\S+\.\S+', texto)
if email:
    print(email.group())

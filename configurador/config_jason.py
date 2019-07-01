import json


with open("termostato.json", "r") as termostato_config:
    termostato = json.load(termostato_config)
print(termostato["proxy_bateria"])
import json
from datetime import date
#import utils
from utils import date_handler

familia = {
    "malu": "la mas malusita",
    "chuko": "His name es xhuko",
    "jose": "Chess master",
    "dany": "he got first place on master challenge"

}
pendientes = ["Escaleras","Arreglar baño", "comprar bicis"]

deudas = {"Scotia":300.12, "banamex": 100}

hobbies = {"malu":None, "pepe": "ajedrez", "Dany":"leer"}
saludo="hola mundo que tal!"
pi= 3.1416
hoy = date.today()
llueve=False
puerta=True


data ={}
data["llueve"]= llueve
data["puerta"]= puerta
data["familia"] = familia
data["pendientes"]= pendientes
data["hobbies"] = hobbies
data["saludo"] = saludo
data["pi"]=pi
data["hoy"]=hoy
#data=data.encode("utf-8")
print(data)

json_data = json.dumps(data, default=date_handler,sort_keys=True, indent=4,ensure_ascii=False)
print (json_data)

#with

with open('data/test_write.csv','w') as f:
    f.write(json_data)
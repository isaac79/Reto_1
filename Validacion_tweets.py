import json

# Esquema de tweet y definición de tipo de datos
schema ={
    "id": str,
    "texto": str,
    "usuario": str,
    "hashtags": list,
    "fecha": str,
    "retweets": float,
    "favoritos": float
}

# Carga de tweets desde archivo json
t_json = "tweets_extraction.json"
with open(t_json, "r", encoding="utf-8") as archivo:
    tweets_data = json.load(archivo)

# Validación de cada tweet
def validacion_tweet(tweet, schema):
    for key, tipo_dato in schema.items():
        if key not in tweet:
            print(f"Clave faltante: {key}")
            return False
        if not isinstance(tweet[key], tipo_dato):
            print(f"Tipo de dato incorrecto para clave '{key}")
            return False
    return True

# Validación de tweets
tweets_validos = list()

for tweet in tweets_data:
    if validacion_tweet(tweet, schema):
        tweets_validos.append(tweet)
        print(f"Tweet válido: {tweet}")
    else:
        print(f"Tweet inválido: {tweet}")


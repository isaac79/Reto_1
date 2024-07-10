import mysql.connector
from datetime import datetime
import json

# Configuración de conexión a DB
DB_config = {
    "user": "root",
    "password": "Mysqlpassword24",
    "host": "localhost",
    "database": "r_sql"
}

# Conexión a DB
conexion = mysql.connector.connect(**DB_config)
cursor = conexion.cursor()

# Esquema de tweet y definición de tipo de datos
schema = {
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
            print(f"Tipo de dato incorrecto para clave '{key}'")
            return False
    return True

# Validación de tweets
tweets_validos = []

for tweet in tweets_data:
    if validacion_tweet(tweet, schema):
        tweets_validos.append(tweet)
        print(f"Tweet válido: {tweet}")
    else:
        print(f"Tweet inválido: {tweet}")

# Inserción a BD
insercion = """
INSERT INTO tweets (id, texto, usuario, hashtags, fecha, retweets, favoritos)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Conversión de formato de fecha a Datetime de Mysql
def conversion_formato_fecha(date):
    return datetime.fromisoformat(date.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S")

# Inserción de tweets en la BD
for tweet in tweets_validos:
    data = (
        tweet["id"],
        tweet["texto"],
        tweet["usuario"],
        json.dumps(tweet["hashtags"]),  # Convertir lista de hashtags a JSON
        conversion_formato_fecha(tweet["fecha"]),
        tweet["retweets"],
        tweet["favoritos"]
    )
    cursor.execute(insercion, data)

conexion.commit()
cursor.close()
conexion.close()

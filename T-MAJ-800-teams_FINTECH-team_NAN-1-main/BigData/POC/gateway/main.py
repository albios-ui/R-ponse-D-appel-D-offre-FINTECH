from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from google.cloud import storage
from confluent_kafka import Producer
import json
import random

app = FastAPI()


@app.get("/")
async def root():
	message = {"message": "API Gateway is Up"}
	return message


def upload_json_to_gcs(data):
	try:
		# Crée un client
		storage_client = storage.Client()

		# Obtient le bucket
		bucket = storage_client.bucket("bucket-poc-fintech")

		# Génère un nom de fichier unique
		blob_name = datetime.now().isoformat() + ".json"

		# Crée un nouveau blob
		blob = bucket.blob("datas_struct/" + blob_name)

		# Convertit les données en chaîne JSON
		json_data = json.dumps(data.dict())

		# Envoie les données au blob
		return blob.upload_from_string(json_data, content_type='application/json')

	except Exception as e:
		return e


class Datas(BaseModel):
	id: int
	lat: str
	long: str
	type: str
	speed: float


types = ["train", "metro", "tramway", "bus", "taxi"]


@app.post("/datas/")
async def datas(datas_for_gcp: Datas):
	try:
		for i in range(0, 10):
			datas_for_gcp.id = random.randint(11, 20)
			datas_for_gcp.lat = str(random.uniform(0, 100))
			datas_for_gcp.long = str(random.uniform(0, 100))
			datas_for_gcp.type = random.choice(types)
			datas_for_gcp.speed = random.uniform(0, 100)
			produce_message("topic-test", 'datas', {
				'id': datas_for_gcp.id,
				'lat': datas_for_gcp.lat,
				'long': datas_for_gcp.long,
				'type': datas_for_gcp.type,
				'speed': datas_for_gcp.speed
			})

		return "Ok"
	except Exception as e:
		e = "Server error"
		return e


def delivery_report(err, msg):
	if err is not None:
		print('Message delivery failed: {}'.format(err))
	else:
		print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


def produce_message(topic, key, value):
	try:
		# Créer un producteur en spécifiant l'adresse du serveur Kafka
		p = Producer({'bootstrap.servers': '51.15.206.248:9092'})

		# Convert the key and value to JSON
		key = json.dumps(key)
		value = json.dumps(value)

		p.produce(topic, key=key, value=value, callback=delivery_report)

		# Wait for any outstanding messages to be delivered and delivery reports
		# to be received.
		p.flush()

		return "ok"

	except Exception as e:
		return e

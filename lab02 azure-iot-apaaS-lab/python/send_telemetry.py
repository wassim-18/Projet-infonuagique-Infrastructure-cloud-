# -------------------------------------------------------------------------
# Azure IoT Hub -> Telemetry JSON (CosmosDB friendly)
# -------------------------------------------------------------------------
import os
import uuid
import time
import json
import random
from datetime import datetime, timezone

from azure.iot.device import IoTHubDeviceClient, Message


def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Variable d'environnement manquante: {name}\n"
            f"Windows PowerShell:  setx {name} \"<ta_connection_string>\"\n"
            f"Puis ferme/ré-ouvre le terminal et relance le script."
        )
    return value


def main():
    # ✅ NE PAS stocker la clé dans le code
    # Mets ta connection string dans une variable d'environnement:
    # Windows: setx IOTHUB_DEVICE_CONN "<HostName=...;DeviceId=...;SharedAccessKey=...>"
    conn_str = get_env("IOTHUB_DEVICE_CONN")

    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Important pour CosmosDB : deviceId doit correspondre à la partition key /deviceId
    device_id = os.getenv("DEVICE_ID", "collecte_temperature_1")

    print("IoTHub Device Client Recurring Telemetry Sample")
    print("Press Ctrl+C to exit")

    try:
        device_client.connect()

        i = 0
        while True:
            i += 1

            # ✅ Payload JSON (CosmosDB / PowerBI / Synapse friendly)
            payload = {
                "id": str(uuid.uuid4()),  # id unique Cosmos (recommandé)
                "deviceId": device_id,    # ✅ correspond à /deviceId
                "seq": i,
                "temperature": round(20 + random.random() * 10, 2),
                "humidity": round(40 + random.random() * 30, 2),
                "ts": datetime.now(timezone.utc).isoformat()
            }

            msg = Message(json.dumps(payload))
            msg.message_id = str(uuid.uuid4())
            msg.correlation_id = "correlation-1234"
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json"

            # (Optionnel) propriétés applicatives
            msg.custom_properties["source"] = "python-simulator"
            msg.custom_properties["lab"] = "apaaS-iot"

            print(f"sending message #{i}: {payload}")
            device_client.send_message(msg)
            time.sleep(10)

    except KeyboardInterrupt:
        print("User initiated exit")
    finally:
        device_client.shutdown()


if __name__ == "__main__":
    main()

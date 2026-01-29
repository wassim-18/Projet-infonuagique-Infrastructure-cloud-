import os
from flask import Flask, render_template_string
from azure.cosmos import CosmosClient

CONNSTR = os.getenv("COSMOS_CONNSTR")
if not CONNSTR:
    raise RuntimeError("Variable manquante: COSMOS_CONNSTR")

DATABASE = "iotdb"
CONTAINER = "telemetry"

app = Flask(__name__)

client = CosmosClient.from_connection_string(CONNSTR)
db = client.get_database_client(DATABASE)
container = db.get_container_client(CONTAINER)




@app.route("/")
def index():

    query = "SELECT TOP 20 * FROM c ORDER BY c._ts DESC"
    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))

    html = """
    <h1>📡 Données IoT</h1>
    <table border=1>
    <tr>
      <th>Device</th>
      <th>Temp</th>
      <th>Humidité</th>
      <th>Date</th>
    </tr>

    {% for i in items %}
    <tr>
      <td>{{ i.Body.deviceId }}</td>
      <td>{{ i.Body.temperature }}</td>
      <td>{{ i.Body.humidity }}</td>
      <td>{{ i.Body.ts }}</td>
    </tr>
    {% endfor %}
    </table>
    """

    return render_template_string(html, items=items)


if __name__ == "__main__":
    app.run(debug=True)

import csv
import sys
from datetime import datetime
from pythonosc import dispatcher, osc_server

csv_file = '/data/stream_data.csv'
with open(csv_file, mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'DataType', 'Values'])

def handle_osc_message(unused_addr, *args):
    timestamp = datetime.now().isoformat()
    data = list(args)
    data_type = type(data[0]).__name__ if data else 'Unknown'

    # Save the data to the CSV file
    with open(csv_file, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, data_type, data])

    print(f"Received message at {timestamp} - Type: {data_type}: {data}")

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/*", handle_osc_message)  # Map all OSC addresses to the handler

try:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print(f"Serving on {server.server_address}")
except Exception as e:
    print(f"Encountered {e}")

# Start the server
server.serve_forever()

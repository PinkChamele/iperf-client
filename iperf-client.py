import subprocess
import json
import math

server_ip = "127.0.0.1"

def client(server_ip):
    iperf_process = subprocess.Popen(["iperf3", "-c", server_ip, "-J"], stdout=subprocess.PIPE)

    return iperf_process.stdout

def parser(output):
    parsed_output = []
    decoded_json = output.read().decode("utf-8")
    parsed_json = json.loads(decoded_json)

    if parsed_json["error"]:
      raise Exception(parsed_json["error"])

    for interval in parsed_json["intervals"]:
      p = math.pow(1024, 3)
      start = round(interval["sum"]["start"], 2)
      end = round(interval["sum"]["end"], 2)
      transfer = round(interval["sum"]["bytes"] / p, 2)
      bitrate = round(interval["sum"]["bits_per_second"] / p, 2)

      if transfer > 2 and bitrate > 20:
        parsed_output.append({
            "Interval": f"{start}-{end}",
            "Transfer": transfer,
            "Bitrate": bitrate,
        })

    return parsed_output

client_output = client(server_ip)
parsed_output = parser(client_output)

for line in parsed_output:
  print(f"{line}\n")

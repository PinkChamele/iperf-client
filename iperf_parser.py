import json
import math

def parse(output):
    parsed_output = []
    decoded_json = output.read().decode("utf-8")
    parsed_json = json.loads(decoded_json)

    if parsed_json.get("error", None):
      raise Exception(parsed_json["error"])

    for interval in parsed_json["intervals"]:
      start = round(interval["sum"]["start"], 2)
      end = round(interval["sum"]["end"], 2)
      transfer = round(interval["sum"]["bytes"] / math.pow(1024, 3), 2)
      bitrate = round(interval["sum"]["bits_per_second"] / math.pow(1000, 3), 2)

      if transfer > 2 and bitrate > 20:
        parsed_output.append({
            "Interval": f"{start}-{end}",
            "Transfer": transfer,
            "Bitrate": bitrate,
        })

    return parsed_output

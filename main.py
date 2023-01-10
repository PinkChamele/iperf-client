import iperf_client
import iperf_parser

server_ip = "127.0.0.1"

if __name__ == "__main__":
  client_output = iperf_client.connect(server_ip)
  parsed_output = iperf_parser.parse(client_output)

  for line in parsed_output:
    print(f"{line}\n")

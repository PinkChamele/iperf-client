import subprocess

def connect(server_ip):
    iperf_process = subprocess.Popen(["iperf3", "-c", server_ip, "-J"], stdout=subprocess.PIPE)

    return iperf_process.stdout

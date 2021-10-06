#!/usr/bin/python
import socket
import netifaces
import time
import prometheus_client


cloudflare_dns = '1.1.1.1'
google_dns_a = '8.8.8.8'
google_dns_b = '8.8.4.4'
interval = 5
socket_port = 53
socket_timeout = 3


def has_connection(ip):

    try:
        socket.setdefaulttimeout(socket_timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, socket_port))
        return True
    except socket.error as ex:
        print(f"{ex}, '{ip}'' not reachable!")
        return False


if __name__ == '__main__':

    # start prometheus server
    prometheus_client.start_http_server(9090)

    # log connection to (part of) internet
    while True:     # todo: better way than infinity loop?

        # get available gateways
        gateways = netifaces.gateways()

        # check if default gateway value exists
        if netifaces.AF_INET not in gateways['default']:
            print("Default gateway not available!")
        else:
            default_gateway = gateways['default'][netifaces.AF_INET][0]

            # check connection to default gateway
            if has_connection(default_gateway):
                # check connection to different big infrastructures
                up = has_connection(cloudflare_dns) or has_connection(google_dns_a) or has_connection(google_dns_b)
                print(f"Internet up: {up}")
            else:
                print(f"Default gateway '{default_gateway}' not reachable!")

        time.sleep(interval)

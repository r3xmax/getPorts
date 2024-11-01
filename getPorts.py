#!/usr/bin/env python3

import os
import datetime
import re
import argparse

## Colors
color_red = '\033[31m'
color_reset = '\033[0m'

parser = argparse.ArgumentParser()

parser.add_argument("file", type=str, help="Nmap output file grepeable (-oG)")

args = parser.parse_args()

try:

    ## Extract Ports
    with open(args.file, "r") as file:
        file_content = file.read()

    ports = re.findall(r"\s(\d+)\/", file_content)

    ports_list = []

    for port in ports:
    
        port = port.strip(" /")
        ports_list.append(port)

    open_ports = ",".join(ports_list)


    ## Copy the ports on the clipboard
    os.system(f"echo {open_ports} | tr -d '\n' | xclip -sel clip")


    ## Extract Host
    with open(args.file, "r") as file:
        file_content = file.read()

    host = re.search(r"Host: \d+\.\d+\.\d+\.\d+", file_content)


    ## Edit File Grepeable de Nmap

    date = datetime.datetime.today()
    content = f"""
    [+] Information Extracted from Nmap file '{args.file}' on {date}

    [+] {host.group()}

    [+] Open Ports: {open_ports}

    [i] The ports are copied to your clipboard
    """

    with open(args.file, "w") as file:

        file.write(content)


except FileNotFoundError:
    print(f"\n{color_red}[!] Error: File '{args.file}' does not exist.{color_reset}")

except PermissionError:
    print(f"\n{color_red}[!] Error: You do not have permission to edit the file {args.file}. Please check if you have the necessary permissions to edit the file or run extractPorts as root.{color_reset}")

except AttributeError:
    print(f"\n{color_red}[!] Error: The file is not greppable or does not contain sufficient information for filtering. Please check if you used the -oG option to output the results to a file.{color_reset}")


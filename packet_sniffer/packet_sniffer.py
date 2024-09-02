import socket
import struct
import textwrap

# Function to parse Ethernet header
def parse_ethernet_header(data):
    # Unpack the Ethernet header using struct
    eth_header = struct.unpack('!6s6sH', data[:14])
    # Convert protocol number from network byte order to host byte order
    eth_protocol = socket.ntohs(eth_header[2])
    # Return the protocol type and the remaining data after the Ethernet header
    return eth_protocol, data[14:]

# Function to parse IP header
def parse_ip_header(data):
    ip_header = struct.unpack('!BBHHHBBH4s4s', data[:20])
    version_ihl = ip_header[0]               # First byte: version and IHL
    version = version_ihl >> 4               # Extract the IP version
    ihl = (version_ihl & 0xF) * 4            # Extract IHL and convert to bytes
    ttl = ip_header[5]                       # Time to live
    protocol = ip_header[6]                  # Protocol number (e.g., TCP, UDP)

    # Convert the raw IP addresses to human-readable format
    src_ip = socket.inet_ntoa(ip_header[8])                   # Source IP
    dest_ip = socket.inet_ntoa(ip_header[9])                  # Destination IP
    return version, ihl, ttl, protocol, src_ip, dest_ip, data[ihl:]

# Function to get the protocol name
def get_protocol_name(protocol_number):
    if protocol_number == 1:
        return 'ICMP'
    elif protocol_number == 6:
        return 'TCP'
    elif protocol_number == 17:
        return 'UDP'
    else:
        return 'Other'
    

# Main function to listen for and process packets
def listen_for_packets() :
    # Create a raw socket to capture all network packets
    try:
        sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except PermissionError:
        # Print an error message if the script is not run with administrative privileges
        print("You need to run this script with administrative privileges.")
        exit()

    # Listen for packets
    while True:
        # Receive raw data from the socket
        raw_data, addr = sniffer_socket.recvfrom(65535)
        
        # Parse the Ethernet header from the raw data
        eth_protocol, ip_data = parse_ethernet_header(raw_data)
        
        # Check if the Ethernet protocol is IP (0x0800)
        if eth_protocol == 8:
            # Parse the IP header from the IP data
            version, ihl, ttl, protocol, src_ip, dest_ip, ip_payload = parse_ip_header(ip_data)
            
            # Get the protocol name based on the protocol number
            protocol_name = get_protocol_name(protocol)

            # Format the payload data as a string for readability, wrapped at 80 characters
            data = textwrap.fill(str(ip_payload), width=80)

            # Print the source and destination IP addresses, and the protocol name
            print(f"IP Packet: {src_ip} -> {dest_ip}  |  Protocol: {protocol_name} ")
        
            # Print the payload data
            print(f"\t The payload data is : \n {data} \t \t")

if __name__ == "__main__" :
    print("Welcome to your packet sniffer, feel free to try it! \n Packet Sniffer Started...")
    listen_for_packets()

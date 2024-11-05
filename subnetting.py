def get_ip_class_and_mask(ip):
    first_octet = int(ip.split('.')[0])

    if 1 <= first_octet <= 126:
        return 'A', '255.0.0.0'
    elif 128 <= first_octet <= 191:
        return 'B', '255.255.0.0'
    elif 192 <= first_octet <= 223:
        return 'C', '255.255.255.0'
    elif 224 <= first_octet <= 239:
        return 'D', 'Invalid subnet mask'
    elif 240 <= first_octet <= 254:
        return 'E', 'Invalid subnet mask'
    else:
        return 'Unknown', None

def calculate_network_and_broadcast(ip, mask):
    ip_addr_parts = ip.split('.')
    mask_parts = mask.split('.')

    network_addr = []
    broadcast_addr = []

    for i in range(4):
        ip_part = int(ip_addr_parts[i])
        mask_part = int(mask_parts[i])
        
        network_part = ip_part & mask_part
        broadcast_part = network_part | (mask_part ^ 255)
        
        network_addr.append(str(network_part))
        broadcast_addr.append(str(broadcast_part))

    return '.'.join(network_addr), '.'.join(broadcast_addr)

def main():
    ip = input("ENTER IP: ")

    ip_class, mask = get_ip_class_and_mask(ip)
    
    if mask and mask != 'Invalid subnet mask':
        print(f"Class {ip_class} IP Address")
        print(f"SUBNET MASK:\n{mask}")

        network_addr, broadcast_addr = calculate_network_and_broadcast(ip, mask)

        print(f"First IP of block: {network_addr}")
        print(f"Last IP of block: {broadcast_addr}")
    elif mask == 'Invalid subnet mask':
        print(f"Class {ip_class} IP Address")
        print("SUBNET MASK: Invalid subnet mask")
    else:
        print("Invalid IP address")

# Correct the __name__ check
if __name__ == "__main__":
    main()

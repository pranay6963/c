import socket


def dns_lookup():
    choice = input("Enter '1' to find URL from IP or '2' to find IP from URL: ")

    if choice == '1':
        ip_address = input("Enter the IP address: ")
        try:
            url = socket.gethostbyaddr(ip_address)
            print(f"The URL for IP address {ip_address} is: {url[0]}")
        except socket.herror:
            print("URL not found for the given IP address.")

    elif choice == '2':
        url = input("Enter the URL: ")
        try:
            ip_address = socket.gethostbyname(url)
            print(f"The IP address for URL {url} is: {ip_address}")
        except socket.gaierror:
            print("IP address not found for the given URL.")

    else:
        print("Invalid choice. Please enter '1' or '2'.")


# Run the DNS lookup program
dns_lookup()
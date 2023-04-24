from zeroconf import ServiceInfo, Zeroconf

# Set up the zeroconf instance
zeroconf = Zeroconf()

# Define the service name and type
service_name = "my-chat-app"
service_type = "_http._tcp.local."

# Define the IP address and port where the chat app is running
ip_address = "192.168.1.100"
port = 8000

# Create a service info object for the chat app
service_info = ServiceInfo(service_type, service_name, socket.inet_aton(ip_address), port, 0, 0, {}, "")

# Register the service with zeroconf
zeroconf.register_service(service_info)

# Run the chat app
run_chat_app()

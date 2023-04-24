from zeroconf import ServiceBrowser, Zeroconf

# Set up the zeroconf instance
zeroconf = Zeroconf()

# Define the service type to browse for
service_type = "_http._tcp.local."

# Create a service browser to discover services
class MyListener(object):
    def add_service(self, zeroconf, service_type, name):
        # Handle the discovered service
        print("Discovered service: ", name)

browser = ServiceBrowser(zeroconf, service_type, MyListener())

# Wait for services to be discovered
while True:
    pass

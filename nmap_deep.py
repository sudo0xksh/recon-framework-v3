import subprocess
import xml.etree.ElementTree as ET
import subprocess

target = None

subprocess.run([
    "nmap",
    "-sV",
    "-oX",
    "nmap_output.xml",
    target
])

tree = ET.parse(("nmap_output.xml"))
root = tree.getroot()


for port in root.iter("port"):
    port_id = port.get("portid")
    protocol = port.get("protocol")

    service = port.get("service")

    name = port.get("name")
    version = port.get("version")

print(f"Port: {port_id}/protocol")
print(f"Service: {name}")
print(f"Version: {version}")
print("=" * 30)



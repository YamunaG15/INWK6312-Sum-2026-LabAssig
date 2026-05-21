import logging
import requests
from requests.auth import HTTPBasicAuth
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
)

# Device credentials and base URL
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'

BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)


def set_interfaces(append_url, interface_name):
    # Construct complete URL
    url = BASE_URL + append_url + interface_name

    # Authentication
    auth = HTTPBasicAuth(USER, PASS)

    # HTTP headers
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }

    # Interface configuration data
    data = {
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet3",
            "description": "Changed through Restconf",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": "true",

            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "10.0.10.3",
                        "netmask": "255.255.255.0"
                    }
                ]
            },

            "ietf-ip:ipv6": {}
        }
    }

    # Send PUT request
    response = requests.put(
        url,
        auth=auth,
        headers=headers,
        data=json.dumps(data)
    )

    # Check response status
    if response.status_code == 204:
        logging.info(
            f"Request was successful on {HOST}, "
            f"Code: {response.status_code}"
        )

        return "success!"

    else:
        logging.error(
            f"Error encountered during request on {HOST}, "
            f"Code: {response.status_code}"
        )

        return response.text


# Call function
print(
    set_interfaces(
        "interfaces/interface/",
        "GigabitEthernet3"
    )
)

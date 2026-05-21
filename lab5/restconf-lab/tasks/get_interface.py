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


def get_interfaces(append_url, interface_name):
    # Construct complete URL
    url = BASE_URL + append_url + interface_name

    # Authentication
    auth = HTTPBasicAuth(USER, PASS)

    # Request headers
    headers = {
        'Accept': 'application/vnd.yang.data+json'
    }

    # Query parameters
    params = {
        'deep': True
    }

    logging.info(f"URL ==> {url}")

    # Send GET request
    response = requests.get(
        url,
        auth=auth,
        headers=headers,
        params=params
    )

    # Check response status
    if response.status_code == 200:
        logging.info(
            f"Request was successful on {HOST}, "
            f"Code: {response.status_code}"
        )

        return json.dumps(
            response.json(),
            sort_keys=True,
            indent=4
        )

    else:
        logging.error(
            f"Error encountered during request on {HOST}, "
            f"Code: {response.status_code}"
        )

        return response.text


# Call function
print(
    get_interfaces(
        "interfaces/interface/",
        "GigabitEthernet1?verbose"
    )
)

import requests
import sys
import json
import pandas as pd
import time

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# use the IP address or hostname of your Cat9300
# HOST = 'sandbox-iosxe-recomm-1.cisco.com'

# # use your user credentials to access the Cat9300
# USER = 'developer'
# PASS = 'lastorangerestoreball8876'
ns ="11.1.1.1"


# create a main() method
# def main(hostname , username ,password , ip , mask , interface):
def main(hostname , username ,password ):
    """Main method that configures the Ip address for a interface via RESTCONF."""

    # url string to issue GET request
    # url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/primary".format(h=hostname)
    # url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/version/".format(h=hostname)
    # foe enable router any protocols
    url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=3/ip/address/".format(h=hostname)
    # payload = "{\"primary\": {\"address\": \"192.168.1.2\", \"mask\": \"255.255.255.0\"}}"
    # payload =f"{{\"primary\": {{\"address\": \"{ip}\", \"mask\": \"{mask}\"}}}}"
    # print(payload)
    # Define the payload to enable OSPF protocol
    # payload = {
    #     "Cisco-IOS-XE-ospf:ospf": {
    #         "id": 1,
    #         "router-id": "1.1.1.1",
    #         "nsr": {},
    #         "Cisco-IOS-XE-ospf:network": [
    #             {
    #                 "ip": "192.168.0.0",
    #                 "mask": "0.0.0.255",
    #                 "area": 0
    #             }
    #         ]
    #     }
    # }
    # payload ={
    #     "Cisco-IOS-XE-rip:rip": {
    #         "network": [
    #             {
    #                 "ip": "192.168.71.0"
    #             }
    #         ]
    #     }
    # }
    payload ={
        "Cisco-IOS-XE-native:address": {
            "primary": {
                "address": f"{ns}",
                "mask": "255.255.255.0"
            }
        }
    }
    payload_json = json.dumps(payload)


    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a PATCH on the specified url
    # response = requests.request("PUT",url, auth=(username, password),
    #                         data=payload, headers=headers, verify=False)
    # response = requests.request("GET",url, auth=(username, password),
    #                          headers=headers, verify=False , timeout=15)

    # for only json file enable ospf or any protocols
    response = requests.request("PUT",url, headers=headers, auth=(username, password), data=payload_json, verify=False)

                            
    # print the json that is returned
    print(response.text)


def get_conf(filename):
    config=[]
    file = pd.read_excel(filename)
    for index,row in file.iterrows():
        device ={
            'hostname':row['hostname'],
            'username':row['username'],
            'password':row['password'],
            # 'ip':row['ip'],
            # 'mask':row['mask'],
            # 'interface':row['interface'],
            
        }
        config.append(device)
    return config
    # print(config)

# print(get_conf("routers-info-1.xlsx")) 


file_path = 'evengroute.xlsx'
configuration = get_conf(file_path)

for data in configuration:
    hostname = data["hostname"]
    username = data["username"]
    passsword = data["password"]
    # ip = data["ip"]
    # mask = data["mask"]
    # interface = data["interface"]

    # main(hostname , username , passsword ,  ip , mask ,interface)
    main(hostname , username , passsword )

# if __name__ == '__main__':
#     sys.exit(main())
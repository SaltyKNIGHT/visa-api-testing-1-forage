import requests
import json
user_id = "5OSWZVOR7HCMK5K2QSYH21xbaHcWv33W0oUY6uXLFJFGmUM-4"
password = "A8hC8l9IOc69T6XByNVZ"
url = "https://sandbox.api.visa.com/cofds-web/v1/datainfo"
body = {"requestMessageId":"6da6b8b024532a2e0eacb1af58581","messageDateTime":"2019-02-35 05:25:12.327",}
header1 = {"pANs":"4072208010000000","group":"STANDARD"}

rr = requests.post(url,
                 verify = ('DigiCertGlobalRootCA.pem'),
								 # verify = False,
								 # verify = ('vdp_root_cert.pem'),
				  			 cert = ('cert.pem','private_key.pem'),
								 headers = header1,
								 auth = (user_id, password),
								 data = body,
								 )
print(rr)
print(rr.json())
# print(rr.content)

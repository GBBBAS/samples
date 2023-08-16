from rtdip_sdk.authentication.azure import DefaultAuth
from rtdip_sdk.connectors import DatabricksSQLConnection
from rtdip_sdk.queries import circular_standard_deviation

auth = DefaultAuth().authenticate()
token = auth.get_token("{token}").token
connection = DatabricksSQLConnection("{server_hostname}", "{http_path}", token)

parameters = {
    "business_unit": "{business_unit}",
    "region": "{region}", 
    "asset": "{asset_name}", 
    "data_security_level": "{security_level}", 
    "data_type": "float",
    "tag_names": ["{tag_name_1}", "{tag_name_2}"],
    "start_date": "2023-01-01",
    "end_date": "2023-01-31",
    "time_interval_rate": "15",
    "time_interval_unit": "minute",
    "lower_bound": 0,
    "upper_bound": 360,
    "include_bad_data": True,
}
x = circular_standard_deviation.get(connection, parameters)
print(x)

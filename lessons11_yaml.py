#pip install pyyaml

import yaml

#write

# l_connections = [
#     {
#         "user_name": "etl_user",
#         "password": "123",
#         "host": "192.168.1.1",
#         "name": "Igor"
#     },
#     {
#         "user_name": "test_user",
#         "password": "456"
#     }
# ]
#
# with open(r'store_file.yaml', 'w') as file:
#     documents = yaml.dump(l_connections, file)

##########################################################
#reading

with open(r'store_file.yaml') as file:
    connection = yaml.load(file, Loader=yaml.FullLoader)
    print(connection)
    print(type(connection))
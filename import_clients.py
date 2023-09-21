import re

with open('TG_client_groups.rtf', 'r') as file:
    text = file.read()

client_chat_ids = []
input_list = text.split('\\\n')
for input in input_list:
    client_chat_ids.append(re.sub('\D', '', input))

# print(client_chat_ids)
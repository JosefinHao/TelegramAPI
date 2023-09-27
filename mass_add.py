from telethon import TelegramClient, events, sync, utils
from telethon.tl.functions.messages import AddChatUserRequest, CreateChatRequest
import re


client_chat_ids = []
test_group_chat_ids = []


def import_clients():
    with open("TG_client_groups.rtf", "r") as file:
        text = file.read()
    input_list = text.split("\\\n")
    for input in input_list:
        client_chat_ids.append(int(re.sub("\D", "", input)))
    # print(client_chat_ids)


def get_test_group_chat_ids():
    with open("test_groups_chat_ids.txt", "r") as file:
        text = file.read()
    input_list = text.split("\n")
    for input in input_list:
        if len(input) > 1:
            test_group_chat_ids.append(int(input))
    # print(test_group_chat_ids)


get_test_group_chat_ids()


users_to_add = [
    # 464929491,  # Max's TG ID
    # 1299245979,  # Michael's TG ID
    # 5498034564,  # Nabeel's TG ID
    # 732931592,  # Daisy's TG ID
    # 5501765660  # Angelly's TG ID
]

api_id = 28660903
api_hash = "2e6d3d05025f5bd74427d140a45bbc47"

client = TelegramClient("session_name", api_id, api_hash)
client.start()

# create test groups and add users to them all at once, target 600+ groups
# for n in range(50):
#     lincoln_id = 1608449357
#     group_number = 51 + n
#     group_name = "TestGroup" + str(group_number)

#     # create a test group and get chat_id
#     new_chat = CreateChatRequest([lincoln_id], group_name)
#     info = client(new_chat)
#     info_dict = info.to_dict()
#     chat_id = info_dict["updates"][1]["participants"]["chat_id"]
#     test_group_chat_ids.append(chat_id)
#     # save chat_ids into a txt file for later use
#     with open("test_groups_chat_ids.txt", "a") as f:
#         f.write(str(chat_id))
#         f.write("\n")

#     # add users to the newly created test group
#     for user_to_add in users_to_add:
#         try:
#             client(
#                 AddChatUserRequest(
#                     chat_id,
#                     user_to_add,
#                     fwd_limit=100,  # Allow the user to see the 100 last messages
#                 )
#             )
#         except Exception as error:
#             print(error)

# # save chat_ids into a txt file for later use
# with open("test_chat_groups.txt", "a", encoding="UTF8") as f:
#     f.write(",".join([str(i) for i in chat_groups]))


# # add one user to all test groups
for user_to_add in users_to_add:
    for chat_id in test_group_chat_ids:
        try:
            client(
                AddChatUserRequest(
                    chat_id,
                    user_to_add,
                    fwd_limit=100,  # Allow the user to see the 100 last messages
                )
            )
        except Exception as error:
            print(error)

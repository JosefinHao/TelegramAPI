from telethon import TelegramClient, events, sync, utils
from telethon.tl.functions.messages import AddChatUserRequest, CreateChatRequest
import telethon.tl.functions
import re


client_chat_ids = []


def import_clients():
    with open("TG_client_groups.rtf", "r") as file:
        text = file.read()
    input_list = text.split("\\\n")
    for input in input_list:
        client_chat_ids.append(re.sub("\D", "", input))
    # print(client_chat_ids)


# TG groups to test:
chat_groups = [
    4023732695,
    4044874801,
    4016892206,
    4035140007,
    4005957837,
    4077575650,
    4062238263,
    4061582253,
    4071929846,
    4062455097,
    4021989027,  # TestGroup11
    4066852879,
    4093702766,
    4026493485,
    4018270475,
    4015709536,
    4080579443,
    4016827893,
    4011107989,
    4045586431,
    4052158893,  # TestGroup21
    4006339985,
    4068448859,
    4079528775,
    4014051019,
    4069259109,
    4089323929,
    4076145680,
    4038409950,
    4056712866,
    4045512594,  # TestGroup31
    4076187874,
    4021369548,
    4072186898,
    4062593072,
    4000704092,
    4047866905,
    4064546411,
    4052360104,
    4050278583,
    4039499664,  # TestGroup41
    4076996673,
    4020042822,
    4043304955,
    4071065766,
    4055463727,
    4031084976,
    4022473918,
    4058451998,
    4075810296,
]

users_to_add = [
    464929491,  # Max's TG ID
    1299245979,  # Michael's TG ID
    5498034564,  # Nabeel's TG ID
    732931592,  # Daisy's TG ID
]

api_id = 28660903
api_hash = "2e6d3d05025f5bd74427d140a45bbc47"

client = TelegramClient("session_name", api_id, api_hash)
client.start()

# create test groups and add users to them all at once, target 600+ groups
for n in range(30):
    lincoln_id = 1608449357
    group_number = 55 + n
    group_name = "TestGroup" + str(group_number)

    # create a test group and get chat_id
    new_chat = CreateChatRequest(
            [lincoln_id],
            group_name
    )
    info = client(new_chat)
    info_dict = info.to_dict()
    chat_id = info_dict["updates"][1]["participants"]["chat_id"]

    # add users to the newly created test group
    for user_to_add in users_to_add:
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

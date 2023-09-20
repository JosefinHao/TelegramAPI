from telethon import TelegramClient, events, sync, utils
from telethon.tl.functions.messages import AddChatUserRequest
import td
 
api_id = 28660903
api_hash = '2e6d3d05025f5bd74427d140a45bbc47'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

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
    4021989027,
    4066852879,
    4093702766,
    4026493485,
    4018270475,
    4015709536,
    4080579443,
    4016827893,
    4011107989,
    4045586431
]
# chat_id = 4023732695
# user_to_add = 464929491  # Max's TG ID 464929491
# user_to_add = 1299245979 # Michael's TG ID
user_to_add = 5498034564 # Nabeel's TG ID

# print(client.get_me().stringify())

# client.download_profile_photo('me')
# messages = client.get_messages('username')
# messages[0].download_media()

# @client.on(events.NewMessage(pattern='(?i)hi|hello'))
# async def handler(event):
#     await event.respond('Hey!')
#     await client(AddChatUserRequest(
#         chat_id,
#         user_to_add,
#         fwd_limit=10  # Allow the user to see the 10 last messages
#     ))


for chat_id in chat_groups:
    try:
        client(AddChatUserRequest(
                chat_id,
                user_to_add,
                fwd_limit=100  # Allow the user to see the 100 last messages
            ))        
    except Exception as error:
        print(error) 




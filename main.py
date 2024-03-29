import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from convert_tdata import convert_tdata

API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
API_ID = 17463049

sessions = []

for tdata in os.listdir("tdatas"):
    try:
        auth_key = convert_tdata(f"tdatas/{tdata}")[0]
    except Exception as err:
        print(err)
    else:
        print(f"{tdata} успешно конвертировано")

    sessions.append(StringSession(auth_key))


for session in sessions:
    client = TelegramClient(
        session,
        api_hash=API_HASH,
        api_id=API_ID
    )

    try:
        client.connect()
        me = client.get_me()
    except Exception as err:
        print(err)
    else:
        phone = client.get_me().phone
        auth_key = client.session.save()
        with open(f"sessions/{phone}.session", "w") as file:
            file.write(auth_key)

        print(f"{me.phone} сохранён")




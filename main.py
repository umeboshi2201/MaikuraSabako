import discord
import sys
import tokendata
import datetime
import os
import subroutines
from character import MaikuraSan

client = discord.Client()
character = MaikuraSan()

@client.event
async def on_ready():
    print('Discordにメッセージを送ります。')

    channel = client.get_channel(tokendata.token["channel_id"])

    if(len(sys.argv) >= 2):
        if(sys.argv[1] == 'start'):
            if(len(sys.argv) >= 3):
                start_message = character.getStartMessage(sys.argv[2])
                await client.send_message(channel, start_message)
                print(start_message)

        elif(sys.argv[1] == 'end'): 
            end_message = character.getEndMessage()

            await client.send_message(channel, end_message)

            if(len(sys.argv) >= 3):

                log_dir_name = 'Logs'
                new_filename = 'ServerLog_' + datetime.datetime.today().strftime("%Y%m%d%H%M%S") + '.txt'
                send_filename = 'Log_' + datetime.datetime.today().strftime("%Y%m%d%H%M%S") + '.txt'
                path_new_filename = os.path.join(log_dir_name, new_filename)
                path_send_filename = os.path.join(log_dir_name, send_filename)
                os.makedirs(log_dir_name, exist_ok=True)

                with open(path_new_filename, 'w') as f:
                    f.write(sys.argv[2])

                with open(path_new_filename, 'r', encoding='utf-8') as rf, open(path_send_filename, 'w') as wf:
                    server_log_messages = rf.readlines()
                    formatted_server_logs = subroutines.formatLogMessage(server_log_messages)
                    for item in formatted_server_logs:
                        wf.write(item)

                log_message = character.getLogMessage(sys.argv[2]);

                await client.send_file(channel, path_new_filename, content=log_message)


            print(end_message)
        else:
            print('error!')

    else:
        print('error!')
    await client.logout()

if __name__ == "__main__":
    client.run(tokendata.token["token_code"])
    print('メッセージ送信完了')

import discord
import sys
import tokendata
import datetime
import os
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

            if(len(sys.argv) >= 3):
                log_dir_name = 'Logs'
                new_filename = 'ServerLog_' + datetime.datetime.today().strftime("%Y%m%d%H%M%S") + '.txt'
                latest_filename = 'LatestLog.txt'
                path_new_filename = os.path.join(log_dir_name, new_filename)
                path_latest_filename = os.path.join(log_dir_name, latest_filename)
                os.makedirs(log_dir_name, exist_ok=True)
                with open(path_new_filename, 'w') as f, open(path_latest_filename, 'w') as lf:
                    f.write(sys.argv[2])
                    lf.write(sys.argv[2])
                end_message = end_message + '\n' + character.getLogMessage(sys.argv[2]);

            await client.send_message(channel, end_message)
            await client.send_file(channel, path_new_filename)

            print(end_message)
        else:
            print('error!')

    else:
        print('error!')
    await client.logout()

if __name__ == "__main__":
    client.run(tokendata.token["token_code"])
    print('メッセージ送信完了')

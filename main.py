import discord
import sys
import tokendata
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
            print(end_message)
        else:
            print('error!')

    else:
        print('error!')
    await client.logout()

if __name__ == "__main__":
    client.run(tokendata.token["token_code"])
    print('メッセージ送信完了')

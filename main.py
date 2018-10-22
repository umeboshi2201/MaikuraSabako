import discord
import sys
from tokendata import token
from character import MaikuraSan

client = discord.Client()
character = MaikuraSan()

@client.event
async def on_ready():
    print('Discordにメッセージを送ります。')

    channel = client.get_channel(token["channel_id"])
    #await client.send_message(channel, 'このチャンネル内での発言は全てテストです')

    if(len(sys.argv) >= 2):
        if(sys.argv[1] == 'start'):
            if(len(sys.argv) >= 3):
                start_message = character.getStartMessage(sys.argv[2])
                #await client.send_message(channel, start_message)
                print(start_message)
        elif(sys.argv[1] == 'end'): 
            end_message = character.getEndMessage()
            #await client.send_message(channel, 'マインクラフトサーバーを終了します')
            print(end_message)
        else:
            print('error!')

    else:
        print('error!')
    await client.logout()

if __name__ == "__main__":
    client.run(token["token_code"])
    print('メッセージ送信完了')

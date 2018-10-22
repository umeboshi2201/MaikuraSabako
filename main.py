import discord
import sys
from tokendata import token

client = discord.Client()

@client.event
async def on_ready():
    print('Discordにメッセージを送ります。')

    channel = client.get_channel(token["channel_id"])
    #await client.send_message(channel, 'このチャンネル内での発言は全てテストです')

    if(len(sys.argv) >= 2):
        if(sys.argv[1] == 'start'):
            #await client.send_message(channel, 'マインクラフトサーバーを起動します')
            if(len(sys.argv) >= 3):
                #await client.send_message(channel, 'IP : ' + sys.argv[2])
                pass
        elif(sys.argv[1] == 'end'): 
            #await client.send_message(channel, 'マインクラフトサーバーを終了します')
            pass
        else:
            print('error!')

    await client.logout()

if __name__ == "__main__":
    client.run(token["token_code"])
    print('メッセージ送信完了')

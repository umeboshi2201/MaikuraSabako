import random

class MaikuraSan:
    def __init__(self):
        pass
    def getStartMessage(self, ip_message):
        messages = ["サーバー起動するわね\nIPアドレスは " + ip_message + " よ"]
        messages.append("サーバー動かすわよ\nIPアドレスは " + ip_message + " ね")
        return messages[random.randrange(len(messages))]
    def getEndMessage(self):
        messages = ["サーバーを終了するわ"]
        messages.append("サーバー止めるわね\n面倒だから入ってこないでよ？")
        return messages[random.randrange(len(messages))]
    def getLogMessage(self, all_log_message):
        messages = ["ログはこんな感じね"]
        return messages[random.randrange(len(messages))]

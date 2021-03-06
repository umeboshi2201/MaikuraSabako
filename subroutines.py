import re
import usernames

def formatLogMessage(log_messages):
    re_pattern_str = r'^\[([^]]*)\] \[Server thread/INFO\]: (<?(' 
    name_make_count = 1

    for name in usernames.users:
        if len(usernames.users) != name_make_count:
            re_pattern_str = re_pattern_str + name + r'|'
        else:
            re_pattern_str = re_pattern_str + name
        name_make_count = name_make_count + 1

    re_pattern_str = re_pattern_str + r')>?[^[]|Starting minecraft server version|Stopping the)'
    match_pattern = re.compile(re_pattern_str)

    result_logs = []
    for message in log_messages:
        match_result = match_pattern.match(message)
        if match_result == None:
            continue
        else:
            result_logs.append(message)

    return result_logs

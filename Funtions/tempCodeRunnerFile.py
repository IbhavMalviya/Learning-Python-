messages=['Hello A','Hello B','Hello C']

def send_message(messages):
    sent_messages=[]
    for message in messages:
        print(message)
        sent_messages.append(message)
        print(sent_messages)
        print(messages)
send_message(messages)
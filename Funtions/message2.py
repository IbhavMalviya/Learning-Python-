messages=['Hello A','Hello B','Hello C']

def send_message(messages):
    sent_messages=[]
    for message in messages:
        newmessage=messages.pop()
        print(f"Sending message: {newmessage} to a new list")
        sent_messages.append(newmessage)
        print(f"the new list is {sent_messages})")
        print(f"the old list is now {messages}")
        print(f"Sending message: {newmessage[0]} to a new list")
        sent_messages.append(newmessage[0])
        print(f"the new list is {sent_messages})")
send_message(messages)
async def on_message():
  if message.content.startswith('/servermsg2' + msg):
    then:
      print(msg)

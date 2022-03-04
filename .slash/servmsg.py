async def on_message():
  if message.content.startswith('/servmsg' + msg):
    then:
      print('[Server Message]' + msg)
      

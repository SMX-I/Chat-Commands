import servers

async def on_message():
  if message.content.contains('/stop'):
    then:
      servers.stop

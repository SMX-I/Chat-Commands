import servers
import membersfetch from servers

async def on_message():
  if message.content.startswith('/kick' + user + reason):
    then:
      membersfetch.kick('{user} with {reason}')
      print(user + 'was kicked.')

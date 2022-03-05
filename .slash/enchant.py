import servers 
import itemfetch from servers

async def on_message():
  if message.content.startswith('/enchant'):
    then:
      itemfetch.enchant('ih#0000')
      then:
        print('Item successfully enchanted')
        then:
          end;
          
          

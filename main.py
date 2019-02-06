#Simonsen Server Discord Bot
#created using https://www.codementor.io/garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz
#event handler
#https://medium.com/bad-programming/making-a-cool-discord-bot-in-python-3-e6773add3c48
import discord, os, random, sys
from keep_alive import keep_alive

client = discord.Client()
commands = []
status = True
###build commands
def list_commands(message, client, args):
  '''displays additional information on how to use a command'''
  count = 1
  coms = '**Commands List**\n'
  for command in commands:
    coms += '{}) {} : {}\n'.format(count, command['trigger'], command['description'])
    count += 1
  return coms
commands.append(
  {'trigger':'!help',
  'function':list_commands,
  'args_num':0,
  'args_name': [''],
  'description':'Displays a list of commands'})

def help_command(message, client, args):
  '''displays all commands'''
  #get rid of extra user stuff
  if len(args)>1:
    args = args[0]
  else:
    #add a '!' to the beginning of the message
   if args[0]!= '!':
    args = '!'+args[0]
  #determine if message is in commands
  cmd_triggers=[]
  for i in commands:
    cmd_triggers.append(i['trigger'])
  if args not in cmd_triggers:
    return "That's not a SimoBot command"
  else:
    i = cmd_triggers.index(args)
    rep = '**{}**\n'.format(args)
    rep += '# of Arguments: {}\n'.format(commands[i]['args_num'])
    rep += 'Name of Arguments: {}\n'.format(commands[i]['args_name'])
    rep += 'Description: {}'.format(commands[i]['description'])
    return rep
commands.append(
  {'trigger':'!command',
  'function':help_command,
  'args_num':1,
  'args_name':['name of a command'],
  'description':'Displays information on how to use a command'})

def ping(message, client, args):
  '''ping gets a response of pong'''
  return ':ping_pong: pong :ping_pong: <@{}>'.format(message.author.id)
commands.append(
  {'trigger':'!ping',
  'function':ping,
  'args_num':0,
  'args_name':[],
  'description':'Pong the user'})

def hello_function(message, client, args):
  '''greets the user with a random message'''
  greetings =(
    "May the odds be ever in your favor","For Aiur!",
    "Live long and prosper","May the Force be with you",
    "En taro Adun","Peek-a-boo!",
    "My name's Ralph, and I'm a bad guy.","I come in peace",
    "Put that cookie down!","Sup, homeslice?","I'm batman",
    "Hello, my name is Inigo Montoya",
    "This call may be recorded for quality assurance",
    "Hello", "Aloha", "Hola", "Que pasa", "Bonjour", "Hallo", "Ciao", "Konnichiwa","What's shakin' bacon",
    "What's up butterup?","Namaste","War never changes",
    "What's the word, hummingbird","Monkeyfeathers",
    "I used to be an adventurer like you, then I took an arrow to the knee","Twinkle-toes")
  return '{} <@{}>'.format(random.choice(greetings),message.author.id)
commands.append(
  {'trigger':'!hello',
  'function':hello_function,
  'args_num':0,
  'args_name': [],
  'description':'Randomly greets the user'})

def reverse(message, client, args):
  '''reverses a message'''
  rev = message.content
  #remove '!reverse ' from the beginning of the message
  rev = rev[9:]
  return '<@{}> {}'.format(message.author.id, rev[::-1])
commands.append(
  {'trigger':'!reverse',
  'function':reverse,
  'args_num':1,
  'args_name': ['message'],
  'description':"reverses the user's message"})

async def join_team(message, client, args):
  '''gives the user a team role'''
  teams = {
    'blue':"Team Blue",
    'green':"Team Green",
    'red':"Team Red"}
  #check for valid team name
  name = args[0].lower()
  if name not in teams.keys():
    return "That wasn't a team name\n'!command teamMe' to see teams you can join"
  else:
    team = teams[name]
  #check to see if they already have a team
  for i in message.author.roles:
    if 'team' in i.name.lower():
      return "You're already on "+i+". You can only be on one team at a time."
      break
  #if they don't - join team
  role = discord.utils.get(message.server.roles, name=team)
  await client.add_roles(message.author, role)
  #return success message
  return"<@{}> has joined {}".format(message.author.id,teams[name])
commands.append(
  {'trigger':'!teamMe',
  'function':join_team,
  'args_num':1,
  'args_name':['team color'],
  'description':'Lets you join a team from "red", "green", or "blue". Need to be on a team to post in the meme channel.'})

async def leave_team(message, client, args):
  '''removes the user from a team role'''
  #check to see if user in team
  team = None
  for i in message.author.roles:
    if 'team' in i.name.lower():
      team = i
  if team:
    #leave team
    await client.remove_roles(message.author, team)
    #?reset score?
    #display success message
    return "<@{}> has left {}".format(message.author.id,team.name)
  else:
    return "You're currently not on a team - check your roles!"
commands.append(
  {'trigger':'!leaveTeam',
  'function':leave_team,
  'args_num':0,
  'args_name':[],
  'description':'Removes the user from their team'})

def display_teams(message, client, args):
  '''displays information on teams'''
  #add more information about each team (cumlative score or top scores in team)
  #count the number of members per role
  cyber = discord.utils.get(message.server.roles, name='CyberPatriot')
  cp = 0
  red = discord.utils.get(message.server.roles, name='Team Red')
  rc = 0
  green = discord.utils.get(message.server.roles, name='Team Green')
  gc = 0
  blue = discord.utils.get(message.server.roles, name='Team Blue')
  bc = 0
  count = 0
  for member in message.server.members:
    count += 1
    #red, green, blue are exclusive
    if red in member.roles:
      rc += 1
    elif green in member.roles:
      gc += 1
    elif blue in member.roles:
      bc += 1
    #not exclusive
    if cyber in member.roles:
      cp += 1
  #string to return
  rep = ''
  rep += "**Member Count**\n"
  rep += "Total Members: {}\n".format(count)
  rep += "CyberPatriots: {}\n".format(cp)
  rep += "Team Red: {}\n".format(rc)
  rep += "Team Green: {}\n".format(gc)
  rep += "Team Blue: {}\n".format(bc)
  rep += "Team Red, Team Green, and Team Blue are the teams you can join using the bot."
  return rep
commands.append(
  {'trigger':'!teams',
  'function':display_teams,
  'args_num':0,
  'args_name':[],
  'description':'Displays a list of teams'})

def rps(message, client, args):
  args = args[0]
  rep = '<@{}> choice: {}\n'.format(message.author.id,args)
  a = ('rock','paper','scissors')
  if args not in a:
    return "That's not a valid choice"
  c = random.choice(a)
  rep += 'Simobot choice: {}\n'.format(c)
  if c == 'rock':
    if args == 'rock':
      rep += ':necktie: Tie'
    elif args == 'paper':
      rep += 'You win'
    elif args == 'scissors':
      rep += 'You lose'
    else:
      print(c, args)
      return 'something went wrong in rock branch'
  elif c == 'paper':
    if args == 'rock':
      rep += 'You lose'
    elif args == 'paper':
      rep += ':necktie: Tie'
    elif args == 'scissors':
      rep += 'You win'
    else:
      print(c, args)
      return 'something went wrong in paper branch'
  elif c == 'scissors':
    if args == 'rock':
      rep += 'You win'
    elif args == 'paper':
      rep += 'You lose'
    elif args == 'scissors':
      rep += ':necktie: Tie'
    else:
      print(c, args)
      return 'something went wrong in paper branch'
  else:
    print(c, args)
    return 'something went wrong with simobot choice branch'
  return rep
commands.append(
  {'trigger':'!rps',
  'function':rps,
  'args_num':1,
  'args_name':['rock, paper, or scissors'],
  'description':'Play Rock Paper Scisscors with the bot'})

def dice(message, client, args):
  n,d = args[0].split('d')
  rep = '<@{}>\nRolled {} d{}\n'.format(message.author.id,n, d)
  total = 0
  for i in range(int(n)):
    x = random.randint(1,int(d))
    rep += '{}, '.format(x)
    total += x
  rep = rep[:-2]
  rep += '\nTotal: {}'.format(total)
  return rep
commands.append(
  {'trigger':'!roll',
  'function':dice,
  'args_num':1,
  'args_name':["xdy"],
  'description':"Rolls 'x'd'y' where x is the number of dice and y is the number of sides"})


###client events
#message from bot on joining server
@client.event
async def on_ready():
  print('Discord.py Version: {}'.format(discord.__version__))
  print("**{} Online**".format(client.user.name))


#event handler on new message
@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content == "!kill":
      print('bot has been killed')
      await client.send_message(message.channel, "It's dead Jim.")
      sys.exit()
    for command in commands:
      if message.content.startswith(command['trigger']):
        args = message.content.split(' ')
        if args[0]=='!teamMe':
          args.pop(0)
          if len(args) >= command['args_num']:
            rep = await join_team(message, client, args)
            await client.send_message(message.channel, rep)
            break
          else:
            await client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
            break
        elif args[0]=='!leaveTeam':
          args.pop(0)
          if len(args) >= command['args_num']:
            rep = await leave_team(message, client, args)
            await client.send_message(message.channel, rep)
            break
          else:
            await client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
            break
        elif command['args_num'] == 0:
          await client.send_message(message.channel, str(command['function'](message, client, args)))
          break
        else:
          #remove trigger from args
          args = args[1:]
          if len(args) >= command['args_num']:
            await client.send_message(message.channel, str(command['function'](message, client, args)))
            break
          else:
            await client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
            break
      else:
        pass #not a command
  else:
    pass #don't check messages from bot

#keep the server alive after closing repl.it
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

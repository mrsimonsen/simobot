#Simonsen Server Discord Bot
#created using https://www.codementor.io/garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz
from keep_alive import keep_alive
import discord
import os
import random

#add method to make reminders to simonsen channel https://discordbots.org/bot/391890106736443393

#command handler class
#https://medium.com/bad-programming/making-a-cool-discord-bot-in-python-3-e6773add3c48
class CommandHandler:
  #constructor
  def __init__(self, client):
    self.client = client
    self.commands = []

  def command_handler(self, message):
    #loop through all the commands
    for command in self.commands:
      #if the message starts with the command trigger
      if message.content.startswith(command['trigger']):
        args = message.content.split(' ')
        if args[0] == command['trigger']:
          args.pop(0)
          #return the results of the function
          if command['args_num']==0 or len(args) >= command['args_num']:
            return self.client.send_message(message.channel,str(command['function'](message, self.client, args)))
          #return an argument error
          else:
            return self.client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
  def add_command(self, command):
    self.commands.append(command)

####create bot objects
#object used to send commands to discord's servers
client = discord.Client()
#object used to handle commands
ch = CommandHandler(client)
#server object, defined on_ready()
server = None

####command support functions
def user_roles(message):
  '''makes a list of all of a message author's roles'''
  r = []
  for i in message.author.roles:
    r.append(i.name)
  print(r)
  return r

async def join(member, role):
  await client.add_roles(member, role)


####command functions
def list_commands(message, client, args):
  try:
    count = 1
    coms = '**Commands List**\n'
    for command in ch.commands:
      coms += '{}.) {} : {}\n'.format(count, command['trigger'], command['description'])
      count += 1
    return coms
  except Exception as e:
    print (e)
ch.add_command(
  {'trigger':'!list',
  'function':list_commands,
  'args_num':0,
  'args_name': [''],
  'description':'Displays a list of commands (this function)'})
##end list_commands

#function to display help message for a command
def help_command(message, client, args):
  try:
    #add a '!' to the beginning of the message
    if args[0][0]!= '!':
      args = '!'+args[0]
    #determine if message is in commands
    cmd_triggers=[]
    for i in ch.commands:
      cmd_triggers.append(i['trigger'])
    if args not in cmd_triggers:
      return "That's not a SimoBot command"
    else:
      i = cmd_triggers.index(args)
      rep = '**{}**\n'.format(args)
      rep += '# of Arguments: {}\n'.format(ch.commands[i]['args_num'])
      rep += 'Name of Arguments: {}\n'.format(ch.commands[i]['args_name'])
      rep += 'Description: {}'.format(ch.commands[i]['description'])
      return rep
  except Exception as e:
    print(e)
ch.add_command(
  {'trigger':'!help',
  'function':help_command,
  'args_num':1,
  'args_name':['name of a command'],
  'description':'Displays information on how to use a command'})
##end help_command

def hello_function(message, client, args):
  greetings=(
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
  try:
    return '{} <@{}>'.format(random.choice(greetings),message.author.id)
  except Exception as e:
    return e
ch.add_command(
  {'trigger':'!hello',
  'function':hello_function,
  'args_num':0,
  'args_name': [],
  'description':'Randomly greets the user'})
##end hello_function

def score(message, client, args):
  try:
    #determine if message is a member of the server
      #error message
    #determine if the member is not themselves
      #can't add points to yourself
    #+1 to score
    return "TODO: score function"
  except Exception as e:
    print(e)
ch.add_command(
  {'trigger':'!thank',
  'function':score,
  'args_num':1,
  'args_name':['name of another user'],
  'description':'Grants points to another user for being helpful'})
##end score

def my_score(message, client, args):
  try:
    #display the value of your socre
    return"TODO: finish my_score"
  except Exception as e:
    print(e)
ch.add_command(
  {'trigger':'!myScore',
  'function':my_score,
  'args_num':0,
  'args_name':[],
  'description':'Displays your current score'})
##end my_score

def your_score(message, client, args):
  try:
    #displays the score of another
    return "TODO: finish your_score"
  except Exception as e:
    print(e)
ch.add_command(
  {'trigger':'!yourScore',
  'function':your_score,
  'args_num':1,
  'args_name':['user name'],
  'description':'Checks the score of another user'})
##end your_score

def scoreboard(message, client, args):
  try:
    #display top leaders and top team
    return"TODO: finish scoreboard"
  except Exception as e:
    print(e)
ch.add_command({'trigger':'!scoreboard',
  'function':scoreboard,
  'args_num':0,
  'args_name':[],
  'description':'Displays the highest scores'})
##end scoreboard

def join_team(message, client, args):
  try:
    teams = {
      'blue':"Team Blue",
      'green':"Team Green",
      'red':"Team Red"
    }
    try:
      name = args[0].lower()
      team = teams[name]
    except KeyError as e:
      print(e)
      return "That wasn't a team name\n'!help teamMe' to see teams you can join"
    #check to see if they already have a team
    u_roles = user_roles(message)
    for i in u_roles:
      if 'team' in i.lower():
        return "You're already in a team. You need to leave that team before joining another team."
      if 'CyberPatriot' in i:
        return "CyberPatriot is the ultimate team role"
    #if they don't - join team
    role = discord.utils.get(server.roles, name=team)
    join(message.author, role)
    #return success message
    u_roles = user_roles(message)
    for i in u_roles:
      if 'team' in i.lower():
        return"Successfully joined {}".format(teams[name])
      else:
        return "error - wasn't able to add you to {}.".format(teams[name])
  except Exception as e:
    print(e)
ch.add_command(
  {'trigger':'!teamMe',
  'function':join_team,
  'args_num':1,
  'args_name':['team color'],
  'description':'Lets you join a team from "red", "green", or "blue"'})
##end join_team

def leave_team(message, client, args):
  try:
    #check to see if the role is a team
    #if not a team, display error (can't leave non-team)
    #make a list of the users current roles
    #check to see if user in team
    #if not - display error message
    #leave team
    #?reset score?
    #display success message
    return"TODO: finish leave_team"
  except Exception as e:
    print(e)
ch.add_command(
  {'trigger':'!leaveTeam',
  'function':leave_team,
  'args_num':1,
  'args_name':['team name or color'],
  'description':'Removes the user from the team'})
##end leave_team

def display_teams(message, client, args):
  try:
    return "Team Red, Team Green, Team Blue\nCyberpatriots are the ultimate team"
    #add more information about each team (# of members for example, score)
  except Exception as e:
    print(e)
ch.add_command(
  {'trigger':'!teams',
  'function':display_teams,
  'args_num':0,
  'args_name':[],
  'description':'Displays a list of teams'})
##end display_teams
###end commands

#message from bot on joining server
@client.event
async def on_ready():
  print('Discord.py Version: {}'.format(discord.__version__))
  print("**{} Online**".format(client.user.name))
  global server
  for i in client.servers:
    server = i


#event handler on new message
@client.event
async def on_message(message):
  if message.author != client.user:
    try:
      await ch.command_handler(message)
    except TypeError as e:
      pass #ignore it if it's not a command
    except Exception as e:
      print(e)#display python errors in console






# last 3 lines, always
#keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

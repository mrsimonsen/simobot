
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

###end commands
import discord
from datetime import datetime, timedelta
import random as rand
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

henry_emma= ["https://c.tenor.com/5Ao75xbhgcAAAAAC/anime-motivation.gif", "https://c.tenor.com/Gpg2Fv5w_V8AAAAC/heart-anime.gif", "https://c.tenor.com/_5xIX2rXzvUAAAAd/yuru-camp-anime.gif", "https://tenor.com/view/trina-trina-gif-24497452", "https://c.tenor.com/FrroZHYurBAAAAAC/kincoven-link.gif", "https://c.tenor.com/hZtJDJOdDoEAAAAd/destiny-destiny2.gif","https://c.tenor.com/-sG02qfQxsEAAAAd/destiny2-shmoovin.gif" "https://tenor.com/view/take-a-rest-steven-steven-universe-good-night-gotta-go-gif-16698355", "https://tenor.com/view/if-you-aer-sad-monday-motivation-bananas-jokes-dont-be-sad-gif-12659942https://tenor.com/view/spongebob-squarepants-patrick-star-im-rooting-for-you-cheer-cheering-gif-5104276", "https://c.tenor.com/Ts1AmJElsKEAAAAM/spongebob-squarepants-chest.gif", "","https://tenor.com/view/baby-yoda-may-the-force-be-with-you-star-wars-mandalorian-gif-17698540",'https://tenor.com/view/thumbs-up-good-great-excellent-like-gif-15425524', "https://tenor.com/view/applause-kyle-broflovski-stan-marsh-eric-cartman-kenny-mccormick-gif-24731767", "https://tenor.com/view/dog-husky-dog-door-hi-gif-17284157", "https://c.tenor.com/5XI6izjb4jAAAAAM/loof-and-timmy-loof.gif"]

jane = ["You're almost there!!", "Just a little further! ", "We're rooting for you!!", "Almost there babe, mom's watching you!!!!!!", "You got this!", "Just a bit more work you can do it.","Don't stress! You got this!", "Remember to take a break once in a while!", "I believe in you! And unicorns. But mostly you!", "You are doing awesome!", "Good luck today!", "Don't stress"]

#Variables
tasks = []
task_dates = []
task_times = []
task_completes = []
task_finished_completes = []
task_finish_status = []
Task_Who = []
t = "Checklist"
d = "Stuff to get done!"

#Ready Message
@bot.event
async def on_ready():
  print('We have logged in as {bot.user}')

# # # # # INFO COMMANDS # # # # #

#Hello Command
@bot.command(pass_context=True)
async def hello(ctx):
  await ctx.message.channel.send('**Hello!**')

#Encuragment Command 
@bot.command(pass_context=True)
async def encourage(ctx):
  message = rand.randint(1,2)
  if message == 1:
    await ctx.message.channel.send(rand.choice(henry_emma))
  else:
    await ctx.message.channel.send(rand.choice(jane))

#Info Command
@bot.command(pass_context=True)
async def info(ctx):
  await ctx.message.channel.send("Greetings, My name is *Mayu* created in 2/5/22 made entirely within 24 hours as part of the GunnHacks 8.0 hackathon, built by students for students. I identify as the they/them gender pronoun and I'm gender fluid.")
@bot.command(pass_context=True)
async def Gesundheit(ctx):
  await ctx.message.channel.send("God Mode Activated.")
@bot.command(pass_contex=True)
async def upupdowndownleftrightleftrightba(ctx):
  await ctx.message.channel.send("Cheat Code Activated")
@bot.command(pass_context=True)
async def no_wifi(ctx):
  await ctx.message.channel.send(file=discord.File("dino.gif"))
@bot.command(pass_contex=True)
async def ihatepurple(ctx):
  await ctx.message.channel.send(file=discord.File("purple.mp4"))
@bot.command(pass_contex=True)
async def ihatecats(ctx):
  await ctx.message.channel.send(file=discord.File("Cat.mp4"))
@bot.command(pass_contex=True)
async def matt(ctx):
  await ctx.message.channel.send(file=discord.File("matt.png"))  

#Dev Tools
@bot.command(pass_context=True)
async def imadev(ctx):
  embedVar= discord.Embed(title="All secrets avaliable", description="Here are the easter eggs.",color=0x00ff00)
  embedVar.add_field(name="Gesundheit", value="Game Reference",inline=False)
  embedVar.add_field(name="upupdowndownleftrightleftrightba", value="Game Reference", inline=False)
  embedVar.add_field(name="no_wifi", value= "Dino confused", inline=False)
  embedVar.add_field(name="ihatepurple", value= "Oh you hate purple?", inline=False)
  embedVar.add_field(name="ihatecats", value= "Attack", inline=False)
  
  await ctx.message.channel.send(embed=embedVar)

#Commands List
@bot.command(pass_context=True)
async def cmds(ctx):
  embedVar= discord.Embed(title="List of Commands", description="These are list of commands that I run on. Remember that all commands start with a >.",color=0x00ff00)
  embedVar.add_field(name=">hello", value="Need a hi back?", inline=False)
  embedVar.add_field(name=">info", value= "Basic information about me", inline=False)
  embedVar.add_field(name=">encourage", value="Need some support?", inline=False)
  embedVar.add_field(name=">list", value= "Shows current checklist of tasks", inline=False)
  embedVar.add_field(name=">listname [name]", value="Changes the list name", inline=False)
  embedVar.add_field(name=">listdesc [description]", value="Changes the description of the checklist", inline=False)
  embedVar.add_field(name=">task ", value= "Need a new list? Create one using this command. It will then ask you for more information", inline=False)
  embedVar.add_field(name=">finish [task]", value= "Add a completion interval to a task", inline=False)
  embedVar.add_field(name=">restart [task]", value= "Restart a task's completion rate to 0%", inline=False)
  embedVar.add_field(name=">delete [task]", value= "Delete a task", inline=False)
  embedVar.add_field(name="BTW there are some secrets hidden for you to find", value="No im not gonna tell them to you, have fun finding them.", inline=False)
  await ctx.message.channel.send(embed=embedVar)

# # # # # CHECKLIST/TASK COMMANDS # # # # #

#Checkist Command
@bot.command(pass_context=True)
async def list(ctx):
  embedVar = discord.Embed(title=t, description=d, color=0x00ff00)

  for i in range(len(tasks)):
      if (int(task_finished_completes[i]) / int(task_completes[i]) >= 1):
        embedVar.add_field(name=str(i+1) + ". " + str(tasks[i]) + " (Deadline: " + str(task_dates[i]) + ") :white_check_mark:", value="Finish Time: " + str(task_times[i]) + "\nTimes Finished: " + str(task_finished_completes[i]) + "/" + str(task_completes[i]), inline=False)
      else:
        embedVar.add_field(name=str(i+1) + ". " + str(tasks[i]) + " (Deadline: " + str(task_dates[i]) + ") :x:", value="Finish Time: " + str(task_times[i]) + "\nTimes Finished: " + str(task_finished_completes[i]) + "/" + str(task_completes[i]), inline=False)

  if (len(tasks) == 0):
    embedVar.add_field(name="Wow no tasks?", value="Lucky...", inline=False)
          
  await ctx.message.channel.send(embed=embedVar)

#Task Command
@bot.command(pass_context=True)
async def task(ctx):
  
  author = ctx.message.author.name
  await ctx.message.channel.send("What is your task?")

  def task_name(m):
    global message 
    tasks.append(str(m.content))
    return m.author.name == author

  await bot.wait_for('message', check=task_name)
  await ctx.message.channel.send('Hello ' + author + ', your task is "'+ tasks[len(tasks)-1] + '".')
  await ctx.message.channel.send("What date is this due? ")

  def task_duedate(m): 
    task_dates.append(str(m.content))
    return m.author.name == author

  await bot.wait_for('message', check=task_duedate)
  await ctx.message.channel.send('Your task is due '+ task_dates[len(task_dates)-1] + '.')
  await ctx.message.channel.send("What time is this due? ")

  def task_time(m): 
    task_times.append(str(m.content))
    return m.author.name == author

  await bot.wait_for('message', check=task_time)
  await ctx.message.channel.send('Your task is due at '+ task_times[len(task_times)-1] + '.')
  await ctx.message.channel.send("How many times do you need to finish this task?")

  def task_user(m): 
    task_completes.append(str(m.content))
    task_finished_completes.append(0)
    task_finish_status.append(False)
    return m.author.name == author

  await bot.wait_for('message', check=task_user)

  await ctx.message.channel.send('The task needs to be completed '+ task_completes[len(task_completes)-1] + ' times!')
  await ctx.message.channel.send("The task has been set! Use >list to see your checklist!")

#Finish Task Command
@bot.command()
async def finish(ctx,*, arg):
  global task_completes, tasks, task_finished_completes, task_finish_status
  tasker=False

  for i in range(len(tasks)):
    if arg == tasks[i]:
      task_finished_completes[i] += 1
      await ctx.message.channel.send(str(ctx.author.mention) + " has finished a task! Yay! :partying_face:")
      tasker=True

    if (((int(task_finished_completes[i])/int(task_completes[i])) >= 1) and (task_finish_status[i]==False)):
      await ctx.message.channel.send("WOW! Task " + str(tasks[i]) + " has been completed! Great work @everyone! :star_struck: ")
      task_finish_status[i] = True  

  if tasker==False:
    await ctx.message.channel.send("This task doesn't exist!! :exploding_head:")  

#Restart Task Command - Needs to be finished
@bot.command()
async def restart(ctx, arg):
  restarter=False
  for i in range(len(tasks)):
    if arg == tasks[i]:
      task_finished_completes[i] = 0
      await ctx.message.channel.send(str(ctx.author.mention) + " has restarted a task! Don't worry, you got this! :thumbsup:")
      restarter=True

  if restarter==False:
    await ctx.message.channel.send("That didn't work! Did you put in the wrong task? :thinking:")

#Delete Task Command
@bot.command()
async def delete(ctx, arg):
  deleter=False
  for i in range(len(tasks)):
    if arg == tasks[i]:
      await ctx.message.channel.send("Task " + str(tasks[i]) + " has been deleted. Less work to do, yay! :sweat_smile:")
      tasks.pop(i)
      task_dates.pop(i)
      task_times.pop(i)
      task_finished_completes.pop(i)
      task_completes.pop(i)
      task_finish_status.pop(i)
      deleter=True
  
  if deleter==False:
    await ctx.message.channel.send("The task doesn't exist! Did you spell it wrong? :thinking:")

# #Reminder Message - Incomplete
# while True:
#   current_time = datetime.now()
#   last_hour = datetime.now() - timedelta(hours = 1)
#   last_day = datetime.now() - timedelta(days = 1)
#   last_week = datetime.now() - timedelta(weeks = 1)

  # print(datetime.now)

  # if (datetime.now() == last_hour):
  #   user = client.get_user(688201835877629971)
  #   await ctx.user.send('')
    
# # # # # CUSTOMIZATION # # # # #

#Change List Name Command
@bot.command()
async def listname(ctx,*, arg):
  global t
  t = str(arg)
  await ctx.message.channel.send('Your checklist is now called ' + t)

#Change List Description Command
@bot.command()
async def listdesc(ctx,*, arg):
  global d
  d = str(arg)
  await ctx.message.channel.send('Your description is now: ' + d)

bot.run("OTM5NjM2Nzg0ODEwMjk5NDQy.Yf7u8w.2J0Z0liaZwA8UO_GpAjifChmhvo")

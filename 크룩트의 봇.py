import discord
import random
import os

from discord import channel

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("okay")

@client.event
async def on_message(message):
    if message.content.startswith("test"):
        await message.channel.send("ready")
    if message.content.startswith("안녕"):
        await message.channel.send("하이")
    if message.content.startswith("help"):
      await message.channel.send("팀.짜기 이름1 이름2 ...이름n/팀1 팀2 ...팀n")
      await message.channel.send("팀 뒤에 있는 .빼고 띄어쓰기 조심")
    if message.content.startswith("팀짜기"):
        team = message.content[4:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        await message.channel.send("무작위로 팀을 나눴습니다.")
        for i in range(0, len(person)):
          await message.channel.send("●" + person[i] + "→" + teamname[i])

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

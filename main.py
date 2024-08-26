import discord



TOKEN = input("Please enter your bot token: ")



intents = discord.Intents.all()
client = discord.Client(intents=intents)



counter = 0

@client.event
async def on_ready():
    global counter
    games = {}
    with open("list.txt", mode='w', encoding='utf8') as f:
            for guild in client.guilds:
                print(f'{guild.name} (id: {guild.id})')
                for member in guild.members:
                    counter += 1 
                    activities_list = []


                    for activity in member.activities:
                        if isinstance(activity, discord.Game):
                            activities_list.append(activity.name)
                            if activity.name not in games:
                                games[activity.name] = 0
                            games[activity.name] += 1
                        elif isinstance(activity, discord.Streaming):
                            activities_list.append(f"Streaming: {activity.name}")
                        elif isinstance(activity, discord.CustomActivity):
                            activities_list.append(f"Custom Status: {activity.name}")
                        elif isinstance(activity, discord.Activity):
                            activities_list.append(f"Activity: {activity.name}")


                    if not activities_list:
                        activities_list.append("No Activity")

                    activities_str = "; ".join(activities_list)



                    print(f"Scraped :{counter}")
                    

                    line = '{} {} {} {} {}\n'.format(counter, member.name + "#" + member.discriminator, member.display_name, member.id, activities_str)
                    f.write(line)




client.run(TOKEN)

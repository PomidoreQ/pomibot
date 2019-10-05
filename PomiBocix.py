import discord
import random

client = discord.Client()

CURSES = ["kurwa", "pierdole", "pierdol", "jebane", "jebany", "pierdolony", "jeb się", "kurwo", "cholera", "cholernik", "skurwysyn", "pierdolec", "spierdalaj", "spierdalam", "spierdolony", "huj", "szmaciura", "pojebany", "pojebaniec", "pojebana", "pojeb", "skurwiel"]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('?pomoc'))
    print('Wszystko działa poprawnie. Bot jest teraz online.')

@client.event
async def on_message(message):

    if any([curse in message.content.lower() for curse in CURSES]):
          await message.delete()
          await message.channel.send(f"{message.author.mention}, nie używaj tutaj takiego słownictwa!")
          return True
    
    if message.content.find("?ping") != -1:
        await message.channel.send("Pong! Jestem gotowy do użytku!")
        
    if message.content.find("?plany") != -1:
        await message.channel.send("Mam zamiar dodać do bota dużo komend!")
        
    if message.content == "?rzut-monetą":
        variable = [
            'Orzeł!',
            'Reszka!',]
        await message.channel.send(random.choice(variable))

    if message.content == "?koteły":
        variable = [
            'https://cdn.discordapp.com/attachments/565131804504489985/628644912816062465/pobrany_plik.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644896407814162/pobrany_plik_7.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644877361479720/pobrany_plik_6.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644853000962059/pobrany_plik_5.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644824349933599/pobrany_plik_4.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644764719251487/pobrany_plik_3.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644739339780127/pobrany_plik_2.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644722306711552/pobrany_plik_1.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644689205264425/images.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644666203439113/images_7.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644647476133889/images_6.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644627670499348/images_5.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644608104071168/images_4.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644584024703006/images_3.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644563019497502/images_2.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628644542719066143/images_1.jpg',]
        await message.channel.send(random.choice(variable))

    if message.content == "?pieseły":
        variable = [
            'https://cdn.discordapp.com/attachments/565131804504489985/628947761273765889/piese16.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947744840613888/piese15.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947728155803648/piese14.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947710745247744/piese13.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947692999147540/piese12.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947675848507422/piese11.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947656491794442/piese10.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947617841283092/piese9.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947591778009089/piese8.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947573993898019/piese7.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947553483751424/piese6.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947530582982687/piese5.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947514778845194/piese4.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947502854570004/piese3.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947490867249162/piese2.jpg',
            'https://cdn.discordapp.com/attachments/565131804504489985/628947476560216074/piese1.jpg',]
        await message.channel.send(random.choice(variable))

    if message.content == "?porada-życiowa":
        variable = [
            'Jeśli będziesz teraz uczył się więcej, później nie będziesz miał z tym problemów!',
            'Bądź sobą!',
            'Staraj się być miły (jeśli taki nie jesteś)!',
            'Pomóż, jeśli ktoś tego potrzebuje!',
            'Spędzaj jak najwięcej czasu z rodziną!',
            'Nie musisz mieć zawsze racji, pogódź się z tym!',
            'Możesz przetrwać wszystko, jeśli skupisz się na tym, co jest teraz!',
            'Słuchaj swojego serca i rób to co kochasz!',
            'Wierz w cuda!',
            'Bez względu na to, jak się czujesz, wstań, ubierz się i działaj!',
            'Nie bierz życia zbyt poważnie!',
            'Prawdziwy przyjaciel przybiegnie do Ciebie nawet o drugiej w nocy!',
            'Doceniaj małe rzeczy i to, co się dzieje w danej chwili!',
            'Zazdrość niszczy relacje!',
            'Nie rezygnuj z marzeń tylko dlatego, że wydają Ci się nieosiągalne!',]
        await message.channel.send(random.choice(variable))
        
    if message.content == "?pomoc":
        embed = discord.Embed(title="Komendy!", description="Znajdziecie tutaj wszystkie komendy.", color=random.randint(0,0xffffff))
        embed.add_field(name="?ping", value="Sprawdza, czy bot jest teraz online.", inline=False)
        embed.add_field(name="?info", value="Daje informacje o bocie.", inline=False)
        embed.add_field(name="?plany", value="Pokazuje plany na przyszłość dotyczące bota.", inline=False)
        embed.add_field(name="?pomoc", value="Pokazuje tą wiadomość.", inline=False)
        embed.add_field(name="?rzut-monetą", value="Losuje pomiędzy orłem a reszką. Świetne do rozstrzygania sporów.", inline=False)
        embed.add_field(name="?koteły", value="Wybiera losowe zdjęcie słodkiego kotka z tych, które są zaprogramowane. Sweet!", inline=False)
        embed.add_field(name="?pieseły", value="Ta komenda działa tak samo jak ?koteły, ale wysyła zdjęcia piesków!", inline=False)
        embed.add_field(name="?porada-życiowa", value="Losuje jedną z piętnastu porad życiowych. Najlepiej jest wykorzystać każdą na jeden dzień!", inline=False)
        await message.channel.send(content=None, embed=embed)

    if message.content == "?info":
        embed = discord.Embed(title="Informacje!", description="Krótkie info o bocie.", color=random.randint(0,0xffffff))
        embed.add_field(name="Autor", value="Pomi >;P#2203", inline=False)
        embed.add_field(name="O bocie", value="Zadanie tego bota to głównie rozrywka, ale ma też wbudowanego auto-moderatora do polskich przekleństw.", inline=False)
        await message.channel.send(content=None, embed=embed)
        
client.run("NjI3NzY2NDAwODAyMzU3MjQ4.XZCdmw.Ft60-7Nowkic8shebw-B7-3OYl0")

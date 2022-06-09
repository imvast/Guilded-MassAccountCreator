import os, sys
try: import httpx, asyncio, random, string, threading, logging; from rich.console import Console; console = Console(); from colorama import Fore as C
except ImportError: 
    os.system("py -m pip install -r .\\data\\requirements.txt")

os.system('cls')
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;40m[\x1b[38;5;8m%(asctime)s\x1b[38;5;40m]\x1b[38;5;8m %(message)s\x1b[0m",
    datefmt="%H:%M:%S"
)
    
    
class Guilded():
    
	def __init__(self) -> None:
		pass
	
	def Create(self):
		username = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(6))
		name = ''.join(random.choice(string.digits) for i in range(5))
		mail = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(12)) + "@vastmail.gg"
		password = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(15))
		url = "https://www.guilded.gg/api/users?type=email"
		payload = {
			"email": f"{mail}",
			"extraInfo": {"platform": "desktop"},
			"fullName": f"Vast{name}",
			"name": f"{username}",
			"password": f"{password}"
		}
		headers = {"accept": "application/json, text/javascript, */*; q=0.01","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","content-length": "149","content-type": "application/json","cookie": "guilded_mid=c9b727a5ba1da14ef1fb275950524cc0; guilded_ipah=25ke32e31b61b17f56d4e9a90c6da4e7","guilded-client-id": "8cdf0318-e401-41c2-90b3-31f1d4734705","guilded-stag": "".join(random.choice(string.ascii_lowercase + string.digits) for i in range(12)),"origin": "https://www.guilded.gg","referer": "https://www.guilded.gg/","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		with httpx.Client() as client:
			req = client.post(url, json=payload, headers=headers)
			if int(req.status_code) in(200,201):
				accounts_file = open(".\\data\\accounts.txt", "a"); accounts_file.write('%s:%s:%s\n' % (req.json()["user"]["id"],mail,password)); accounts_file.close()
				return logging.info(req.text)
				

	def start(self):
		while True:
			threading.Thread(self.Create()).start()

if __name__ == "__main__":
	asyncio.get_event_loop().run_until_complete(Guilded().start())
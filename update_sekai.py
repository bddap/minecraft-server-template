import requests, json

def j_get(url):
	return json.loads(requests.get(url).content)

r = j_get("https://launchermeta.mojang.com/mc/game/version_manifest.json")

#with open("result.json",'w') as f:
#	f.write(r.content)

latest_version = r["latest"]["snapshot"]

latest = {v["id"]:v for v in r["versions"]}[latest_version]

r = j_get(latest["url"])

def out(thing):
	json.dump(thing, open("res.json", 'w'), indent=1)

server_url = r["downloads"]["server"]["url"]

try:
	with open("sekai_version.json") as f:
		j = json.load(f)
	if j["server_url"] == server_url:
		do_download = False
	else:
		do_download = True
except IOError:
	do_download = True

if do_download:
	with open("server.jar", 'w') as f:
		f.write(requests.get(server_url).content)
	
	with open("sekai_version.json", 'w') as f:
		json.dump({
				"server_url":server_url,
				"server_version":latest_version				
			},f)







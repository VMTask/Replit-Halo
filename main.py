def install():
  try:
    import requests
  except ModuleNotFoundError:
    os.system("python -m pip install -U pip --user")
    os.system("pip install requests --user")
  import json
  version_raw = requests.get("https://luminouszigzagbookmark.intosoft.repl.co/d/version.json")
  version_json = json.loads(version_raw.text)
  url = "https://luminouszigzagbookmark.intosoft.repl.co/d/halo-" + version_json["version"] +"-SNAPSHOT.jar"
  print("开始下载")
  execcommand = "python3 downloader.py "+url
  os.system(execcommand)
  with open(".installed","w") as file:
    file.write("true")
  os.system("python3 boot.py")
  with open("jarfile.txt","w") as f:
    f.write("halo-" + version_json["version"] +"-SNAPSHOT.jar")
  

if __name__=='__main__':
  import os
  if(os.path.exists(".installed")):
    os.system("python3 boot.py")
  else:
    install()
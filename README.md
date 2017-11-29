# Markdown Image Server
a simple file server, you can upload snapshot to server in a very convenient way, and use the url in markdown.

## Server
a simple python torando server

* Install dependency
```
pip install torando
```

* Run
```
python fileserver/server.py
```

## Clients

### Ubuntu

* Install dependency
```
sudo apt-get install xclip
```

* Usage
1. execute `./snapshot.sh` to make a snapshot, and the scripts will upload the image to server automaticlly. 
(so, you can add this script to system shortcuts)
2. then, the image url will write to your clipper, `ctrl+v` it to wherever you want.
3. `snapshot-md.sh` will do the same job, and return a markdown image label like `![](http://localhost:8080/static/201711/1511966433.png)`

### Others
Welcome to provide scripts in Windows or MacOS
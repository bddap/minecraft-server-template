Self updating minecraft server, almost ready to go.

## Prerequsites:

- python3 (apt install python3)
- java (apt install openjdk-8-jre-headless)
- upnpc (apt install miniupnpc)
- tmux (apt install tmux)

## Scripts:

### start_server

Attempts to automatically forward port 25565.

Checks to see if the latest snapshot is installed. If not, downloads it as server.jar.

Starts server.jar in a tmux session named `sekai`.

### stop_server

Stops server. Ends tmux session.

### do_backup

Saves the current world into bak/{date_and_time}.tar.gz

## todo

- Systemd script for automatcally starting server.

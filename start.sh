cd ~/Desktop/Server/Sekai
sudo iptables --flush
python ./update_sekai.py
nohup java -Xms1G -Xmx3G -jar server.jar nogui <server.in > server.out 2>&1 &

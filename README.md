# Running the Airfoil service
1. Create an instance and contextualize it with the config file /worker/cloud-config-host.txt
2. Add a floating IP to the instance and ssh to it (The floating ip needs to be the same as in celeryconfig on this public repo, this would ideally not be the case)
3. Clone this repo into the instance
4. Run `source /worker/source.sh`to authenticate with the cloud
5. Start the server by running `python Server.py`

# Running the Airfoil service
1. Create an instance and contextualize it with the config file /worker/cloud-config-host.txt
2. Add a floating IP to the instance and ssh to it
3. Clone this repo into the instance
4. Change the BROKER_URL env variable in /worker/cloud-config.txt to reflect the IP of the newly created host instance

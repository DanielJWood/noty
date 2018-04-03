# to transfer to ec2
scp -i /Users/dwood/Documents/DWKey2.pem /Users/dwood/Sites/noty/scrape/scrape.sh ec2-user@ec2-35-164-23-64.us-west-2.compute.amazonaws.com:names2018

ssh -i "DWKey2.pem" ec2-user@ec2-35-164-23-64.us-west-2.compute.amazonaws.com

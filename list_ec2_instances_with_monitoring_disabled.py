import boto3

client = boto3.resource('ec2', 'us-west-2')

def lambda_handler(event, context):
    
    instances = client.instances.all()
    n=0
    #looping through instances
    for instance in instances:
        if instance.monitoring["State"] == "disabled":
            n=n+1
            print('Instance number:', n)
            print('EC2 instance ID:', instance.id)
            print('Instance state:', instance.state["Name"])
            print('Instance type:', instance.instance_type)
            print("Instance monitoring state: ", instance.monitoring["State"])
            print('-*'*30)

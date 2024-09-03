import boto3

Instance_ids = ['your instance id']

Region_Name = 'instance's region'

ec2 = boto3.client('ec2', region_name=Region_Name)
def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=Instance_ids)
    print('Started: ' + str(Instance_idsnstances))

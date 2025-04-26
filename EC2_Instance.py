import boto3

def launch_instance():

    ec2 = boto3.client('ec2', region='us-east-1')

    print(response)

    response = ec2.launch_instance(
        ImageId = 'ami-084568db4383264d4',
        Instance_Type ='t2.micro',
        Key_Name = 'Ansible_Managed',
        MinCount = 1,
        MaxCount = 1,
        SecurityGroupIds = 'sg-01ff7a0babb9688fb',
        SubnetId = 'subnet-05e144c45dee12c3f',
        TagSpecification = [
            {
                'ResourceType' : 'instance',
                'Tags' : [
                    {'Key': 'Name' , 'Value': 'MyBoto3Instance'}
                ]
            }
        ]  
    )









import boto3

def client_init():
  return boto3.client('ec2', region_name='eu-west-1')

def vpc_creation(client):
  client.create_vpc(CidrBlock='10.10.0.0/16')

if __name__ == "__main__":
  ec2_client = client_init()
  vpc_creation(ec2_client)

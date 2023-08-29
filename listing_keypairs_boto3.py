# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Create an EC2 client instance using boto3
ec2 = boto3.client('ec2')

# Describe key pairs to retrieve information about available key pairs
response = ec2.describe_key_pairs()

# Loop through each key pair in the response
for keypair in response['KeyPairs']:
    # Print the key pair's name and its ID
    print(keypair['KeyName'], keypair['KeyPairId'])

# Print the entire response (useful for debugging or more information)
print(response)


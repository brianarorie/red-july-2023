# Import the boto3 library, which provides an interface to interact with AWS services
import boto3

# Define a function to stop an EC2 instance
def stop_instance(client, instance_id):
    # Stop the specified instance
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    # Print a message indicating that the instance has been stopped
    print(instance_id, 'stopped')

# Define a function to start an EC2 instance
def start_instance(client, instance_id):
    # Start the specified instance
    response = ec2.start_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    # Print a message indicating that the instance has been started
    print(instance_id, 'started')

# Define a function to terminate an EC2 instance.
def terminate_instance(client, instance_id):
    # Terminate the specified instance
    response = ec2.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    # Print a message indicating that the instance has been terminated
    print(instance_id, 'terminated')

# Check if the script is being run as the main program
if __name__ == '__main__': 
    # Define the instance ID
    instance_id = 'i-0395a9944a319bd35'
    
    # Create an EC2 client instance using boto3
    ec2 = boto3.client('ec2')
    
    # Call the stop_instance function to stop the specified instance
    stop_instance(ec2, instance_id)
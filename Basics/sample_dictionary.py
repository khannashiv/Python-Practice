# This code defines a list called ec2_info, where each element is a dictionary representing information about an EC2 instance.

ec2_info = [
    {
        "id": "1",
        "type": "t2.micro"
    },
    {
        "id": "2",
        "type": "t2.small"
    },
    {
        "id": "3",
        "type": "t2.medium"
    }
]

print(ec2_info[1])         # This will print the second dictionary in the list, which contains the id and type of the second EC2 instance.
print(ec2_info[2]["type"]) # This will print the type of the third EC2 instance.
print(ec2_info[0]["id"])   # This will print the id of the first EC2 instance.
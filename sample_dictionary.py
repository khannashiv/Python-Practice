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

print(ec2_info[1])
print(ec2_info[2]["type"])
print(ec2_info[0]["id"])
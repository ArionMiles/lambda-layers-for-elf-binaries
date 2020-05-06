import subprocess

def lambda_handler(event, context):
    rig_command = "rig -d /opt/rig"
    random_identity = subprocess.getoutput(rig_command)
    return {
        "identity": random_identity,
    }

if __name__ == "__main__":
    # Test function
    print(lambda_handler("", ""))

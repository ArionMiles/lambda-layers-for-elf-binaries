# ELF Binaries for Lambda Layer

Sample code written for my blogpost on [Creating ELF Binaries for Lambda Layers](https://arionmiles.me/posts/lambda)

1. `pip3 install --user requirements.txt`
2. Run `aws configure` and add AWS Access, Secret Keys, and select your default region and response format (json).
    [Learn how to create AWS Access & Secret Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).
3. `sam deploy --guided`
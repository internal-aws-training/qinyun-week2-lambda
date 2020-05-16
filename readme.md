# AWS-training-week2
This repo is to create a lambda function which can read and copy files from different S3 buckets through *AWS CLI* and *Cloudformation*.

## Structure

![avatar](https://imgur.com/YSLj8ze.png)

## Run the project
```shell
./auto/main
```

## Create/Update the stack
### Prerequisite
In this script, `stackup` is used to inject parameters to the cloudformation configuration file.

To install `stackup`, run the following:
```shell
gem install stackup
```

To deploy the S3 buckets and lambda function to stack:
```shell
./auto/deploy
```
#!/usr/bin/python

import boto.ec2

region = raw_input("Enter Region to launch instance: ")
aws_access_key_id = raw_input("Enter aws access key: ")
aws_secret_access_key = raw_input("Enter Secret access key: ")
instance_type = raw_input("Enter instance Type: ")

conn = boto.ec2.connect_to_region(region,aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
instance = conn.run_instances('ami-d7b9a2b1',instance_type=instance_type)

reservations = conn.get_all_reservations(instance_ids=instance.instances[0].id)

for r in reservations:
    for i in r.instances:
        print('%s\t%s' % (i.id, i.launch_time))



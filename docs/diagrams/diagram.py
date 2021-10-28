#!/usr/bin/env python3
from diagrams import Cluster , Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.general import InternetGateway
from diagrams.aws.compute import LocalZones
from diagrams.aws.network import VPC

with Diagram("Web Service", show=False):
  igw = InternetGateway("igw")
  with VPC("production") as prodVPC:
    EC2("bastion")

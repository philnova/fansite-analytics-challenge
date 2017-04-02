import argparse
import feature1
import feature2

parser = argparse.ArgumentParser(description='Process hits from a server log.')
parser.add_argument('input_server_log',
    help='ASCII file containing server log of requests.')
parser.add_argument('output_hosts',
    help='Writeable text file to contain list of the top 10 most active host/IP addresses that have accessed the site.')
parser.add_argument('output_hours',
    help='Writeable text file to contain list of 10 resources that consume the most bandwidth on the site.')
parser.add_argument('output_resources',
    help='Writeable text file to contain list of the top 10 most frequently visited 60-minute periods.')
parser.add_argument('output_blocked',
    help='Writeable text file to contain potential security threats.')
args = parser.parse_args()

# Implement Feature 1
parser1 = feature1.FindMostActive(args.input_server_log, args.output_hosts, k=10)
parser1.parse()

# Implement Feature 2
parser2 = feature2.FindMostIntensiveResources(args.input_server_log, args.output_resources, k=10)
parser2.parse()

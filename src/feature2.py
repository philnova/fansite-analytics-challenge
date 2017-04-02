import collections
import csv
import read_server_log

def extract_bandwidth_from_row(row):
    try:
        bytes = int(row[-1])
    except:
        bytes = 0
    return bytes

class FindMostIntensiveResources(object):

    def __init__(self, input_file, output_file, k=10):
        self.input_file = input_file
        self.output_file = output_file
        self.resources_to_bandwidth = collections.Counter()
        self.top_k_resources = []
        self.k = k

    def parse(self):
        with open(self.input_file, 'rb') as f_input:
            csv_input = csv.reader(f_input, delimiter=' ')

            for row in csv_input:
                log_line = read_server_log.ServerLog(row)
                self.resources_to_bandwidth[log_line.resource] = self.resources_to_bandwidth.get(log_line.resource, 0) + log_line.bytes

            # collections.Counter allows us to return the k largest (item,count) pairs
            # using a heapsort algorithm, so runs in O(n log k)
            self.top_k_resources = self.resources_to_bandwidth.most_common(self.k)

            with open(self.output_file, 'w') as f_output:
                for item in self.top_k_resources:
                    f_output.write(item[0]+"\n")
           

import collections
import csv

class FindMostActive(object):

    def __init__(self, input_file, output_file, k=10):
        self.input_file = input_file
        self.output_file = output_file
        self.hosts_to_hits = collections.Counter()
        self.top_k_hits = []
        self.k = k

    def parse(self):
        with open(self.input_file, 'rb') as f_input:
            csv_input = csv.reader(f_input, delimiter=' ')

            for row in csv_input:
                self.hosts_to_hits[row[0]] = self.hosts_to_hits.get(row[0], 0) + 1

            # collections.Counter allows us to return the k largest (item,count) pairs
            # using a heapsort algorithm, so runs in O(n log k)
            self.top_k_hits = self.hosts_to_hits.most_common(self.k)

            with open(self.output_file, 'w') as f_output:
                for item in self.top_k_hits:
                    f_output.write(item[0]+","+str(item[1])+"\n")

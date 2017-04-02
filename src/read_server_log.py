class ServerLog(object):

    def __init__(self, delimited_list):
        self.host = delimited_list[0]
        self.timestamp = delimited_list[3]
        self.request = delimited_list[5]
        self.resource = self.get_resource(self.request)
        self.response_code = delimited_list[6]
        self.bytes = self.get_bytes(delimited_list[7])

    def get_bytes(self, byte_string):
        try:
            bytes = int(byte_string)
        except:
            bytes = 0 # '-' should be interpreted as 0 bytes
        return bytes

    def get_resource(self, request):
        request_list = request.split(' ')
        if len(request_list) == 1:
            return request
        else:
            return request_list[1]

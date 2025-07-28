import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        self.read_amount = 0
        self.read_count = 0
        self.write_count = 0
        self.write_amount = 0

        return super().__init__(args, kwargs)
    

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        self.read_count += 1

        result = super().readline()

        if len(result) == 0:
            raise StopIteration
        else:
            self.read_amount += len(result)
            
            return result

    def read(self, size=-1):
        result = super().read(size)
        self.read_count += 1
        self.read_amount += len(result)

        return result


    @property
    def read_bytes(self):
        return self.read_amount

    @property
    def read_ops(self):
        return self.read_count

    def write(self, b):
        self.write_count += 1
        result = super().write(b)
        self.write_amount += result


        return result

    @property
    def write_bytes(self):
        return self.write_amount

    @property
    def write_ops(self):
        return self.write_count

class MeteredSocket:
    def __init__(self, socket):
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        return self  # don't call super().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(data)
        self._recv_ops += 1

        return data

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        bytes_sent = self._socket.send(data, flags)
        self._send_bytes += bytes_sent
        self._send_ops += 1

        return bytes_sent

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops
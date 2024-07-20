import serial
import serial.tools.list_ports
import threading

class SerialReader:
    def __init__(self, port, baudrate, bytesize, parity, stopbits, output_file, output_format):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.output_file = output_file
        self.output_format = output_format
        self.ser = None
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.read_from_comport)
            self.thread.start()
            return True
        return False

    def stop(self):
        if self.running:
            self.running = False
            self.thread.join()
            return True
        return False

    def read_from_comport(self):
        try:
            self.ser = serial.Serial(
                self.port,
                self.baudrate,
                bytesize=self.bytesize,
                parity=self.parity,
                stopbits=self.stopbits,
                timeout=1
            )
            print(f"Connected to {self.port} at {self.baudrate} baudrate.")
            with open(self.output_file, 'a') as f:
                while self.running:
                    if self.ser.in_waiting > 0:
                        data = self.ser.read(self.ser.in_waiting)
                        if self.output_format == 'hex':
                            data_str = ' '.join(f'{byte:02x}' for byte in data)
                        else:
                            data_str = data.decode('utf-8')
                        print(data_str, end='')
                        f.write(data_str)
                        f.flush()
        except serial.SerialException as e:
            print(f"Error opening or reading from {self.port}: {e}")
        finally:
            if self.ser and self.ser.is_open:
                self.ser.close()
            print(f"Disconnected from {self.port}.")
            print(f"Data has been saved to {self.output_file}")
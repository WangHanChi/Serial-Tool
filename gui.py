import os
import serial
import serial.tools.list_ports
import SerialReader
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SerialGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COM Port Reader")
        self.serial_reader = None

        self.create_widgets()
        self.update_ports()

    def create_widgets(self):
        self.port_label = tk.Label(self.root, text="Serial Port:")
        self.port_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.port_combobox = ttk.Combobox(self.root, width=30)
        self.port_combobox.grid(row=0, column=1, padx=10, pady=5)
        
        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.update_ports)
        self.refresh_button.grid(row=0, column=2, padx=10, pady=5)

        self.baudrate_label = tk.Label(self.root, text="Baud Rate:")
        self.baudrate_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.baudrate_combobox = ttk.Combobox(self.root, width=30)
        self.baudrate_combobox['values'] = (9600, 19200, 38400, 57600, 115200)
        self.baudrate_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.baudrate_combobox.set(115200)  # set default baud rate

        self.bytesize_label = tk.Label(self.root, text="Data Bits:")
        self.bytesize_label.grid(row=2, column=0, padx=10, pady=5)

        self.bytesize_combobox = ttk.Combobox(self.root, width=30)
        self.bytesize_combobox['values'] = (5, 6, 7, 8)
        self.bytesize_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.bytesize_combobox.set(8)  # set default bit

        self.parity_label = tk.Label(self.root, text="Parity:")
        self.parity_label.grid(row=3, column=0, padx=10, pady=5)

        self.parity_combobox = ttk.Combobox(self.root, width=30)
        self.parity_combobox['values'] = ('N', 'E', 'O', 'M', 'S')  # None, Even, Odd, Mark, Space
        self.parity_combobox.grid(row=3, column=1, padx=10, pady=5)
        self.parity_combobox.set('N')  # set default parity selection

        self.stopbits_label = tk.Label(self.root, text="Stop Bits:")
        self.stopbits_label.grid(row=4, column=0, padx=10, pady=5)

        self.stopbits_combobox = ttk.Combobox(self.root, width=30)
        self.stopbits_combobox['values'] = (1, 1.5, 2)
        self.stopbits_combobox.grid(row=4, column=1, padx=10, pady=5)
        self.stopbits_combobox.set(1)  # set default stop bit
        
        self.output_format_label = tk.Label(self.root, text="Output Format:")
        self.output_format_label.grid(row=5, column=0, padx=10, pady=5)

        self.output_format_combobox = ttk.Combobox(self.root, width=30)
        self.output_format_combobox['values'] = ('string', 'hex')
        self.output_format_combobox.grid(row=5, column=1, padx=10, pady=5)
        self.output_format_combobox.set('string')  # set default output format
        
        self.file_label = tk.Label(self.root, text="Output File:")
        self.file_label.grid(row=6, column=0, padx=10, pady=5)
        
        self.file_entry = tk.Entry(self.root, width=33)
        self.file_entry.grid(row=6, column=1, padx=10, pady=5)
        self.file_entry.insert(0, os.path.join(os.getcwd(), "output.txt"))  # set default PATH
        
        self.start_button = tk.Button(self.root, text="Start", command=self.start_reading)
        self.start_button.grid(row=7, column=0, padx=10, pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_reading)
        self.stop_button.grid(row=7, column=1, padx=10, pady=10)

    def update_ports(self):
        ports = serial.tools.list_ports.comports()
        self.port_combobox['values'] = [port.device for port in ports]
        if ports:
            self.port_combobox.current(0)

    def start_reading(self):
        port = self.port_combobox.get()
        baudrate = self.baudrate_combobox.get()
        bytesize = self.bytesize_combobox.get()
        parity = self.parity_combobox.get()
        stopbits = self.stopbits_combobox.get()
        output_format = self.output_format_combobox.get()
        output_file = self.file_entry.get()

        if not port or not baudrate or not bytesize or not parity or not stopbits or not output_format or not output_file:
            messagebox.showwarning("Input Error", "Please provide all input fields.")
            return
        
        try:
            baudrate = int(baudrate)
            bytesize = int(bytesize)
            stopbits = float(stopbits)
        except ValueError:
            messagebox.showerror("Input Error", "Baud rate, data bits and stop bits must be numbers.")
            return

        parity_dict = {
            'N': serial.PARITY_NONE,
            'E': serial.PARITY_EVEN,
            'O': serial.PARITY_ODD,
            'M': serial.PARITY_MARK,
            'S': serial.PARITY_SPACE
        }

        parity = parity_dict.get(parity, serial.PARITY_NONE)

        self.serial_reader = SerialReader(port, baudrate, bytesize, parity, stopbits, output_file, output_format)
        if self.serial_reader.start():
            messagebox.showinfo("Started", "Started reading from COM port.")
        else:
            messagebox.showwarning("Already Running", "Reading is already in progress.")

    def stop_reading(self):
        if self.serial_reader and self.serial_reader.stop():
            messagebox.showinfo("Stopped", "Stopped reading from COM port.")
        else:
            messagebox.showwarning("Not Running", "Reading is not in progress.")
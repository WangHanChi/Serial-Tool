# Serial-Tool

This project is a Python-based COM port data logger with a GUI for selecting COM port settings. The application can read data from a specified COM port and save the data to a text file. The application supports options for displaying data as either hexadecimal or string format.

## Features

- Automatically search and list available COM ports.
- Allow selection of COM port settings (baud rate, data bits, parity, stop bits).
- Display incoming data in hexadecimal or string format.
- Save received data to a text file.
- Gracefully handle Ctrl-C to stop logging and save the file.

## Requirements

- Python 3.x
- `pyserial` package
- `tkinter` package (comes with standard Python installation)

## Installation

### Linux

To install the required packages on Linux, run:

```sh
$ sudo apt-get update
$ sudo apt-get install python3-tk
$ pip install pyserial
```

### macOS
To install the required packages on macOS, run:

```sh
$ brew install python-tk
$ pip install pyserial
```

### Windows
To install the required packages on Windows, you need to download and install Python from the official website if it is not already installed. Use the following link:

[Down load Python 3.12.3](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe)  
[Install Guide](https://docs.python.org/3/using/windows.html)

After installing Python, install the required packages:

```sh
pip install pyserial
```

## Makefile Commands
The Makefile provided includes commands to help with setting up the environment, installing dependencies, running the script, and packaging it as an executable.

### Install Dependencies
To install the required Python packages and tkinter, run:

```sh
$ make install
```

### Setup Environment
To check and install Python if it is not already installed, run:

```sh
$ make env
```

### Run the Application
To run the application, use:

```sh
$ make run
```

### Package the Application
To package the application into an executable, use:

```sh
$ make package
```

This will create an executable in the dist/ directory.


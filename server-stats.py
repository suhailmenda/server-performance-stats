import subprocess
import platform
import time
import re

def get_cpu_usage_mac():
    result = subprocess.run(['top', '-l1'])
    
    output = result.stdout.splitlines()
    cpu_line = None
    for line in output:
        if "CPU" in line:
            cpu_line = line
            break
    
    if cpu_line:
        pattern = r"(\d+\.\d+)%"
        cpu_usage_info = re.findall(pattern,cpu_line)
        user_space = float(cpu_usage_info[0])
        system_space = float(cpu_usage_info[1])
        idle_space = float(cpu_usage_info[2])

        total_usage = user_space + system_space
        return total_usage
    return None

def get_cpu_usage_windows():
    # Run the 'wmic cpu' command to get the CPU usage on Windows
    result = subprocess.run(['wmic', 'cpu', 'get', 'loadpercentage'], capture_output=True, text=True)
    
    # Parse the output to extract the CPU usage percentage
    output = result.stdout.splitlines()
    if len(output) > 1:
        # The second line should contain the load percentage
        return float(output[1].strip())
    return None

def get_cpu_usage_linux():
    result = subprocess.run(["top", "-b", "-n1"], capture_output=True,text=True)
    output = result.stdout.splitlines()
    cpu_line = None
    for line in output:
        if "%Cpu(s)" in line:
            cpu_line = line
            break
    if cpu_line:
        pattern = r"(\d+.\d+)"
        percent = re.findall(pattern,cpu_line)
        cpu_usage_info = 100 - float(percent[3])
        return cpu_usage_info
    return None

def get_cpu_usage():
    if platform.system() == 'Linux':  # macOS is Darwin
        return get_cpu_usage_linux()
    elif  platform.system() == 'Darwin':
        return get_cpu_usage_mac()
    elif platform.system() == 'Windows':
        return get_cpu_usage_windows()
    else:
        return None

# Get the total CPU usage and print it
cpu_usage = get_cpu_usage()
print(f"Total CPU Usage: {cpu_usage}%")

import subprocess
import platform
import time
import re

def get_usage_mac():
    result = subprocess.run(['top', '-l1'], capture_output=True, text=True)
    output = result.stdout.splitlines()
    cpu_line = None
    MemUsage = None
    for line in output:
        if "CPU" in line:
            cpu_line = line

        if "PhysMem" in line:
            MemUsage = line
    
        if cpu_line and MemUsage:
            break 
    
    
    if cpu_line and MemUsage:
        pattern = r"(\d+\.\d+)%"
        cpu_usage_info = re.findall(pattern,cpu_line)
        user_space = float(cpu_usage_info[0])
        system_space = float(cpu_usage_info[1])
        idle_space = float(cpu_usage_info[2])
        total_usage = user_space + system_space
        mem = re.findall(r"\d+", MemUsage) 
        freeMem = float(mem[3]) * 1024
        usageMem = float(mem[0]) * 1024
        percentMem = (freeMem / usageMem ) * 100
        df_output = subprocess.run(["df","-h"], capture_output=True, text=True)
        diskUsage = df_output.stdout
        return total_usage, freeMem , usageMem , percentMem, diskUsage
    return None


def get_usage_linux():
    result = subprocess.run(["top", "-b", "-n1"], capture_output=True,text=True)
    output = result.stdout.splitlines()
    cpu_line = None
    MemUsage = None
    freeMem = None
    usageMem = None
    percentMem = None
    cpu_usage_info = None

    for line in output:
        if "%Cpu(s)" in line:
            cpu_line = line
        if "MiB Mem" in line:
            MemUsage = line
        if cpu_line and MemUsage:
            break

    if cpu_line and MemUsage:
        pattern = r"(\d+.\d+)"
        percent = re.findall(pattern,cpu_line)
        cpu_usage_info = 100 - float(percent[3])
        mem = re.findall(r'\d+\.\d+|\d+', MemUsage)
        freeMem, usageMem = float(mem[1]), float(mem[2])
        percentMem = (usageMem / freeMem) * 100
        df_output = subprocess.run(["df","-h"], capture_output=True, text=True)
        diskUsage = df_output.stdout
        return cpu_usage_info, freeMem , usageMem , percentMem, diskUsage
    return None



def get_usage():
    if platform.system() == 'Linux':  # macOS is Darwin
        return get_usage_linux()
    elif  platform.system() == 'Darwin':
        return get_usage_mac()
    elif platform.system() == 'Windows':
        return get_cpu_usage_windows()
    else:
        return None


cpu_usage, freeMem, usageMem, percentMem, diskUsage = get_usage()

print(f"Cpu Usage is {cpu_usage}%, free memory is {freeMem}MB, memory used is {usageMem}MB and percentage of memory used is {percentMem}%")
print("This is the disk usage")
print(f"{diskUsage}")

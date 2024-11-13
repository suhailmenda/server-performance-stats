#!/bin/bash

# Function to display CPU usage
cpu_usage() {
    echo "CPU Usage:"
    let total_cpu=0
    for ((i=1; i<=5; i++))
    do
	    cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
	    echo "CPU usage in $i cycle: $cpu_usage"
	 	total_cpu=$($cpu_usage + $total_cpu | bc)
	    echo "$cpu_usage"
done		
}

### Function to display memory usage
#memory_usage() {
    #echo "Memory Usage:"
    #free -h | awk 'NR==2{printf "Total: %s | Used: %s | Free: %s | Percentage Used: %.2f%\n", $2, $3, $4, $3/$2 * 100}'
    #echo
#}

## Function to display disk usage
#disk_usage() {
    #echo "Disk Usage:"
    #df -h | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{print $1 ": " $3 " used, " $4 " available, " $5 " used (" $2 ")"}'
    #echo
#}

## Function to display top 5 processes by CPU usage
#top_cpu_processes() {
    #echo "Top 5 Processes by CPU usage:"
    #ps aux --sort=-%cpu | head -n 6 | awk 'NR>1 {print $3"% CPU usage - " $11}'
    #echo
#}

## Function to display top 5 processes by memory usage
#top_memory_processes() {
    #echo "Top 5 Processes by Memory usage:"
    #ps aux --sort=-%mem | head -n 6 | awk 'NR>1 {print $4"% Memory usage - " $11}'
    #echo
#}

## Function to display OS version
#os_version() {
    #echo "OS Version:"
    #lsb_release -a | grep "Description" | awk -F"\t" '{print $2}'
    #echo
#}

## Function to display uptime
#uptime_info() {
    #echo "Uptime:"
    #uptime -p
    #echo
#}

## Function to display load average
#load_average() {
    #echo "Load Average (1, 5, 15 min):"
    #uptime | awk -F'load average: ' '{print $2}'
    #echo
#}

## Function to display logged-in users
#logged_in_users() {
    #echo "Logged-in Users:"
    #who | awk '{print $1}' | sort | uniq
    #echo
#}




## Function to display failed login attempts (from /var/log/auth.log)
#failed_logins() {
    #echo "Failed Login Attempts (last 24 hours):"
    #sudo grep "Failed password" /var/log/auth.log* | grep -i "sshd" | wc -l
    #echo
#}

## Main function to execute all stats
#main() {
    #cpu_usage
    #memory_usage
    #disk_usage
    #top_cpu_processes
    #top_memory_processes
    #os_version
    #uptime_info
    #load_average
    #logged_in_users

    #failed_logins
#}
## Run the main function
#main

cpu_usage

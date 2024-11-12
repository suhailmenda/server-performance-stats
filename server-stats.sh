#!/bin/bash

function cpu_total() {
    for i in {1..5} 
    do 
        top -n1 -b | grep "%Cpu" 
    done
}

cpu_total
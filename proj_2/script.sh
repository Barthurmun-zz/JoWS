#!/bin/bash

for i in {220..230}
    do
	    for k in {2..8..2}
	        do
		        echo "CBR scenario with 2 STA and 1 AP, only 1 scenario is moving RNG:$i meters:$k"
				python proj_2.py --distance=$k --RngRun=$i >> Results/cbr_2sta1ap_onlyonestamoving_dist$k.txt 2>&1
	        done
    done

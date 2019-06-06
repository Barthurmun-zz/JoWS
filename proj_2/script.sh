#!/bin/bash

for i in {220..230}
    do
	    for k in {0..10..1}
	        do
		        echo "CBR scenario with 2 STA and 1 AP"
				python proj_2.py --distance=$k --RngRun=$i >> Results/cbr_2sta1ap_dist$k.txt 2>&1
	        done
    done

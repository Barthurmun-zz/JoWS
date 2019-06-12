#!/bin/bash

for i in {220..230}
    do
	    for k in {0..30..2}
	        do
				echo "CBR scenario with 2 STA and 1 AP, only 1 scenario is moving RNG:$i meters:$k"
				python proj_2.py --distance=$k --RngRun=$i >> Results/cbr_2sta1ap_VIonFirstSta_onlyonestamoving_dist$k.txt 2>&1
		        #echo "VBR scenario with 2 STA and 1 AP, only 1 scenario is moving RNG:$i meters:$k"
				#python proj_2_VBR.py --distance=$k --RngRun=$i >> Results/vbr_2sta1ap_VIonFirstSta_onlyonestamoving_dist$k.txt 2>&1
	        done
    done

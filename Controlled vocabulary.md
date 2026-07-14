# FDD-ON controlled vocabulary list (version: 2026A)
The controlled vocabulary list was released in January 25, 2026.
FDD-ON include lists of controlled vocabulary to define fault types and symptom statuses. 

## Controlled vocabulary list for describing fault types

|No.|Fault type|Definition|Example components in which a fault may occur|
| --- | --- | --- |--- |
|1.|Bias|Sensor reading value consistently deviates from the true value, creating a persistent measurement error.|Sensor|  
|2.|Drift|Sensor reading value gradually deviates from the true value over time.|Sensor|
|3.|Freeze|Sensor reading remains a constant value even if the true value changes.|Sensor|
|4.|Air-side fouling|Fouling is the buildup of sediments and debris on the surface area of a coil.|Coil|
|5.|The accumulation of unwanted deposits on the internal (water-contacting) surfaces of coils.|Coil|
|6.|Leakage|Fluid leaks from a high-pressure region to a low-pressure region.|Coil, valve, duct, damper|
|7.|Stuck|Fouling is the buildup of sediments and debris on the surface area of a coil.|Coil, valve, duct, damper|
|8.|Hunting|The actuator continuously modulates back and forth, over-correcting its position while attempting to reach a stable setpoint. |Valve, damper|
|9.|Blockage|The component is physically blocked, causing a significant increase of resistance to airflow.|Filter, vent|
|10.|Looseness|The physical part of a system is not securely fastened, properly tensioned, or correctly seated. |Fan belt|
|11.|Failure|The component stops work.|Heat pump compressor|
|12.|Setting error|The parameters, control sequence, or logic in the software are wrongly set. |VAV terminal unit schedule |
|13.|Location error|The component is installed in the wrong place.|VAV discharge air temperature sensor|
|14.|Overcharge|The fluid is overcharged. |Refrigerant|
|15.|Undercharge|The fluid is undercharged.|Refrigerant|
|16.|Restriction|The flow in the component (coil, tube, or pipe) is restricted, reducing the fluid flow rate. |Refrigerant circuit |
|17.|Loss|In communication, data packages are lost.|Communication data|
|18.|Oversize|The equipment or components are oversized.|Chilled water supply pump|
|19.|Undersize|The equipment or components are undersized.|Chilled water supply pump|
|20.|Offline|The controller stops work.|AHU controller|

## Controlled vocabulary list for describing symptom statuses
|No.|Fault type|Definition|Example components in which a fault may occur|
| --- | --- | --- |--- |
|1.|High|The measured value is higher than the baseline value or the reference value.|Supply air temperature |  
|2.|Low|The measured value is lower than the baseline value or the reference value.|Supply air temperature |
|3.|Slow response|The measured value has excessive settling time.|Chilled water supply temperature |
|4.|Unresponse|The measured value keeps constant when it should change.|Damper position signal|  
|5.|Oscillation|The measured value has cyclical variation.|Discharge air damper control signal|
|6.|Cycling|The measured equipment status or equipment control command signal is switched between an 'on' (logic high or 100% of the normal value) status and an 'off' status (logic low or 0% of the normal value) frequently or irregularly.|Damper position signal|
|7.|Spike|The measured value contains a transient sharp peak.|Pump control signal|  
|8.|Step change|The measured value appears as a sudden and discrete shift from one steady level to another level.|Damper control signal|
|9.|Intermittent|The measured value appears and disappears irregularly.|Pump control signal|
|10.|Mismatch|The measured values are not matched.|Damper position and control signal|
|11.|Simultaneous Occurrence|The signals can be measured at the same time, but logically they should not be measured at the same time.|Cooling valve position signal and heating valve position signal|

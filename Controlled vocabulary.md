# FDD-ON controlled vocabulary list (version: 2026A)
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

## Controlled vocabulary list for for describing symptom statuses
|No.|Fault type|Definition|Example components in which a fault may occur|
| --- | --- | --- |--- |
|1.|High|Sensor reading value consistently deviates from the true value, creating a persistent measurement error.|Sensor|  
|2.|Low|Sensor reading value gradually deviates from the true value over time.|Sensor|
|3.|Slow response|Sensor reading remains a constant value even if the true value changes.|Sensor|
|4.|Unresponse|Sensor reading value consistently deviates from the true value, creating a persistent measurement error.|Sensor|  
|5.|Oscillation|Sensor reading value gradually deviates from the true value over time.|Sensor|
|6.|Cycling|Sensor reading remains a constant value even if the true value changes.|Sensor|
|7.|Spike|Sensor reading value consistently deviates from the true value, creating a persistent measurement error.|Sensor|  
|8.|Step change|Sensor reading value gradually deviates from the true value over time.|Sensor|
|9.|Intermittent|Sensor reading remains a constant value even if the true value changes.|Sensor|
|10.|Mismatch|Sensor reading value gradually deviates from the true value over time.|Sensor|
|11.|Simultaneous Occurrence|Sensor reading remains a constant value even if the true value changes.|Sensor|


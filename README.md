# MFB (ModEM File Builder)

## Overview

Simple GUI software to carry out pre- and post- procesess for ModEM (Egbert and Kelbert, 2012)

![SS1](https://user-images.githubusercontent.com/62272721/149767139-ca5f9ed0-e652-457a-850f-d86f37ece25d.png)

![SS2](https://user-images.githubusercontent.com/62272721/149767262-2c74b5d9-d618-4099-ac5d-05501586095d.png)

## Features

- Simple GUI
- Pre- and post- processing can be done in one software.
- Initial model is created taking into account the topography.
- Observation point location and grid are automatically drawn.
- Observed and Calculated apparent resistivity and phase can be easily compared.
- Resistivity structure, hypocenters and other points can be easily exported to paraview format.
- Resistivity structure can be easily partially modified for sensitivity check.


## Requirement

- python3 or more
- pandas
- numpy
- matplotlib
- seaborn
- pyevtk
- pyproj
- PysimpleGUI

## Usage

1. Prepare DEM and bathymetry (if needed).
2. Prepare the file with the latitude and longitude of the observation point.
3. Find the EPSG code of the destination Cartesian coordinate system.(https://epsg.io/)
4. Launch MFB

    `$ python mfb_gui.py`

5. Configure settings via GUI (Push 'Save Settings' Button)
6. Make files (Push 'Make files' Button)
7. Carry out the inversion via ModEM
8. Carry out post-processes

## Installation

    $ git clone https://github.com/r-tnk/MFB.git

## Author

[R. Tanaka](https://www.researchgate.net/profile/Ryo-Tanaka-12)

## License

[MIT](https://github.com/r-tnk/MFB/blob/main/LICENSE)


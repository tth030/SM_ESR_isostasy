# SM_ESR_isostasy

This repository contains a collection of [Jupyter notebooks](#jupyter-notebooks) and [datasets](#datasets) as supplement of the following research paper:

- Theunissen, T., Huismans, R.S., Lu, G. and Riel, N. Relative continent/mid-ocean ridge elevation: a reference case for isostasy in geodynamics. Earth-Science Reviews (Submission January 2022)

***Please cite the source when using these data.***

This Repository allows:

- Displaying data and computing statistics on elevation of continents and mid-ocean ridges
- Displaying and downloading thermodynamic solutions including input files, raw data and grids of density, melt fraction,...
- Computing basic 1-D isostatic balance for a reference case

While you can run these notebooks on Binder (except topo_cont.ipynb that requires too much RAM), only a part of the data are accessible from there. Full data are localized on FigShare with the same structure as on the github repository. Therefore, we encourage you to download the full dataset on FigShare and to run jupyter-lab locally in order to be able to display everything.

## Content

- [How to run the notebooks?](#how-to-run-the-notebooks)
    - [Run in the cloud (Binder)](#run-in-the-cloud-binder)
    - [Install and run locally (Conda)](#install-and-run-locally-conda)
- [Jupyter notebooks](#jupyter-notebooks)
- [Datasets](#datasets)

## How to run the notebooks?

### Run in the cloud (Binder)

You can run the notebooks in your browser without installing anything thanks to
[binder](https://mybinder.org/). Just follow the link below and it will launch 
remotely a new notebook server for you:

- [Run on binder](https://mybinder.org/v2/gh/tth030/SM_ESR_isostasy/main?labpath=start.ipynb)

### Install and run locally (Conda)

Assuming that you have `git` and [conda](https://conda.io/docs/index.html)
installed, you can install all the packages required to run the notebooks in a
new conda environment using the following commands:

```bash
$ git clone https://github.com/tth030/SM_ESR_isostasy.git
$ cd SM_ESR_isostasy
$ conda env create -f environment.yml
$ conda activate SM_ESR_isostasy
```

You also need to install a few Jupyterlab extensions with the following command
(this step won't be required anymore with Jupyterlab >= 3.x):

```bash
$ jupyter labextension install \
    @jupyter-widgets/jupyterlab-manager \
    @pyviz/jupyterlab_pyviz \
    dask-labextension \
    ipygany
```

You then need to download the data on Figshare following this [link](https://figshare.com/) (the public link will not be available before publication).
After that, you have to move the `data_figshare` folder into `SM_ESR_isostasy/`.

Finally run the command below to start the Jupyterlab application. It should
open a new tab in your browser.

```bash
$ jupyter-lab start.ipynb
```

## Jupyter notebooks

- `start.ipynb`: general introduction and disclaimers.
- `topo_cont.ipynb`: data display and computation of statistics of Earth Topography.
- `topo_MOR.ipynb`: data display and computation of statistics of mid-ocean ridges elevation.
- `thermo.ipynb`: data display and building grid from results of thermodynamic calculations.
- `isostasy_ref.ipynb`: 1-D isostatic comparison of reference columns, provide semi-analytical solution for the water depth at the ridge for models M1 and M2.
- `isostasy_calib.ipynb`: Calibration of the crustal density and degree of depletion of the continentlal lithospheric mantle and sensitivity on water depth/sea level.
- `isostasy_calib2.ipynb`: Calibration of the reference mantle density with temperature dependent only densities (model M2).

## Datasets

### Disclaimer:

Some files provided here (data/) comes from a preliminary filtering using a command that is described in each binary header (can be read using `ncinfo` or `gmt gmtinfo`). Links provided here will give you access directly to the raw data or to a contact email.

***Please cite each specific source when using these data.***

### ETOPO1

- [https://www.ngdc.noaa.gov/mgg/global/](https://www.ngdc.noaa.gov/mgg/global/)
- NOAA National Geophysical Data Center. 2009: ETOPO1 1 Arc-Minute Global Relief Model. NOAA National Centers for Environmental Information. Accessed [date]\
- Amante, C. and B.W. Eakins, 2009. ETOPO1 1 Arc-Minute Global Relief Model: Procedures, Data Sources and Analysis. NOAA Technical Memorandum NESDIS NGDC-24. National Geophysical Data Center, NOAA. [doi:10.7289/V5C8276M](http://dx.doi.org/10.7289/V5C8276M) [access date]

### Seafloor ages and spreading rate

- [https://www.earthbyte.org/age-spreading-rates-and-spreading-asymmetry-of-the-worlds-ocean-crust/](https://www.earthbyte.org/age-spreading-rates-and-spreading-asymmetry-of-the-worlds-ocean-crust/)
- M??ller, R.D., M. Sdrolias, C. Gaina, and W.R. Roest 2008. Age, spreading rates and spreading symmetry of the world's ocean crust, Geochem. Geophys. Geosyst., 9, Q04006, [doi:10.1029/2007GC001743](https://doi.org/10.1029/2007GC001743)

### Horizontal strain rate

- [https://gsrm2.unavco.org/intro/intro.html](https://gsrm2.unavco.org/intro/intro.html)
- Kreemer, C., G. Blewitt, E.C. Klein, 2014, A geodetic plate motion and Global Strain Rate Model, Geochemistry, Geophysics, Geosystems, 15, 3849-3889, [https://doi.org/10.1002/2014GC005407](https://doi.org/10.1002/2014GC005407)

### High resolution bathymetry data

- [https://www.gmrt.org/about/](https://www.gmrt.org/about/)
- Ryan, W. B. F., et al. (2009), Global Multi-Resolution Topography synthesis, Geochem. Geophys. Geosyst., 10, Q03014, [doi:10.1029/2008GC002332](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2008GC002332)

### Lithospheric thickness (average based on several seismological estimates)

- Steinberger, B. and Becker, T.W. A comparison of lithospheric thickness models, Tectonophysics, 746 (2018), pp. 325-338, [doi.org/10.1016/j.tecto.2016.08.001](https://www.sciencedirect.com/science/article/pii/S004019511630316X?via%3Dihub)

### Age of the lithosphere from seismological analysis

- Poupinet, G., Shapiro, N.M. Worldwide distribution of ages of the continental lithosphere derived from a global seismic tomographic model, Lithos, 109 (2009), pp. 125-130, [doi.org/10.1016/j.lithos.2008.10.023](https://www.sciencedirect.com/science/article/pii/S0024493708002582?via%3Dihub)

### Hot spots list

- [http://www.mantleplumes.org/P%5E4/P%5e4Chapters/MorganP4ElectronicSupp1.pdf](http://www.mantleplumes.org/P%5E4/P%5e4Chapters/MorganP4ElectronicSupp1.pdf)
- Morgan, W.J. and Morgan, J.P. Plate velocities in the hotspot reference frame, Plates, Plumes and Planetary Processes, Gillian R. Foulger, Donna M. Jurdy, (2007), [doi.org/10.1130/2007.2430(04)](https://pubs.geoscienceworld.org/gsa/books/book/618/chapter/3805271/Plate-velocities-in-the-hotspot-reference-frame)

## License

The source code and data assets are under the following licenses:

    script: MIT. (LICENSE)
    data:
        thermodyn: CC-BY-4.0 (LICENSE)
        topography: Data from external sources (described in Datasets section)

For a full description, please visit the README and LICENSE files of each package in the corresponding package folders.

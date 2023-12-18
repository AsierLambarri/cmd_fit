# cmd_fit
Code generated for the 'Galaxy formation and Evolution' course at UCMs Astrophysics Master.

## The idea
The characteristics of a CMD can be easily picked with a quick look: a long MS means ongoing star-formation, wide turning-points mean either long SFR periods or variations in the chemical composition, populated RGB and AGB branches mean moderate-age populations while BL stars are a rign of young populations, and RR Lyrae of old populations. For a more precise estimation of the Star Formation and Chemical Evolution of the target population, carefull analysis of the CMD is needed. Using IAC-Star (Aparicio & Gallart, 2004) synthetically generated CMDs (or any other synthetically generated CMDs), resolved stellar populations can be preciselly characterized by fitting the CMD of the whole stellar population to these synthetic CMDs.

The fit is performed by star counting, as suggested by Aparicio & Hidalgo (2009); characteristic regions of the CMD can be selected _a la carte_ or the whole CMD can be selected at once. The second option is easier, but selecting _a la carte_ regions yields better results if low star density regions are avoided. For example, after visual inspection one might decide to select regions aroung the Main Sequence, Red Giant Branch, Asymptotic Gian Branch and Red Clump, which are the main characteristics of a CMD and contain (normally) most of the stars in it. Subdividing the regions into n x m bins gives greater accuracy. The quality of the fit is given by an appropriate merit function (Mighell 1999): the merit function is computed to be a weighted sum of the squares of the residuals of each bin, over all the regions (if no bins are created, the sum of the residuals is performed over the raw regions).

## The code
Several functions are provided in the different .py files that can be combined in a simple python script to analyze a given CMD:

**1.**: data_loader_iacSTAR.py contains a function to load IAC-Star data correctly.

**2.**: bundles.py contains the function that returns the data in the desired region (RGB, AGB,...).

**3.**: bin_determination.py contains a function that applies Freedman-Diaconis rule (Freedman & Diaconis 1981) to determine optimum bin number for a region/bundle.

**4.**: chi_squared_models.py contains the Mighell 1999 merit function.

The recomended usage is as follows: 1) load the CMD. 2) visually inspect the CMD and decide which regions you want to select and if you want meshing. 3) define the boundaries of the regions. There is no real benefit on constructing complicated shape regions so only square/rectangular regions can be created (and, after all, you can combine a bunch of these to make more arbitrary shapes). The regions must be defined by providing the x_range and y_range in a (2,2) array, i.e.: box_AGB = [[xmin,xmax],[ymin,ymax]]. 4) compute the chi_squared for a bunch of synthetic CMDs and determine best fit.

Notice that the aim is not to produce an automated program, but one that needs human input and benefits from it to obtain the best results possible: the number, placement and size of the regions to be selected is a purely human choice, as well as whether to create a mesh inside each one of them or not. Also, due to the fact that IAC-Star cannot be queried remotely, the synthetic CMDs need to be pre-downloaded.

The dependencies are: numpy, pandas and scipy.


An example program is provided in a jupyter-notebook, whith which the following results have been obtained.

## Some results

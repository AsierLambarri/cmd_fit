# cmd_fit
Code generated for the 'Galaxy formation and Evolution' course at UCMs Astrophysics Master.

## The idea
The characteristics of a CMD can be easily picked with a quick look: a long MS means ongoing star-formation, wide turning-points mean either long SFR periods or variations in the chemical composition, populated RGB and AGB branches mean moderate-age populations while BL stars are a rign of young populations, and RR Lyrae of old populations. For a more precise estimation of the Star Formation and Chemical Evolution of the target population, carefull analysis of the CMD is needed. Using IAC-Star (Aparicio & Gallart, 2004) synthetically generated CMDs (or any other synthetically generated CMDs), resolved stellar populations can be preciselly characterized by fitting the CMD of the whole stellar population to these synthetic CMDs.

The fit is performed by star counting, as suggested by Aparicio & Hidalgo (2009); characteristic regions of the CMD can be selected _a la carte_ or the whole CMD can be selected at once. The second option is easier, but selecting _a la carte_ regions yields better results if low star density regions are avoided. For example, after visual inspection one might decide to select regions aroung the Main Sequence, Red Giant Branch, Asymptotic Gian Branch and Red Clump, which are the main characteristics of a CMD and contain (normally) most of the stars in it. Subdividing the regions into n x m bins gives greater accuracy. The quality of the fit is given by an appropriate merit function (Mighell 1999): the merit function is computed to be a weighted sum of the squares of the residuals of each bin, over all the regions (if no bins are created, the sum of the residuals is performed over the raw regions).

## The code
Several functions are provided in the different .py files:

*A

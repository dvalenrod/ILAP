# ILAP

This code implements the ILAP indicator presented in the following article:

Valencia-Rodríguez, D.C., Coello Coello, C.A. (2023). A Novel Performance Indicator Based on the Linear Assignment 
Problem. In: Emmerich, M., et al. Evolutionary Multi-Criterion Optimization. EMO 2023. Lecture Notes in Computer 
Science, vol 13970. Springer, Cham. https://doi.org/10.1007/978-3-031-27250-9_25

## Execution 
```shell
python3 run_indicator weights_file_name points_file_name
```

where weights_file_name is the name of the file that contains uniformly distributed weight vectors 
and points_file_name is the name of the file that contains the approximation set to evaluate.
Both files must be of the same dimension and have the same number of points. 

The repository contains some examples of these files. 
For instance, you can run:

```shell
python3 run_indicator.py weights/udh_3D_100.dat data/center_3D_100.dat
```

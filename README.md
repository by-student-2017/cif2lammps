# cif2lammps
## Authors

- Ryther Anderson

- By STUDENT (Minor changes and additions)

## Motivation
cif2lammps is a Python 2 or 3 program used to convert crystals (developed initially for metal-organic frameworks) to Large-scale Atomic Molecular Massively Parallel Simulator (LAMMPS) format. 

## Current Status
cif2lammps can be used to convert ToBaCCo (https://github.com/tobacco-mofs/tobacco_3.0) generated and most other cifs to LAMMPS data. Currently, the generic force fields UFF, UFF4MOF, and Dreiding are implemented.
The MZHB (zeolite specific) and ZIF-FF (ZIF specific) force fields are also available. ZIF-FF uses the Generalized Amber Force Field (GAFF) for interactions
not explicitly parameterized, so there is also a preliminary version of GAFF for use with ZIF-FF (which does not include all the atom types seen in GAFF). 
UFF4MOF has the most robust atom typing functionality, based on connectivity and geometry. More force fields and the option to use custom force fields will be added. 
Keep in mind this is the first version of the code, and I (Ryther) wrote it quite quickly, it is becoming more useful/general, but be aware that it may need to be adapted for specific usage cases. 

## Installation (miniconda on Ubuntu 22.04 LTS or WSL2)
```
conda deactivate
conda remove -n cif2lammps_env --all
conda create -y -n cif2lammps_env python=3.8
conda activate cif2lammps_env
conda install -y networkx>=2.5
conda install -y ase==3.20.1
conda install -y pymatgen==2021.3.3
git clone https://github.com/rytheranderson/cif2lammps.git
```

## Usage
Get cif file from https://github.com/numat/RASPA2/tree/master/structures/mofs/cif and cif file in cifs directory.
- very simple command
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --outdir ./../unopt_lammps_data --read_cifs_pymatgen
```
- UFF4MOF
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field UFF4MOF --outdir ./../unopt_lammps_data --read_cifs_pymatgen --replication 2x2x2
```
- Dreiding
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field Dreiding --outdir ./../unopt_lammps_data --read_cifs_pymatgen --replication 2x2x2
```
- UFF
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field UFF --outdir ./../unopt_lammps_data --read_cifs_pymatgen --replication 2x2x2
```
- ZIF-FF (I haven't been able to fix the code yet.)
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field ZIFFF --outdir ./../unopt_lammps_data --read_cifs_pymatgen --charge --replication 2x2x2
```

## Help
```
python3 main_conversion.py -h
```

## Usage
Generally speaking just run:
```
python main_conversion.py --cifs directory_of_cifs
```
where "directory_of_cifs" is a directory with the cifs you want to convert. By default, this will convert the cifs serially and add the data and in files to a new directory called unopt_lammps_data. The options currently are:
```
--parallel
```
This switches ON parallel conversion.
```
--force_field UFF4MOF
```
Determines the force field to be used. The generic force fields UFF, UFF4MOF, and Dreiding are available (UFF4MOF has the most robust atom typing). The MZHB (zeolite specific) and ZIFFF (ZIF specific) force fields are also available. Note that ZIFFF requires the Generalized Amber Force Field (GAFF) to be used for all interactions not explicitly parameterized. Therefore, I have implemented a preliminary version of GAFF useable with ZIF-FF. This preliminary version does not cover all carbon, nitrogen, hydrogen, or sulfur atom types available in GAFF (requires complex typing given the diversity of types for these elements in GAFF). In addition, GAFF expects all atoms to have partial charges assigned using HF/6-31g* RESP, so add these to the CIF before using my ZIF-FF implementation (except for the case of ZIF-8, for which charges can be automatically assigned).
```
--small_molecule_force_field TraPPE
```
The force field to use for any small molecules that are detected (less than 10 atoms).
```
--outdir some_path
```
This will change the output location to the specified path.
```
--charges 
```
This flag switches charges ON, this means the pair_style and such will be updated to include electrostatic interactions. The default is False. Only set to True if the the region atom_site_charge is in your cif file(s).
```
--replication [QxRxS | min_atoms:N ]
```
The CIF cell will be replicated to the shape QxRxS or to have atleast N atoms, in the latter case the most cubic possible shape is used.
```
--read_cif_pymatgen
```
Switches ON reading the inputs CIFs using pymatgen i/o. This can be used to read most CIF formats. The bond topology will also be determined using the Atomic Simulation Environment (ASE).
Keep in mind that this might not work as expected in all cases. Bonds are typed in this scheme according to length, which also may not work as expected (use with caution).
```
--add_molecule molname,model,N
```
Used to add write molecule file and include this molecule in the main simulation. Molname is the name of the molecule, which must be included in small_molecule_constants.py, model is the name of the model (e.g. TraPPE, this allows multiple models to be implemented for the same molecule), and N is the number of molecules to insert into the system (can be 0).
```
--small_molecule_file file
```
The name of a file (currently only RASPA pdb format is supported) containing an initial configuration of small molecules, which are added into the provided CIF(s). The molecules are assigned force field parameters according to small_molecule_force_field. Bonds are automatically calculated.
## Requirements
Anaconda convers all the basic requirements. If you intend to use the --read_cif_pymatgen option you will also need to install pymatgen and the Atomic Simulation Environment (ASE). 
Install instructions for pymatgen can be found here: https://pymatgen.org/installation.html.
Install instructions for ASE can be found here: https://wiki.fysik.dtu.dk/ase/install.html.

## References
[1] Park, H., Yan, X., Zhu, R. et al. A generative artificial intelligence framework based on a molecular diffusion model for the design of metal-organic frameworks for carbon capture. Commun Chem 7, 21 (2024). https://doi.org/10.1038/s42004-023-01090-2 (Open Access)

## For Minor changes and additions and Acknowledgment
- This project (modified version) is/was partially supported by the following :
  + ATSUMITEC Co., Ltd.

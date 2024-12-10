# cif2lammps
## Authors

- Ryther Anderson (original: https://github.com/rytheranderson/cif2lammps.git)

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
conda remove -y -n cif2lammps_env --all
conda create -y -n cif2lammps_env python=3.8
conda activate cif2lammps_env
conda install -y networkx>=2.5
conda install -y ase==3.20.1
conda install -y pymatgen==2021.3.3
git clone https://github.com/by-student-2017/cif2lammps.git
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
- ZIF-FF (The crucial Zn parameter is missing.)
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field ZIFFF --outdir ./../unopt_lammps_data --read_cifs_pymatgen --charge --replication 2x2x2
```
- MZHB (Zeolite) (The parameters are also not yet established.)
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field MZHB --outdir ./../unopt_lammps_data --read_cifs_pymatgen --charge --parallel
```
- UFF4MOF + H2O (Not recommended) (Note: TIP4P_cutoff, TIP4P_2005_cutoff, TIP4P_2005_long, TIP3P_long)
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field UFF4MOF --outdir ./../unopt_lammps_data --read_cifs_pymatgen --replication 1x1x1 --add_molecule H2O,TIP4P_cutoff,1
```
- UFF4MOF + MX2 molecule (TraPPE type) (e.g., CO2)

It is recommended to use a cif file with charge as close to 0 as possible.
Molecules (parameters) confirmed in papers, etc.: O2, N2, H2, H2S, H2O, CO2, NO2, SO2. Unconfirmed molecules: F2, Cl2, H2Se, H2Te, ClO2, SF2, PCl2, PF2, CN2 (see "small_molecule_constants.py")
```
conda activate cif2lammps_env
cd cif2lammps
python3 main_conversion.py --cifs ./../cifs --force_field UFF4MOF --outdir ./../unopt_lammps_data --read_cifs_pymatgen --replication 1x1x1 --add_molecule CO2,TraPPE,30
```
- Carbon dioxide (CO2) has a critical point of 31.1°C and 7.38 MPa. Above this critical point, CO2 becomes a supercritical fluid, and the distinction between liquid and gas disappears.
- I have not yet modified it to use both "--charge" and "--add_molecule". This will take a lot of time, and I need to prepare parameters for LJ without Coulomb interaction to explicitly add Coulomb interaction.

## Help
```
python3 main_conversion.py -h
```

## Current known issues
- If you do not add the option "--read_cifs_pymatgen", no file will be output.
- A cif file that does not have an occupancy count of 1 must be rewritten so that the occupancy count is 1 at each site and the average occupancy count is also 1.
- "Zeolite temperated carbon (ZTC)" fails as "Killed" after a long calculation. Zeolite and other compounds have the same problem.
- The original code does not properly create input files for lammps in COF etc. In the MIL series, non-zero charges are listed in the cif file. When charges are taken into account in UFF, UFF4MOF or Dreiding, the initial structure shrinks abnormally, so the Coulomb force considering the charges is probably being calculated twice.
- To address these issues, the code and parameters need to be rewritten. Note that reference [1] is for MOF, not COF etc. There is still a lot of room for research. RASPA (or RASPA2) code is a useful code, but it is not all-purpose. It works well from vacuum to atmospheric pressure. However, at 10 MPa or 70 MPa, the structure of organic matter shrinks. In addition, it is important to note that although it is GCMC, it is not MD. This is the reason why the predictions differ from the real world, and there is room for research on these points as well.
- Unless it is stated that the parameters have been optimized by adding charges to UFF, UFF4MOF, or Dreiding and taking into account Coulomb forces, it is best not to trust reports that show formulas calculated by adding Coulomb forces. Adding Coulomb forces that take charge into account to such a force field means that the Coulomb forces are being calculated twice. (see "examples/MIL-100_UFF4MOFF_charge_failed")
- Since the grand potential takes pV into account, when parameters are used that cause the initial structure to shrink (or expand) abnormally when the Coulomb force is explicitly included and calculations are performed at room temperature and pressure, it is clear that the results of the Grand Canonical Monte Carlo (GCMC) method cannot be trusted.
- Of course, there is no disagreement that the accuracy of predictions of adsorption phenomena affected by charge (Coulomb forces), such as CO2, is improved when parameters are optimized taking these issues into account. 
- In [1], RASPA is used, but GCMC in Lammps requires input of chemical potential. I use the HOMO energy of MOPAC (the chemical potential at 0 K corresponds to the Fermi energy in DFT. It is important to note that MOPAC parameters are optimized for data at 25 degrees or room temperature).


## Charge
In docking calculations (sievgene) of 132 protein-compound complexes, the correct structure was obtained with a probability of 56% (accuracy 2 [A]) using RHF/6-31G* and RESP, which was only 2-3% lower for MOPAC AM1 charge and only 5% lower for Gasteiger charge. Even in small-scale drug screening experiments of about 10,000 compounds, the hit rate was better with more accurate charge, but the Gasteiger charge was only a few percent lower. [2]
- PACMOF: https://github.com/arung-northwestern/pacmof
- MOPAC: https://github.com/openmopac/mopac (Recent open source versions can also handle periodic structures.) (Japanese paper: https://doi.org/10.5571/synth.2.60) (In the UCSF Chimera code, it has been used for proteins as AM1-bcc and has a proven track record.)
- Gasteiger method (RDKit): https://www.rdkit.org/docs/source/rdkit.Chem.rdPartialCharges.html
- Psi4: https://psicode.org/ (Dr. Y. Hayashi (, who is the developer of Xenonpy.) of the Institute of Statistical Mathematics is using it in polymers. I don't know if it can be used in periodic structures.)


## MIL-47: charge equilibration vs. DFT-derived charges [3] and PM7 (MOPAC)
MOPAC became open source from the 2016 version, and it is now possible to calculate periodic structures (using Tv) free of charge.
| type | V0+      | V2+      | V4+      | DFT [3]  | PM7  |
|------|----------|----------|----------|------|------|
| V    | 2.67677  | 1.45833  | 1.83592  | 1.68 | 1.72 |
| O1   | -0.986909| -0.527963| -0.661157| -0.6 | -0.81|
| O2   | -0.712381| -0.439958| -0.516643| -0.52| -0.51|
| O3   | -0.693279| -0.427135| -0.501819| -0.52| -0.52|
| C1   | 0.00680379| -0.0146643| -0.0110838| -0.15| -0.12|
| H1   | 0.0434488| 0.0574796| 0.055858 | 0.12 | 0.15 |
| C2   | 0.0116383| -0.0118276| -0.00782077| -0.15| -0.12|
| H2   | 0.0444475| 0.0586772| 0.0570134| 0.12 | 0.15 |
| C3   | -0.150672| -0.0720208| -0.083311| 0.0  | -0.04|
| C4   | 0.605064 | 0.384265 | 0.420426 | 0.56 | 0.56 |


## Installation (Lammps)
1. LAMMPS Windows Installer Repository (http://packages.lammps.org/windows.html) -> LAMMPS Binaries Repository: ./legacy/admin/64bit (https://rpm.lammps.org/windows/legacy/admin/64bit/index.html)
2. LAMMPS-64bit-22Dec2022-MSMPI-admin.exe (https://rpm.lammps.org/windows/legacy/admin/64bit/LAMMPS-64bit-22Dec2022-MSMPI-admin.exe)
- LAMMPS Windows Installer Repository -> legacy -> admin -> 64bit -> LAMMPS-64bit-22Dec2022-MSMPI-admin.exe
- The options available for GCMC vary depending on the version of lammps. The above version is used for testing GCMC calculations.

## Microsoft MPI
1. Microsoft MPI v10.1.2 (https://www.microsoft.com/en-us/download/details.aspx?id=100593)


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
--read_cifs_pymatgen
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
[2] Y. Fukunishi et al., Synthesiology 2 (2009) 60-68.: https://doi.org/10.5571/synth.2.60 (Open Access, Japanese)  
[3] D. Dubbeldam et al., "RASPA 2.0: Molecular Software Package for Adsorption and Diffusion in (Flexible) Nanoporous Materials" (2020).: https://iraspa.org/raspa/
[4] T. Ohmameuda, The Gunma-Kosen Review 40 (2022) 51-58.: https://doi.org/10.51030/krev.40.0_51 (Open Access, Japanese)  


## For Minor changes and additions and Acknowledgment
- This project (modified version) is/was partially supported by the following :
  + ATSUMITEC Co., Ltd.


## Other information
None of the following installations worked properly without "--read_cifs_pymatgen". For ZIF-FF, there is a problem where integers in the data file become symbols (characters) containing information about the corresponding elements.
- Installation (ubuntu 22.04 LTS or WSL2, Python 3.7 version)
```
conda deactivate
conda remove -y -n cif2lammps_env --all
conda create -y -n cif2lammps_env python=3.7
conda activate cif2lammps_env
conda install -y networkx>=2.5
conda install -y ase==3.20.1
conda install -y pymatgen==2021.3.3
git clone git clone https://github.com/by-student-2017/cif2lammps.git
```
- Installation (ubuntu 22.04 LTS or WSL2, Python 3.8 version)
```
conda deactivate
conda remove -y -n cif2lammps_env --all
conda create -y -n cif2lammps_env python=3.8
conda activate cif2lammps_env
conda install -y networkx>=2.5
conda install -y ase==3.20.1
conda install -y pymatgen==2021.3.3
git clone git clone https://github.com/by-student-2017/cif2lammps.git
```
- Installation (ubuntu 22.04 LTS or WSL2, Python 3.9 version)
```
conda deactivate
conda remove -y -n cif2lammps_env --all
conda create -y -n cif2lammps_env python=3.9
conda activate cif2lammps_env
conda install -y networkx>=2.5
conda install -y ase==3.20.1
conda install -y pymatgen==2022.0.8
git clone git clone https://github.com/by-student-2017/cif2lammps.git
```
- It seems that the ImportError occurs because the gcd function has been removed from the fractions module in Python 3.10 and later. Instead, you need to use the gcd function from the math module, so you will need to rewrite your code. 

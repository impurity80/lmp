
from ase import Atoms, Atom
from ase.calculators.lammpsrun import LAMMPS
from ase.visualize import view

a = [6.5, 6.5, 7.7]
d = 2.3608
NaCl = Atoms([Atom('Na', [0,0,0]), Atom('Cl', [0,0,d])], cell=a, pbc=True)

calc = LAMMPS()
NaCl.set_calculator(calc)

view(NaCl)

# print NaCl.get_total_energy()

# print(NaCl.get_stress())

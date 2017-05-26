#/usr/bin/env python

import sys
import f90nml
sys.path.insert(1, '../flint/')
from flint.project import Project

rootdir = sys.argv[1]

src = Project()
src.parse(rootdir)

# print(src.files[0].units[0].variables[0])
# print(src.files[0].units[0].namelists)

nmlfile = sys.argv[2]

nml = f90nml.read(nmlfile)

for file in src.files:
    for unit in file.units:
        for nmlname in unit.namelists:
            if nmlname in nml:
                # print("Found namelist {}".format(nmlname))
                for var in nml[nmlname]:
                    if var not in unit.namelists[nmlname]:
                        print("Variable {} missing from namelist {} in {}".format(var,nmlname,file.path))
                    else:
                        pass
                        # print("Found {} variable in {}".format(var,file.path))
            else:
                print("Not found namelist {}".format(nmlname))

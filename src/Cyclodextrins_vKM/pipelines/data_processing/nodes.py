import autode as ade
orca = ade.methods.ORCA()
import numpy as np

def ConvertMol(x):
    Solvent = input('If you got a solvent give us the name here if not just hit enter: ')
    if Solvent == '':
        Solvent = None
    xnew = x.decode("utf-8")
    with open('Molecule.xyz','w') as XYZfile:
        XYZfile.write(xnew)

    MoI = ade.Molecule('Molecule.xyz', solvent_name=Solvent)

    XYZfile.close()
    return(MoI)

def OptimizeMol(MoI):
    print(MoI)
    MoI.optimise(method=ade.methods.XTB())
    return(MoI)

def CalculateMol(MoI):
    NoC = input('How many cores do you have/want to use if you only have 1 hit enter: ')
    if NoC == '':
        NoC = 1
    CoI = ade.Calculation(name=MoI.name,molecule=MoI,method=orca,keywords=orca.keywords.hess,n_cores=NoC)
    CoI.output.filename = MoI.name+'.out'
    return(CoI)

def GetGibbsMol(MoI,CoI):
    MoI.calc_thermo(calc=CoI)
    print(f'G = {MoI.free_energy:.6f} Ha')
    GibbsE = MoI.free_energy
    return(GibbsE)

def GetPka(GibbsE):
    GibbsEkJpM = 2600*GibbsE
    R = 0.008314
    T = input("What's the Temperature(if you give nothing it will be 273.15K): ")
    if T == '':
        T = 273.15
    LnK = GibbsEkJpM/(-1*R*T)
    K = np.exp(LnK)
    pKa = -1*np.log10(K)
    print(f'pKa = {pKa}')
    return(pKa)
from unicodedata import name
from black import out
from kedro.pipeline import Pipeline, node
from .nodes import ConvertMol, OptimizeMol, CalculateMol, GetGibbsMol, GetPka
def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(func=ConvertMol, inputs='Butane_xyz', outputs='Butane_Molecule', name='Create Molecule'),
            node(func=OptimizeMol, inputs='Butane_Molecule', outputs='Butane_Molecule', name='Optmize Molecule'),
            node(func=CalculateMol, inputs='Butane_Molecule', outputs='Butane_Calculation',name='Single Point Calc'),
            node(func=GetGibbsMol, inputs=['Butane_Molecule','Butane_Calculation'], outputs='GibbsE', name='Get Gibbs'),
            node(func=GetPka, inputs='GibbsE',outputs='pKa',name='Get pKa')
        ]
    )
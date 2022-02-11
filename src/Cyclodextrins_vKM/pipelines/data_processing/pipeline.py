from unicodedata import name
from black import out
from kedro.pipeline import Pipeline, node
from .nodes import ConvertMol, OptimizeMol, CalculateMol, GetGibbsMol, GetPka
def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(func=ConvertMol, inputs='Butane_xyz', outputs='Molecule', name='Create_Molecule'),
            node(func=OptimizeMol, inputs='Molecule', outputs='Molecule_opt', name='Optmize_Molecule'),
            node(func=CalculateMol, inputs='Molecule_opt', outputs='Calculation',name='Single_Point_Calc'),
            node(func=GetGibbsMol, inputs=['Molecule_opt','Calculation'], outputs='GibbsE', name='Get_Gibbs'),
            node(func=GetPka, inputs='GibbsE',outputs='pKa',name='Get_pKa')
        ]
    )
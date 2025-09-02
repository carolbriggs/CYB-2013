''' Simple Unit Tests for gs.py '''

import pytest
from gs import gs, gs_block, gs_tie

themen = ['xavier','yancey','zeus']
thewomen = ['amy','bertha','clare']

thepref = {'xavier': ['amy','bertha','clare'],
        'yancey': ['bertha','amy','clare'],
        'zeus': ['amy','bertha','clare'],
        'amy': ['yancey','xavier','zeus'],
        'bertha': ['xavier','yancey','zeus'],
        'clare': ['xavier','yancey','zeus']
        }
thepreftie = {'xavier': [{'bertha'},{'amy'},{'clare'}],
        'yancey': [{'amy','bertha'},{'clare'}],
        'zeus': [{'amy'},{'bertha','clare'}],
        'amy': [{'zeus','xavier','yancey'}],
        'bertha': [{'zeus'},{'xavier'},{'yancey'},],
        'clare': [{'xavier','yancey'},{'zeus'}]
        }
    
m1 = ['alan','brad','charlie','david']
w1 =  ['alice','beth','catherine','denise']
p1 = {'alan':['beth','catherine','alice','denise'],
        'brad':['beth','denise','alice','catherine'],
        'charlie':['catherine','alice','beth','denise'],
        'david':['alice','beth','catherine','denise'],
        'alice':['alan','charlie','david','beth'],
        'beth':['charlie','alan','brad','david'],
        'catherine':['charlie','alan','brad','david'],
        'denise':['david','charlie','alan','brad']
}

p1tie = {'alan':[{'beth','catherine'},{'alice'},{'denise'}],
        'brad':[{'beth'},{'denise'},{'alice','catherine'}],
        'charlie':[{'catherine','alice'},{'beth'},{'denise'}],
        'david':[{'alice'},{'beth','catherine'},{'denise'}],
        'alice':[{'alan'},{'charlie'},{'david'},{'beth'}],
        'beth':[{'charlie','alan','brad'},{'david'}],
        'catherine':[{'charlie'},{'alan'},{'brad'},{'david'}],
        'denise':[{'david'},{'charlie','alan'},{'brad'}]
}

#print(gs(m1,w1,p1))
blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}
blocked2 = [('brad','beth'),('catherine','alan')]

#print(gs_tie(m1,w1,p1tie))
print(gs_block(m1,w1,p1,blocked2))
def test_gs():

    assert gs(themen,thewomen,thepref) == {'amy': 'xavier', 'clare': 'zeus', 'bertha': 'yancey'}

def test_gs2():
    assert gs(m1,w1,p1) == {'beth': 'alan', 'alice': 'david', 'catherine': 'charlie', 'denise': 'brad'}

def test_gsblock():
    assert gs_block(themen,thewomen,thepref,blocked) == {'amy': 'xavier', 'bertha': 'yancey'}

def test_gsblock2():
    assert gs_block(m1,w1,p1,blocked2) == {'catherine': 'charlie', 'alice': 'david', 'beth': 'alan', 'denise': 'brad'}

def test_gstie():
    m = gs_tie(themen,thewomen,thepreftie)
    correct_match = {'amy': 'zeus', 'clare': 'yancey', 'bertha': 'xavier'}
    correct_match2 = {'amy': 'xavier', 'bertha': 'zeus', 'clare': 'yancey'}
    correct_match3 = {'bertha': 'zeus', 'amy': 'yancey', 'clare': 'xavier'}
    correct_match4 = {'amy': 'yancey', 'bertha': 'xavier', 'clare': 'zeus'}
    assert m in [correct_match,correct_match2,correct_match3,correct_match4]

def test_gstie2():
    m = gs_tie(m1,w1,p1tie)
    correct_match = {'alice': 'charlie', 'beth': 'alan', 'denise': 'brad', 'catherine': 'david'}
    correct_match2 = {'alice': 'alan', 'beth': 'brad', 'catherine': 'charlie', 'denise': 'david'}
    correct_match3 = {'alice': 'david', 'catherine': 'charlie', 'beth': 'alan', 'denise': 'brad'}
    correct_match4 = {'alice': 'charlie', 'beth': 'brad', 'catherine': 'alan', 'denise': 'david'}
    assert  m in [correct_match,correct_match2,correct_match3,correct_match4]
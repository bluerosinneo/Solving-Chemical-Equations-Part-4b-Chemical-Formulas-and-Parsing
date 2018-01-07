# This code follows the following post.
# http://cramerexplainsmath.com/2018/01/07/solving-chemical-equations-part-4b-chemical-formulas-and-parsing/
# @desc This is a driver file for chemicalFormula.
# A detailed description can be found in the post
# @author Cramer Grimes cramergrimes@gmail.com

from chemicalFormula import chemicalFormula

myFormula = chemicalFormula()

formulaText = "K3[Fe(C2O4)3].3H2O"

myFormula.readFormula(formulaText,1)

print myFormula.elementDict
print myFormula.origFormula


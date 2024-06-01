from ast import List
from AST import construir_arbol_postfix, graficar_arbol,obtener_alfabeto,evaluate_tree,graficar_pos
from AnalizadorLexico import AnalizadorDeLexemas
from Posfix import PostFix
from AFD import afd_directo,reconocer_cadena,AFD,renderAfd
#Realizar las conversiones
tokens = set()
AFDs = {}
AFDl = ["Coment","Variable","Rules"]
with open("./PostfixData.txt",encoding="utf-8") as f:
    for i, line in enumerate(f):
        expresion_infix = line.strip()
        expresion_infix_direct = "(" + expresion_infix + ')#'
        #afd directo
        expresion_postfix_direct = PostFix(expresion_infix_direct)
        
        arbol_root_direct = construir_arbol_postfix(expresion_postfix_direct)
        # graficar_arbol(arbol_root_direct)
        alfabeto = evaluate_tree(arbol_root_direct)
        # graficar_pos(arbol_root_direct)
        afd_direct = afd_directo(arbol_root_direct)
        AFDs[AFDl[i]] = AFD(afd_direct,alfabeto)
analizador = AnalizadorDeLexemas("./slr-3.yal", "./PostfixData.txt")

# Iniciar el análisis léxico
analizador.analizar()
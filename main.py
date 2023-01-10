import numpy as np
lst_datos=['112|CampoBolivar|0-2|97', '116|CampoZamora|3-0|86', '117|CampoTungurahua|4-3|101','119|CampoPastaza|2-1|78']
def ubicarCamposPetroleros(lst_campos):
    m_campos= np.zeros((5, 5), int)
    m_cantidades= np.zeros((5, 5), int)
    for i in range(len(lst_campos)):
        l=lst_campos[i].split("|")
        coordenada=l[2].split("-")
        x=int(coordenada[0])
        y=int(coordenada[1])
        m_cantidades[x, y] = int(l[-1])
        m_campos[x, y]=int(l[0])
    return m_campos,m_cantidades
def codigosCampos(M_codigos, M_barriles, cantidad):
    v_bool1=M_barriles<cantidad
    v_bool2=M_barriles!=0
    v_bool=v_bool1==v_bool2
    v_cod=M_codigos[v_bool]
    print("Cantidad={}; los codigos serian {}".format(cantidad,v_cod))
def ReporteArea(M_barriles, puntoInicio=[0,1], puntoFinal=[3,3]):
    f1=puntoInicio[0]
    f2=puntoFinal[0]
    c1=puntoInicio[1]
    c2=puntoFinal[1]
    m=M_barriles[f1:f2+1,c1:c2+1]#debido a que el slicing no considera el intervalo final
    total=m.sum()
    n_campos=(m!=0).sum()
    print("Entre los dos puntos hay {} campos y suman un total de {}".format(n_campos,total))
cantidad=int(input("Ingrese un valor"))
m_campos,m_cantidades=ubicarCamposPetroleros(lst_datos)
print(m_campos)
print(m_cantidades)
codigosCampos(m_campos,m_cantidades, cantidad)
ReporteArea(m_cantidades,[0,0],[3,1])





for posk in posMTotals:
            montTotal =page_content[posk+5:posk+13].strip()
            #print(numDocuments)
            #print(f"monto: {montTotal}")
            #print(f"len: {len(montTotal)}")
            #print(buscar_Indices(montTotal,"."))
            #html="<tr><td>"+l+"</td><td>BOLETA</td><td>"+numDocuments+"</td><td> "+tipoMoneda+"</td><td>" + limpiar_Monto_Total(montTotal,".")+"</td></tr>"
            #print(NumberDoc)
            x="<tr><td>"+l+"</td><td>BOLETA</td><td>"+numDocuments+"</td><td> "+tipoMoneda+"</td><td>" + limpiar_Monto_Total(montTotal,".")+"</td></tr>"
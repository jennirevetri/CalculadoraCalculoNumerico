import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors, TextStyle,FontWeight
import numpy as np





def main(page: Page):

    page.title = "Calculadora de Ecuaciones"

    #text fields de Sistema de Ecuacion
    e1=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e2=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e3=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e4=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e5=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e6=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e7=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e8=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e9=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e10=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e11=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    e12=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    eR1 = ft.Text("X=",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    eR2 = ft.Text("Y=",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    eR3 = ft.Text("Z=",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    ex = ft.Text("X+ ",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    ey = ft.Text("Y+ ",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    ez = ft.Text("Z= ",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    

    #text fields de matriz
    elemento1=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento2=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento3=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento4=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento5=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento6=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento7=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento8=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento9=ft.TextField(label="",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    respuesta1 = ft.Text("Autovector1=         Autovalor1=",color="#1a2e41",size=14,font_family="Consolas")
    respuesta2 = ft.Text("Autovector2=         Autovalor2=",color="#1a2e41",size=14,font_family="Consolas")
    respuesta3 = ft.Text("Autovector3=         Autovalor3=",color="#1a2e41",size=14,font_family="Consolas")


    #text fields de interpolacion
    x1=ft.TextField(label="x1",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    y1=ft.TextField(label="y1",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    x2=ft.TextField(label="x2",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    y2=ft.TextField(label="y2",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    x3=ft.TextField(label="X",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    resultado=ft.Text("Interpolacion del elemento desconocido= ",color="#1a2e41",size=14,font_family="Consolas")

    def route_change(e):
        ventanaMenu()  
        if page.route == "/ecuaciones":
            ventanaEcuaciones()
           
        elif page.route == "/autovector":
            ventanaAutoVector()
           

        elif page.route == "/interpolacion":
            ventanaInterpolacion()
        page.update()
    
    def ventanaMenu():
        page.views.clear()
        page.views.append(
            
            View(
                "/",
                [
                    AppBar(title=Text("CALCULO NUMERICO",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                     
        ft.Column(
            [    
                 ft.ElevatedButton(text="SISTEMA DE ECUACIONES",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=100,width=400,on_click=lambda _: page.go("/ecuaciones")),
                 ft.ElevatedButton(text="AUTOVALOR Y AUTOVECTOR ",bgcolor ="#1a2e41" , color = "#D9D9D9",height=100,width=400, on_click=lambda x: page.go("/autovector")),
                 ft.ElevatedButton(text="INTERPOLACION",bgcolor ="#1a2e41" , color = "#D9D9D9",height=100,width=400, on_click= lambda x: page.go("/interpolacion"))
            ],spacing=50
            
        )  
    
                ],
            vertical_alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,bgcolor="#9BA5B7"
            )
            
        )

    def ventanaEcuaciones():
        page.views.append(
                View(
                    "/ecuaciones",
                    [
                        AppBar(title=Text("Calculo Numerico: Sistema de Ecuaciones lineales 3x3",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                        ft.Row([
                            ElevatedButton("Volver",color="#D9D9D9",bgcolor="#1a2e41", on_click=lambda _: page.go("/")),
                            ft.Container(Text("Sistema de Ecuaciones Lineales",color="#D9D9D9",font_family="Consolas",size=15),bgcolor="#1A2E41",border_radius = 10,width=300,height=80,alignment=ft.alignment.center)
                            
                    ],spacing=382)
,
                        ft.Column([
                            
                            
                            
                            ft.Container(
                                ft.Column([
                                    ft.Row([ft.Text("Ingrese los coeficientes del sistema",color="#1a2e41",font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([e1,ex,e2,ey,e3,ez,e4],spacing=10,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([e5,ex,e6,ey,e7,ez,e8],spacing=10,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([e9,ex,e10,ey,e11,ez,e12],spacing=10,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.ElevatedButton(text="RESOLVER ECUACION LINEAL",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=40,width=400,on_click= resolverEcuacion),
                                    ft.ElevatedButton(text="LIMPIAR",bgcolor ="#4C6B94" ,color = "#D9D9D9", height=40,width=200,on_click=limpiar),
                                    
                                ],spacing=15,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER),
                            alignment = ft.alignment.center,
                            width=400,
                            height=350,
                            bgcolor="#788BA7",
                            border_radius = 10,
                            padding=20
                        ),
                        ft.Container(
                            ft.Column([
                                    ft.Row([ft.Text("Resultados",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([eR1,eR2,eR3 ],spacing=30,alignment=ft.MainAxisAlignment.CENTER),
                                    
                                ],spacing=15),
                            width=400,
                            height=135,
                            bgcolor="#A5B5C9",
                            border_radius=10,
                            padding = 20
                        )
                    ])
                    

                    ],bgcolor="#9BA5B7", vertical_alignment = ft.MainAxisAlignment.CENTER,
                     horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )

    def ventanaAutoVector():
        page.views.append(
                View(
                    "/autovector",
                    [
                        AppBar(title=Text("Calculo Numerico: Autovector y Autovalor",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                        ft.Row([
                            ElevatedButton("Volver",color="#D9D9D9",bgcolor="#1a2e41", on_click=lambda _: page.go("/")),
                            ft.Container(Text("Solucion de Autovector y Autovalor",color="#D9D9D9",font_family="Consolas",size=15),bgcolor="#1A2E41",border_radius = 10,width=300,height=80,alignment=ft.alignment.center)
                            
                    ],spacing=382)
,
                        ft.Column([
                            
                            
                            
                            ft.Container(
                                ft.Column([
                                    ft.Row([ft.Text("Ingrese matriz a determinar su",color="#1a2e41",size=14,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text("autovector y autovalor",color="#1a2e41",size=14,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([elemento1,elemento2,elemento3],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([elemento4,elemento5,elemento6],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([elemento7,elemento8,elemento9],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.ElevatedButton(text="RESOLVER AUTOVECTOR Y AUTOVALOR",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=40,width=400,on_click=resolverVectores),
                                    ft.ElevatedButton(text="LIMPIAR",bgcolor ="#4C6B94" ,color = "#D9D9D9", height=40,width=200,on_click=limpiar),
                                    
                                ],spacing=15,horizontal_alignment = ft.CrossAxisAlignment.CENTER),
                            alignment = ft.alignment.center,
                            width=400,
                            height=350,
                            bgcolor="#788BA7",
                            border_radius = 10,
                            padding = 15,
                        ),
                        ft.Container(
                            ft.Column([
                                    ft.Row([ft.Text("Resultados",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([respuesta1]),
                                    ft.Row([respuesta2]),
                                    ft.Row([respuesta3]),
                                    
                                ],spacing=10),
                            width=400,
                            height=135,
                            bgcolor="#A5B5C9",
                            border_radius=10,
                            padding =15
                        )
                    ])
                    

                    ],bgcolor="#9BA5B7", vertical_alignment = ft.MainAxisAlignment.CENTER,
                     horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )

    def ventanaInterpolacion():
        page.views.append(
                View(
                    "/interpolacion",
                    [
                        AppBar(title=Text("Calculo Numerico: Interpolacion",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                        ft.Row([
                            ElevatedButton("Volver",color="#D9D9D9",bgcolor="#1a2e41",on_click=lambda _: page.go("/")),
                            ft.Container(Text("Solucion Interpolacion",color="#D9D9D9",font_family="Consolas",size=15),bgcolor="#1A2E41",border_radius = 10,width=300,height=80,alignment=ft.alignment.center)
                            
                    ],spacing=382)
,
                        ft.Column([
                            
                            
                            
                            ft.Container(
                                
                                ft.Column([
                                    ft.Row([ft.Text("Ingrese los cinco valores conocidos",color="#1a2e41",size=16,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([x1,y1],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([x2,y2],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([x3],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.ElevatedButton(text="RESOLVER POR METODO DE GAUSS",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=40,width=400,on_click=resolverInterpolacion),
                                    ft.ElevatedButton(text="LIMPIAR",bgcolor ="#4C6B94" ,color = "#D9D9D9", height=40,width=200,on_click=limpiar),
                                ],spacing=15,horizontal_alignment = ft.CrossAxisAlignment.CENTER),
                                width=400,
                                height=350,
                                bgcolor="#788BA7",
                                border_radius = 10,
                                padding=20,
                 
                                
                                
                            
                        ),
                        ft.Container(
                            ft.Column([
                                ft.Row([ft.Text("Resultados:",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([resultado],alignment=ft.MainAxisAlignment.CENTER),
                            ],spacing=20),
                            width=400,
                            height=135,
                            bgcolor="#A5B5C9",
                            border_radius=10,
                            padding=20,
                        )
                    ])
                    

                    ],bgcolor="#9BA5B7", vertical_alignment = ft.MainAxisAlignment.CENTER,
                     horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    def resolverEcuacion(e):
        X1= 0 if e1.value=="" else int(e1.value)
        Y1 = 0 if e2.value=="" else int(e2.value)
        Z1 = 0 if e3.value=="" else int(e3.value)
        B1 = 0 if e4.value=="" else int(e4.value)
        X2 = 0 if e5.value=="" else int(e5.value)
        Y2 = 0 if e6.value=="" else int(e6.value)
        Z2 = 0 if e7.value=="" else int(e7.value)
        B2 = 0 if e8.value=="" else int(e8.value)
        X3 = 0 if e9.value=="" else int(e9.value)
        Y3 = 0 if e10.value=="" else int(e10.value)
        Z3 = 0 if e11.value=="" else int(e11.value)
        B3 = 0 if e12.value=="" else int(e12.value)
        matriz = [[X1,Y1,Z1],[X2,Y2,Z2],[X3,Y3,Z3]]
        B = [B1,B2,B3]
        A = np.array(matriz)
        b = np.array(B)
        try:
            # Resolver el sistema de ecuaciones
            x = np.linalg.solve(A, b)
            eR1.value ="X= " + str(round(x[0],2))
            eR2.value ="Y= " + str(round(x[1],2))
            eR3.value ="Z= "+ str(round(x[2],2))
            page.update()
            
            
        except np.linalg.LinAlgError:
            eR1.value = "Sin solucion"
            eR2.value = ""
            eR3.value = ""
            
            page.update()
             
    def resolverVectores(e):
        elemento1R = 0 if elemento1.value=="" else int(elemento1.value)
        elemento2R = 0 if elemento2.value=="" else int(elemento2.value)
        elemento3R = 0 if elemento3.value=="" else int(elemento3.value)
        elemento4R= 0 if elemento4.value=="" else int(elemento4.value)
        elemento5R = 0 if elemento5.value=="" else int(elemento5.value)
        elemento6R = 0 if elemento6.value=="" else int(elemento6.value)
        elemento7R = 0 if elemento7.value=="" else int(elemento7.value)
        elemento8R = 0 if elemento8.value=="" else int(elemento8.value)
        elemento9R = 0 if elemento9.value=="" else int(elemento9.value)
        matriz = [[elemento1R,elemento2R,elemento3R],[elemento4R,elemento5R,elemento6R],[elemento7R,elemento8R,elemento9R]]
        A = np.array(matriz)

        try:
            # Resolver el sistema de ecuaciones
            autovalores, autovectores = np.linalg.eig(A)

            
            
            respuesta1.value = "v1= " + str(np.round(autovectores[0][0],2))+" " + str(np.round(autovectores[0][1],2))+ " "+ str(np.round(autovectores[0][2],2)) + "     λ1=" + str(np.round(autovalores[0],2))
            respuesta2.value = "v2= " + str(np.round(autovectores[1][0],2))+" " + str(np.round(autovectores[1][1],2))+ " "+ str(np.round(autovectores[1][2],2)) + "     λ2=" + str(np.round(autovalores[1],2))
            respuesta3.value = "v3= " + str(np.round(autovectores[2][0],2))+" " + str(np.round(autovectores[2][1],2))+ " "+ str(np.round(autovectores[2][2],2)) + "     λ3=" + str(np.round(autovalores[2],2))

            
            
            page.update()

        except np.linalg.LinAlgError as e:
            respuesta1.value = "Sin solucion"
            respuesta2.value = ""
            respuesta3.value= ""
            
            
        
            
            page.update()

    def resolverInterpolacion(e):
        valorx1 =  0 if x1.value=="" else int(x1.value)
        valorx2 =  0 if x2.value=="" else int(x2.value)
        valory1 =  0 if y1.value=="" else int(y1.value)
        valory2 =  0 if y2.value=="" else int(y2.value)
        valor5 =  0 if x3.value=="" else int(x3.value)

        x_conocidos = np.array([valorx1, valorx2])
        y_conocidos = np.array([valory1,valory2])
        x_desconocido = valor5
        
        try:
            y_interpolado = np.interp(x_desconocido, x_conocidos, y_conocidos)  
            resultado.value = "El valor interpolado de y en x =  " + str(x_desconocido)+ " es: " + str(y_interpolado)
            page.update()
        except Exception as e:
            resultado.value = "Sin solucion "
            
    
 
    def limpiar(e):
        e1.value = ""
        e2.value = ""
        e3.value = ""
        e4.value = ""
        e5.value = ""
        e6.value = ""
        e7.value = ""
        e8.value = ""
        e9.value = ""
        e10.value = ""
        e11.value = ""
        e12.value = ""
        eR1.value = ""
        eR2.value = ""
        eR3.value = ""

        elemento1.value = ""
        elemento2.value = ""
        elemento3.value = ""
        elemento4.value = ""
        elemento5.value = ""
        elemento6.value = ""
        elemento7.value = ""
        elemento8.value = ""
        elemento9.value = ""
        respuesta1.value = ""
        respuesta2.value = ""
        respuesta3.value = ""

        x1.value = ""
        x2.value = ""
        x3.value = ""
        y1.value = ""
        y2.value = ""
        resultado.value = ""


        page.update()

        


    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


if __name__ == "__main__":

    ft.app(main)

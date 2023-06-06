import json
from claseDocente import Docente
from clasePersonalApoyo import PersonalApoyo
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador

class Lista:
    def __init__(self):
        self.agentes = []

    def insertar_agente(self, posicion, agente):
        if posicion < 0 or posicion > len(self.agentes):
            raise ValueError("La posición dada no es válida para la inserción")
        self.agentes.insert(posicion-1, agente)

    def agregar_agente(self, agente):
        self.agentes.append(agente)

    def obtener_agente(self, posicion):
        if posicion < 0 or posicion >= len(self.agentes):
            raise IndexError("La posición dada no es válida para mostrar el elemento")
        return self.agentes[posicion-1]

    def cargar_desde_archivo(self, archivo):
        with open(archivo, "r", encoding="utf-8") as file:
            agentes_data = json.load(file)

        for agente_data in agentes_data:
            tipo_agente = agente_data["tipo_agente"]
            if tipo_agente == "Docente":
                docente = Docente(
                    agente_data["cuil"], 
                    agente_data["apellido"], 
                    agente_data["nombre"], 
                    agente_data["sueldo_basico"], 
                    agente_data["antiguedad"], 
                    agente_data["carrera"], 
                    agente_data["cargo"], 
                    agente_data["catedra"]
                    )
                self.agregar_agente(docente)

            elif tipo_agente == "PersonalApoyo":
                personal_apoyo = PersonalApoyo(
                    agente_data["cuil"], 
                    agente_data["apellido"], 
                    agente_data["nombre"], 
                    agente_data["sueldo_basico"], 
                    agente_data["antiguedad"], 
                    agente_data["categoria"]
                    )
                self.agregar_agente(personal_apoyo)

            elif tipo_agente == "Investigador":
                investigador = Investigador(
                    agente_data["cuil"], 
                    agente_data["apellido"], 
                    agente_data["nombre"], 
                    agente_data["sueldo_basico"], 
                    agente_data["antiguedad"],
                    agente_data["area_investigacion"], 
                    agente_data["tipo_investigacion"])
                self.agregar_agente(investigador)

            elif tipo_agente == "DocenteInvestigador":
                docente_investigador = DocenteInvestigador(
                    agente_data["cuil"], 
                    agente_data["apellido"], 
                    agente_data["nombre"], 
                    agente_data["sueldo_basico"], 
                    agente_data["antiguedad"], 

                    agente_data["carrera"], 
                    agente_data["cargo"], 
                    agente_data["catedra"], 

                    agente_data["area_investigacion"], 
                    agente_data["tipo_investigacion"], 
                    agente_data["categoria"], 
                    agente_data["importe_extra"])
                self.agregar_agente(docente_investigador)

    def mostrarTodo(self):
        for agente in self.agentes:
            print(f"Tipo: {type(agente).__name__}")
            print(agente)

    def listado_ordenado(self, carrera):
        docentes_investigadores = []
        i=0
        while i < len(self.agentes): 
            if isinstance(self.agentes[i], DocenteInvestigador) and self.agentes[i].get_carrera() == carrera:
                docentes_investigadores.append(self.agentes[i])
                i+=1
            else:
                i+=1
        docentes_investigadores.sort()
        for docente in docentes_investigadores:
            print(f"Nombre: {docente.get_nombre()}")

    def contar_agentes_por_area_investigacion(self, area_investigacion):
        contador_docentes_investigadores = 0
        contador_investigadores = 0
        for agente in self.agentes:
            if isinstance(agente, DocenteInvestigador) and agente.get_area_investigacion() == area_investigacion:
                contador_docentes_investigadores += 1
            elif isinstance(agente, Investigador) and agente.get_area_investigacion() == area_investigacion:
                contador_investigadores += 1
        print(f"Cantidad de Agentes Investigadores en el area {area_investigacion} son: {contador_investigadores}")
        print(f"Cantidad de Docentes Investigadores en el area {area_investigacion} son: {contador_docentes_investigadores}")

    def generar_listado_agentes(self):
        listado_agentes = []
        for agente in self.agentes:
            tipo_agente = type(agente).__name__
            sueldo = agente.calcular_sueldo()
            listado_agentes.append((agente.get_nombre(), agente.get_apellido(), tipo_agente, sueldo))
        listado_agentes.sort(key=lambda x: x[1])  # Ordenar por apellido
        return listado_agentes

    def listar_importe_extra_por_categoria(self, categoria):
        docentes_investigadores_categoria = []
        total_importe_extra = 0
        for agente in self.agentes:
            if isinstance(agente, DocenteInvestigador) and agente.get_categoria() == categoria:
                docentes_investigadores_categoria.append(
                    (agente.get_apellido(), agente.get_nombre(), agente.get_importe_extra())
                )
                total_importe_extra += agente.get_importe_extra()
        for apellido, nombre, importe in docentes_investigadores_categoria:
            print(apellido, nombre, importe)
        print(f"La secretaria debera solicitar: {total_importe_extra}")

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w", encoding="utf-8") as file:
            agentes_data = [agente.to_dict() for agente in self.agentes]
            json.dump(agentes_data, file, indent=2, ensure_ascii=False)
        print("Archivo generado con exito")

    def buscar_agente_por_cuil(self, cuil):
        i = 0
        band=False
        while i < len(self.agentes) and not band:
            agente = self.agentes[i]
            if agente.get_cuil() == cuil:
                band=True
                return agente
            else:
                i += 1

    def getDocente(self, cuil):
        i = 0
        band=False
        while i < len(self.agentes) and not band:
            agente = self.agentes[i]
            if isinstance(agente, Docente) and agente.get_cuil() == cuil:
                band=True
                return agente
            else:
                i += 1

    def getPersonalApoyo(self, cuil):
        i = 0
        band=False
        while i < len(self.agentes) and not band:
            agente = self.agentes[i]
            if isinstance(agente, PersonalApoyo) and agente.get_cuil() == cuil:
                band=True
                return agente
            else:
                i += 1

    def getDocenteInvestigador(self, cuil):
        i = 0
        band=False
        while i < len(self.agentes) and not band:
            agente = self.agentes[i]
            if isinstance(agente, DocenteInvestigador) and agente.get_cuil() == cuil:
                band=True
                return agente
            else:
                i += 1

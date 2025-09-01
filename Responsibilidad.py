# Clase que se encarga SOLAMENTE de gestionar las tareas
class GestorTareas:
    def crear_tarea(self):
        # Lógica para crear la tarea
        print("✅ Tarea creada correctamente.")

    def actualizar_tarea(self):
        # Lógica para actualizar la tarea
        print("♻️ Tarea actualizada correctamente.")

    def eliminar_tarea(self):
        # Lógica para eliminar la tarea
        print("🗑️ Tarea eliminada correctamente.")


# Clase que se encarga SOLAMENTE de la conexión con una API externa
class ConectorAPI:
    def conectar_api(self):
        # Lógica de conexión (ejemplo ficticio)
        print("🌐 Conectando con la API externa...")
        return "Conexión exitosa con API"


# Clase que se encarga SOLAMENTE de enviar notificaciones
class Notificador:
    def enviar_notificacion(self):
        # Lógica para enviar la notificación
        print("📩 Notificación enviada al usuario.")


# Clase que se encarga SOLAMENTE de generar informes
class GeneradorInforme:
    def generar_informe(self):
        # Lógica para crear el informe
        print("📊 Informe generado correctamente.")


# Clase que se encarga SOLAMENTE de enviar informes
class EnviadorInforme:
    def enviar_informe(self):
        # Lógica para enviar el informe
        print("📤 Informe enviado correctamente.")


# Clase principal para probar todas las funcionalidades
if __name__ == "__main__":
    # 1. Gestionar tareas
    gestor = GestorTareas()
    gestor.crear_tarea()
    gestor.actualizar_tarea()
    gestor.eliminar_tarea()

    # 2. Conectar a una API externa
    api = ConectorAPI()
    print(api.conectar_api())

    # 3. Enviar notificación
    notificador = Notificador()
    notificador.enviar_notificacion()

    # 4. Generar informe
    generador = GeneradorInforme()
    generador.generar_informe()

    # 5. Enviar informe
    enviador = EnviadorInforme()
    enviador.enviar_informe()

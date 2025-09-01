// Clase principal para probar todas las funcionalidades
public class Main {
    public static void main(String[] args) {
        
        // 1. Gestionar tareas
        GestorTareas gestor = new GestorTareas();
        gestor.crearTarea();
        gestor.actualizarTarea();
        gestor.eliminarTarea();

        // 2. Conectar a una API externa
        ConectorAPI api = new ConectorAPI();
        System.out.println(api.conectarAPI());

        // 3. Enviar notificación
        Notificador notificador = new Notificador();
        notificador.enviarNotificacion();

        // 4. Generar informe
        GeneradorInforme generador = new GeneradorInforme();
        generador.generarInforme();

        // 5. Enviar informe
        EnviadorInforme enviador = new EnviadorInforme();
        enviador.enviarInforme();
    }
}

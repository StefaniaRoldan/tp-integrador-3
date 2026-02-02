class FormularioContacto:
    def __init__(self, nombre: str, email: str, mensaje: str):
        self.nombre = nombre or ""
        self.email = email or ""
        self.mensaje = mensaje or ""

    def enviar(self):
        errores = []
        if not self.nombre.strip():
            errores.append("El campo 'nombre' es obligatorio.")
        if not self.email.strip():
            errores.append("El campo 'email' es obligatorio.")
        if not self.mensaje.strip():
            errores.append("El campo 'mensaje' es obligatorio.")

        if errores:
            return {"success": False, "errors": errores}
        return {"success": True, "message": "Formulario enviado con éxito ✅"}


if __name__ == "__main__":
    print("---- Formulario de Contacto ----")
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    mensaje = input("Ingrese su mensaje: ")

    form = FormularioContacto(nombre, email, mensaje)
    resultado = form.enviar()

    if resultado["success"]:
        print(resultado["message"])
    else:
        print("Errores encontrados:")
        for err in resultado["errors"]:
            print("-", err)
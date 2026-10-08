package ejercicios_adicionales.ejer_3;

import java.util.ArrayList;
import java.util.List;

class Contacto {
    private String direccionFisica;
    private String correoElectronico;
    private String telefonoFijo;
    private String telefonoMovil;

    public Contacto(String direccionFisica, String correoElectronico, String telefonoFijo, String telefonoMovil) {
        this.direccionFisica = direccionFisica;
        this.correoElectronico = correoElectronico;
        this.telefonoFijo = telefonoFijo;
        this.telefonoMovil = telefonoMovil;
    }

    public String getDireccionFisica() {
        return direccionFisica;
    }

    public void setDireccionFisica(String direccionFisica) {
        this.direccionFisica = direccionFisica;
    }

    public String getCorreoElectronico() {
        return correoElectronico;
    }

    public void setCorreoElectronico(String correoElectronico) {
        this.correoElectronico = correoElectronico;
    }

    public String getTelefonoFijo() {
        return telefonoFijo;
    }

    public void setTelefonoFijo(String telefonoFijo) {
        this.telefonoFijo = telefonoFijo;
    }

    public String getTelefonoMovil() {
        return telefonoMovil;
    }

    public void setTelefonoMovil(String telefonoMovil) {
        this.telefonoMovil = telefonoMovil;
    }
    
}

class Cliente {
    private String rut;
    private String nombre;
    private Contacto contacto;

    public Cliente(String rut, String nombre, Contacto contacto) {
        this.rut = rut;
        this.nombre = nombre;
        this.contacto = contacto;
    }

    public String getRut() {
        return rut;
    }

    public void setRut(String rut) {
        this.rut = rut;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }
    
}

class Colaborador {
    private String rut;
    private String nombre;
    private String cargo;
    private Contacto contacto;
    private List<Cliente> clientes;

    public Colaborador(String rut, String nombre, String cargo, Contacto contacto) {
        this.rut = rut;
        this.nombre = nombre;
        this.cargo = cargo;
        this.contacto = contacto;
        this.clientes = new ArrayList<>();
    }

    public void agregarCliente(Cliente cliente) {
        this.clientes.add(cliente);
    }

    public String getRut() {
        return rut;
    }

    public void setRut(String rut) {
        this.rut = rut;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

    public List<Cliente> getClientes() {
        return clientes;
    }

    public void setClientes(List<Cliente> clientes) {
        this.clientes = clientes;
    }
    
}

class Empresa {
    private String nombre;
    private String fechaFundacion;
    private List<Colaborador> colaboradores;

    public Empresa(String nombre, String fechaFundacion) {
        this.nombre = nombre;
        this.fechaFundacion = fechaFundacion;
        // como pide una lista se usa el "new ArrayList<>"
        this.colaboradores = new ArrayList<>();
    }

    public void agregarColaborador(Colaborador colaborador) {
        this.colaboradores.add(colaborador);
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getFechaFundacion() {
        return fechaFundacion;
    }

    public void setFechaFundacion(String fechaFundacion) {
        this.fechaFundacion = fechaFundacion;
    }

    public List<Colaborador> getColaboradores() {
        return colaboradores;
    }

    public void setColaboradores(List<Colaborador> colaboradores) {
        this.colaboradores = colaboradores;
    }
    
}

public class main {
    public static void main(String[] args) {
        // Ejemplo de uso e instanciación del modelo
        Empresa miEmpresa = new Empresa("Tech Solutions", "15/08/2010");
        
        Contacto contactoColab = new Contacto("Av. Principal 123", "juan@tech.com", "22334455", "+56987654321");
        Colaborador colab = new Colaborador("11.111.111-1", "Juan Pérez", "Ejecutivo de Ventas", contactoColab);
        
        Contacto contactoCliente = new Contacto("Calle Sur 456", "cliente@mail.com", "22998877", "+56912345678");
        Cliente cliente = new Cliente("22.222.222-2", "Comercializadora SPA", contactoCliente);
        
        colab.agregarCliente(cliente);
        miEmpresa.agregarColaborador(colab);
        
        System.out.println("Estructura de la empresa inicializada correctamente.");
    }
}
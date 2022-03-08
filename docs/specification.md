# Pepino

Este proyecto es para administrar huertas.

## Entidades

### **User**

Esta entidad permite almacenar y recuperar datos de usuarios.

### Atributos

- **UserName**: Texto
- **Email**: texto
- **Password**: Texto
- **Orchads**: [Orchard]

### Metodos

- Login
- **CRUD**: Create, Read, Update, Delete
- SendMail
- PasswordRecovery

---

### **Orchard**

### Atributos

- **Name**: Texto
- **CompassPoint**: [N | S | E | W]
- **Size**: unidad es m^2
- **SunExposure**: Horas de luz solar.
- **Crops**: [Crop]
- **Owner**: User

### Metodos

- **CRUD**

---

### **Crop**

### Atributos

- **Name**: Texto

### Metodos

- **CRUD**

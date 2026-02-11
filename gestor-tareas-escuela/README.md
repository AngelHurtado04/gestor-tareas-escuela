# Sistema Gestor de Tareas para la Escuela

**Autor:** Angel Andres Mendoza Hurtado  
**Matrícula:** 367862  
**Materia:** Proyectos Profesionales II  
**Fecha de Inicio:** 27 de Enero, 2026

## Descripción del Proyecto

Sistema web para gestión de tareas académicas diseñado para estudiantes universitarios y de nivel medio superior. Permite registrar, consultar, modificar y dar seguimiento a tareas, proyectos y exámenes de manera eficiente.

## Objetivos

- Facilitar la organización de actividades académicas
- Proporcionar una interfaz intuitiva y fácil de usar
- Permitir el seguimiento del estado de tareas (pendiente/completada)
- Ofrecer filtros para visualizar tareas según su estado
- Mejorar la productividad estudiantil

## Tecnologías Utilizadas

### Backend
- **Lenguaje:** Python 3.11+
- **Framework:** Django 4.2
- **ORM:** Django ORM / SQLAlchemy 2.0
- **API:** Django REST Framework
- **Base de Datos:** SQLite (desarrollo) / PostgreSQL (producción)

### Frontend
- **Framework:** React 18.2
- **Build Tool:** Vite
- **Lenguaje:** JavaScript (ES6+)
- **Estilos:** Tailwind CSS
- **HTTP Client:** Axios

### Herramientas de Desarrollo
- **Editor:** Visual Studio Code
- **Control de Versiones:** Git + GitHub
- **Gestión de Proyecto:** Monday.com + Trello
- **Testing:** pytest (Backend), Jest (Frontend)

## Estructura del Proyecto

```
gestor-tareas-escuela/
├── backend/                # Servidor Django
│   ├── api/               # Endpoints REST
│   ├── models/            # Modelos de datos
│   ├── services/          # Lógica de negocio
│   ├── repositories/      # Acceso a datos
│   └── manage.py          # Script de Django
│
├── frontend/              # Aplicación React
│   ├── src/
│   │   ├── components/   # Componentes React
│   │   ├── services/     # Servicios API
│   │   ├── pages/        # Páginas principales
│   │   └── App.jsx       # Componente raíz
│   └── package.json
│
├── docs/                  # Documentación
└── README.md             # Este archivo
```

## Funcionalidades Principales

### Requerimientos Funcionales Implementados

- **RF-01:** Registro de nueva tarea con nombre, descripción, fecha límite y prioridad
- **RF-02:** Visualización de todas las tareas en formato lista
- **RF-03:** Edición de tareas existentes
- **RF-04:** Eliminación de tareas
- **RF-05:** Marcar tareas como completadas/pendientes
- **RF-06:** Filtrado de tareas por estado (Todas/Pendientes/Completadas)

### Requerimientos No Funcionales

- **RNF-01:** Usabilidad - Interfaz intuitiva y fácil de usar
- **RNF-02:** Rendimiento - Respuesta en menos de 5 segundos
- **RNF-03:** Portabilidad - Compatible con Chrome, Edge, Firefox
- **RNF-04:** Seguridad - Validación dual cliente-servidor
- **RNF-05:** Mantenibilidad - Código modular y documentado
- **RNF-06:** Accesibilidad - Cumple estándares WCAG 2.1 AA

## Cronograma de Desarrollo

### Fase 1: Preparación y Diseño (27 enero - 9 febrero)
- [x] Configuración del ambiente de desarrollo
- [x] Creación del repositorio GitHub
- [x] Configuración entorno virtual Python
- [x] Diseño detallado de base de datos
- [x] Configuración proyecto React con Vite

### Fase 2: Desarrollo Backend (10 febrero - 2 marzo)
- [ ] Implementación de modelos de datos (ORM)
- [ ] Desarrollo del Repository Pattern
- [ ] Implementación de capa de servicios
- [ ] Desarrollo de API REST (CRUD endpoints)
- [ ] Implementación de autenticación JWT
- [ ] Pruebas unitarias del backend

### Fase 3: Desarrollo Frontend (3 marzo - 23 marzo)
- [ ] Componente de autenticación (Login/Register)
- [ ] Servicio de comunicación con API
- [ ] Componente Lista de Tareas
- [ ] Componente Formulario Nueva Tarea
- [ ] Componente Formulario Editar Tarea
- [ ] Funcionalidad de filtros por estado
- [ ] Marcar tarea como completada (checkbox)
- [ ] Diseño CSS responsive y pulido visual

### Fase 4: Integración y Pruebas (24 marzo - 6 abril)
- [ ] Integración frontend-backend completa
- [ ] Pruebas de integración
- [ ] Pruebas End-to-End (E2E)
- [ ] Corrección de bugs detectados

### Fase 5: Despliegue y Documentación (7 abril - 10 abril)
- [ ] Preparación para despliegue (build producción)
- [ ] Despliegue en servidor (Vercel + Railway)
- [ ] Documentación técnica final y manual

## Instalación y Configuración

### Requisitos Previos
- Python 3.11 o superior
- Node.js 18 o superior
- Git

### Backend Setup

```bash
# Clonar el repositorio
git clone https://github.com/AngelHurtado04/gestor-tareas-escuela.git
cd gestor-tareas-escuela/backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor de desarrollo
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

## Base de Datos

### Modelo de Datos Principal

**Tabla: usuarios**
- id (PK)
- nombre
- email (UNIQUE)
- password (hash)
- fecha_registro
- ultimo_acceso

**Tabla: tareas**
- id (PK)
- usuario_id (FK → usuarios.id)
- nombre
- descripcion
- fecha_limite
- completada (BOOLEAN)
- prioridad (Alta/Media/Baja)
- fecha_creacion
- fecha_actualizacion

Relación: 1 Usuario → N Tareas

## Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Documentación Adicional

- [Documento de Requerimientos](docs/requerimientos.md)
- [Guía de Arquitectura](docs/arquitectura.md)
- [Manual de Usuario](docs/manual-usuario.md)
- [Plan de Construcción](docs/plan-construccion.md)

## Contribuciones

Este es un proyecto académico individual para la materia de Proyectos Profesionales II.

## Licencia

Este proyecto es de uso académico exclusivamente.

## Contacto

**Angel Andres Mendoza Hurtado**  
Matrícula: 367862  
Universidad Autónoma de Chihuahua  
Facultad de Ingeniería

---

**Estado del Proyecto:** En Desarrollo (Fase 2)  
**Última Actualización:** 10 de Febrero, 2026

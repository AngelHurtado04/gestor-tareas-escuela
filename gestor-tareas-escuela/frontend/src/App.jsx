/**
 * Componente principal de la aplicación
 * Sistema Gestor de Tareas para la Escuela
 * 
 * @author Angel Andres Mendoza Hurtado
 * @matricula 367862
 * @date 10 de febrero, 2026
 */

import React, { useState } from 'react';
import './App.css';

function App() {
  const [tareas, setTareas] = useState([]);
  const [filtro, setFiltro] = useState('todas');

  return (
    <div className="App">
      <header className="app-header">
        <h1>📚 Gestor de Tareas Escolar</h1>
        <p>Sistema de organización académica</p>
      </header>

      <main className="app-main">
        <div className="container">
          <div className="welcome-message">
            <h2>¡Bienvenido al Sistema de Gestión de Tareas!</h2>
            <p>Este sistema está en desarrollo activo.</p>
            <p><strong>Fase actual:</strong> Desarrollo Backend (Fase 2)</p>
            <p><strong>Progreso:</strong> 25% completado</p>
          </div>

          <div className="status-grid">
            <div className="status-card completed">
              <h3>✅ Fase 1</h3>
              <p>Preparación y Diseño</p>
              <span className="badge">Completada</span>
            </div>

            <div className="status-card in-progress">
              <h3>🔄 Fase 2</h3>
              <p>Desarrollo Backend</p>
              <span className="badge">En progreso</span>
            </div>

            <div className="status-card pending">
              <h3>⏳ Fase 3</h3>
              <p>Desarrollo Frontend</p>
              <span className="badge">Pendiente</span>
            </div>

            <div className="status-card pending">
              <h3>⏳ Fase 4</h3>
              <p>Integración</p>
              <span className="badge">Pendiente</span>
            </div>
          </div>

          <div className="tech-stack">
            <h3>🛠️ Stack Tecnológico</h3>
            <div className="tech-list">
              <span className="tech-badge backend">Django 4.2</span>
              <span className="tech-badge backend">Python 3.11</span>
              <span className="tech-badge frontend">React 18.2</span>
              <span className="tech-badge frontend">Vite</span>
              <span className="tech-badge database">PostgreSQL</span>
              <span className="tech-badge tools">Git + GitHub</span>
            </div>
          </div>
        </div>
      </main>

      <footer className="app-footer">
        <p>Desarrollado por Angel Andres Mendoza Hurtado - Matrícula 367862</p>
        <p>Universidad Autónoma de Chihuahua | Ingeniería de Software</p>
      </footer>
    </div>
  );
}

export default App;

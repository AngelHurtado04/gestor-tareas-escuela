"""
Modelos de datos para el Sistema Gestor de Tareas
Autor: Angel Andres Mendoza Hurtado
Matrícula: 367862
Fecha: 10 de febrero, 2026
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from datetime import date


class Usuario(AbstractUser):
    """
    Modelo extendido de usuario para el sistema
    Extiende el modelo AbstractUser de Django para agregar campos personalizados
    """
    
    # Campos adicionales
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return f"{self.username} - {self.email}"


class Tarea(models.Model):
    """
    Modelo principal para las tareas del sistema
    Representa una tarea académica con todos sus atributos
    """
    
    # Opciones de prioridad
    PRIORIDAD_CHOICES = [
        ('ALTA', 'Alta'),
        ('MEDIA', 'Media'),
        ('BAJA', 'Baja'),
    ]
    
    # Campos principales
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='tareas',
        verbose_name='Usuario'
    )
    
    nombre = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(1)],
        verbose_name='Nombre de la tarea'
    )
    
    descripcion = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Descripción'
    )
    
    fecha_limite = models.DateField(
        verbose_name='Fecha límite'
    )
    
    completada = models.BooleanField(
        default=False,
        verbose_name='Completada'
    )
    
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDAD_CHOICES,
        default='MEDIA',
        verbose_name='Prioridad'
    )
    
    # Campos de auditoría
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name='Última actualización'
    )
    
    class Meta:
        db_table = 'tareas'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['completada', 'fecha_limite', '-prioridad']
        indexes = [
            models.Index(fields=['usuario', 'completada']),
            models.Index(fields=['fecha_limite']),
        ]
    
    def __str__(self):
        estado = "✓" if self.completada else "○"
        return f"{estado} {self.nombre} ({self.get_prioridad_display()})"
    
    def clean(self):
        """
        Validación personalizada del modelo
        """
        from django.core.exceptions import ValidationError
        
        # Validar que la fecha límite no sea en el pasado (solo para nuevas tareas)
        if not self.pk and self.fecha_limite < date.today():
            raise ValidationError({
                'fecha_limite': 'La fecha límite no puede ser en el pasado.'
            })
        
        # Validar longitud del nombre
        if len(self.nombre.strip()) == 0:
            raise ValidationError({
                'nombre': 'El nombre no puede estar vacío.'
            })
    
    def save(self, *args, **kwargs):
        """
        Override del método save para ejecutar validaciones
        """
        self.full_clean()
        super().save(*args, **kwargs)
    
    def marcar_completada(self):
        """
        Marca la tarea como completada
        """
        self.completada = True
        self.save()
    
    def marcar_pendiente(self):
        """
        Marca la tarea como pendiente
        """
        self.completada = False
        self.save()
    
    @property
    def esta_vencida(self):
        """
        Verifica si la tarea está vencida
        """
        return not self.completada and self.fecha_limite < date.today()
    
    @property
    def dias_restantes(self):
        """
        Calcula los días restantes hasta la fecha límite
        """
        delta = self.fecha_limite - date.today()
        return delta.days

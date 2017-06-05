from .models import Rol, Empresa

roles = Rol.objects.bulk_create([Rol(tipo='administrador', es_personal=False),
                                 Rol(tipo='paciente', es_personal=False),
                                 Rol(tipo='fisioterapista', es_personal=True),
                                 Rol(tipo='nutricionista', es_personal=True)])

Empresa.objects.create(nombre="Kala Fitness",
                       razon_social="Kala Fitness",
                       propietario_nombre="ABC",
                       propietario_apellido="XYZ",
                       ruc="0999999999001",
                       telefono="0987665432",
                       direccion="Urdesa central",
                       iva=12
                       )
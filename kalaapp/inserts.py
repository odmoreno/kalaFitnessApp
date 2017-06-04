from .models import Rol

roles = Rol.objects.bulk_create([Rol(tipo='administrador', es_personal=False),
                                 Rol(tipo='paciente', es_personal=False),
                                 Rol(tipo='fisioterapista', es_personal=True),
                                 Rol(tipo='nutricionista', es_personal=True)])


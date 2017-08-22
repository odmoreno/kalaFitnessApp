'''
MODULO DIAGNOSTICO FISIOTERAPISTA Y NUTRICIONISTA

VERSION 2.0.0

ACTUALIZADO EN 15/07/2017

'''

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from diagnostico.models import DiagnosticoFisioterapia, DiagnosticoNutricion, Dieta, PlanNutDiario
from kalaapp.views import paginar
from paciente.models import Paciente
from personal.models import Personal
from .models import Rutina, Subrutina, DIAS
from kalaapp.decorators import rol_required

# Create your views here.


'''
Funcion: listarDiagnosticos
Entradas: request
Salidas: - HttpResponse con template diagnostico_listar.ntml y la lista de todos los diagnosticos

Funcion que permite listar los diagnosticos existentes
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista'])
def listarDiagnosticos(request):
    template = 'diagnostico_listar.html'
    contexto = {}
    diagnosticos = None
    rol = None

    sesion = request.session.get('user_sesion', None)

    if sesion:
        rol = sesion.get('rol__tipo', None)

        if rol == 'fisioterapista':
            diagnosticos = DiagnosticoFisioterapia.objects.filter(estado='A', paciente__usuario__estado='A',
                                                                  personal_id=sesion.get('personal__id', 0))\
                .annotate(paciente_nombre_completo=Concat('paciente__usuario__nombre',
                                                          Value(' '), 'paciente__usuario__apellido')) \
                .annotate(paciente_id=Concat('paciente_id', Value('')))\
                .annotate(paciente_foto=Concat('paciente__usuario__foto', Value('')))\
                .annotate(cedula=Concat('paciente__usuario__cedula', Value('')))\
                .order_by('-creado')

        elif rol == 'nutricionista':
            diagnosticos = DiagnosticoNutricion.objects.filter(estado='A', paciente__usuario__estado='A',
                                                               personal_id=sesion.get('personal__id', 0))\
                .annotate(paciente_nombre_completo=Concat('paciente__usuario__nombre',
                                                          Value(' '), 'paciente__usuario__apellido')) \
                .annotate(paciente_id=Concat('paciente_id', Value('')))\
                .annotate(paciente_foto=Concat('paciente__usuario__foto', Value(''))) \
                .annotate(cedula=Concat('paciente__usuario__cedula', Value(''))) \
                .order_by('-creado') \

    contexto['diagnosticos'] = diagnosticos
    contexto['user_sesion'] = sesion

    return render(request, template_name=template, context=contexto)


'''
Funcion: crearDiagnostico
Entradas: request
Salidas: - HttpResponse con template crear.ntml y la lista de todas los pacientes

Funcion que permite crear un nuevo diagnostico
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista'])
@transaction.atomic
def crearDiagnostico(request):
    template = None
    contexto = {}
    pacientes = None
    rol = None

    sesion = request.session.get('user_sesion', None)

    if sesion:
        rol = sesion.get('rol__tipo', '')

    if request.method == 'POST':
        diagnostico = getDiagnostico(request)

        if diagnostico is not None:
            messages.add_message(request, messages.SUCCESS, 'Diagnostico creado con exito!')
        else:
            messages.add_message(request, messages.WARNING, 'Error inesperado creando diagnostico!')
        return redirect('diagnostico:ListarDiagnosticos')

    try:
        pacientes = Paciente.objects.filter(usuario__estado='A', pacientepersonal__estado='A',
                                            pacientepersonal__personal_id=sesion.get('personal__id', 0))\
            .values('id', 'usuario__nombre', 'usuario__apellido') \
            .annotate(nombre_completo=Concat('usuario__nombre', Value(' '), 'usuario__apellido')) \
            .order_by('nombre_completo')
        if pacientes is None or pacientes.count() == 0:
            raise Exception
    except Exception, e:
        messages.add_message(request, messages.WARNING, 'No tiene pacientes asignados, consulte con su administrador! ')

    contexto['pacientes'] = pacientes

    if rol == 'fisioterapista':
        template = 'diagnostico_crear.html'
    elif rol == 'nutricionista':
        template = 'diagnostico_nut_crear.html'
        contexto['dias'] = DIAS
    else:
        return redirect(to='/')

    return render(request, template_name=template, context=contexto)

'''
Funcion: getDiagnostico
Entradas: - request
Salidas:  - nueva diagnostico

Funcion que retorna un nuevo diagnostico con los datos ingresados en formulario
'''


@transaction.atomic
def getDiagnostico(request):
    diagnostico = None
    sesion = request.session.get('user_sesion', None)
    rol = None

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if rol is not None:
        try:
            if rol == 'fisioterapista':
                diagnostico = DiagnosticoFisioterapia()
                diagnostico.area_afectada = request.POST.get('areaafectada', '')
                diagnostico.receta = request.POST.get('receta', '')
                diagnostico.rutina = Rutina.objects.create()

                cantidad_rutinas = int(request.POST.get('cantidadrutinas', '0'))
                id_rutinas = request.POST.getlist('idaccordion', [])
                nombre_rutinas = request.POST.getlist('nombrerutina', [])
                descripcion_rutinas = request.POST.getlist('descripcionrutina', [])
                repeticiones_rutinas = request.POST.getlist('repeticionesrutina', [])
                veces_rutinas = request.POST.getlist('vecesrutina', [])
                descanso_rutinas = request.POST.getlist('descansorutina', [])
                videoenlace_rutinas = request.POST.getlist('videoenlace', [])

                for id, nom, desc, rep, vec, des, vid in zip(id_rutinas, nombre_rutinas, descripcion_rutinas,
                                                             repeticiones_rutinas, veces_rutinas, descanso_rutinas,
                                                             videoenlace_rutinas):

                    subrutina = Subrutina.objects.create(nombre=nom, detalle=desc, repeticiones=rep, veces=vec,
                                                         descanso=des, link=vid)
                    diagnostico.rutina.subrutina.add(subrutina)
            elif rol == 'nutricionista':
                diagnostico = DiagnosticoNutricion()

                dieta = Dieta()
                dieta.descripcion = request.POST.get('dietadescripcion', '')
                dieta.save()
                diagnostico.dieta = dieta

                for key, dia in DIAS:
                    plan_diario = PlanNutDiario(dia=dia,
                                                desayuno=request.POST.get(dia+'_Desayuno', ''),
                                                colacion1=request.POST.get(dia+'_Colacion1', ''),
                                                almuerzo=request.POST.get(dia+'_Almuerzo', ''),
                                                colacion2=request.POST.get(dia+'_Colacion2', ''),
                                                cena=request.POST.get(dia+'_Cena', ''),
                                                dieta=dieta)
                    plan_diario.save()

            diagnostico.personal = Personal.objects.get(estado='A', id=sesion.get('personal__id', 0))
            diagnostico.paciente = Paciente.objects.get(estado='A', id=request.POST.get('paciente', 0))
            diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
            diagnostico.save()
        except Exception, e:
            return None
    return diagnostico

'''
Funcion: crearDiagnostico
Entradas: - request
          - id: id del diagnostico a eliminar
Salidas: ninguna

Funcion que permite eliminar un diagnostico existente
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista'])
@transaction.atomic
def eliminarDiagnostico(request, id=0):
    contexto = {}
    diagnosticoEliminado = None
    sesion = request.session.get('user_sesion', None)

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if request.method == 'POST':
        try:
            if rol == 'fisioterapista':
                diagnosticoEliminado = DiagnosticoFisioterapia.objects.get(estado='A', id=id)
                subrutinas = Subrutina.objects.filter(rutina=diagnosticoEliminado.rutina)
                for subrutina in subrutinas:
                    subrutina.estado = 'I'
                    subrutina.save()
                diagnosticoEliminado.rutina.estado = 'I'
                diagnosticoEliminado.rutina.save()

            elif rol == 'nutricionista':
                diagnosticoEliminado = DiagnosticoNutricion.objects.get(estado='A', id=id)
                diagnosticoEliminado.dieta.estado = 'I'
                diagnosticoEliminado.dieta.save()

                for plan_diario in PlanNutDiario.objects.filter(estado='A', dieta=diagnosticoEliminado.dieta):
                    plan_diario.estado = 'I'
                    plan_diario.save()

            if diagnosticoEliminado and diagnosticoEliminado.estado == 'A':
                diagnosticoEliminado.estado = 'I'
                diagnosticoEliminado.save()
                messages.add_message(request, messages.SUCCESS, 'Diagnostico eliminado con exito!')
            else:
                messages.add_message(request, messages.WARNING, 'Diagnostico no encontrado o ya eliminado')
        except Exception, e:
            messages.add_message(request, messages.WARNING, 'Error inesperado! ' + str(e))

    return redirect('diagnostico:ListarDiagnosticos')

'''
Funcion: editarDiagnostico
Entradas: - request
          - id: id del diagnostico a editar
Salidas: ninguna

Funcion que permite editar un diagnostico existente
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista'])
def editarDiagnostico(request, id=0):
    contexto = {}
    template = None
    rol = None
    diagnostico = None
    pacientes = None
    subrutinas = None

    sesion = request.session.get('user_sesion', None)

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if request.method == 'POST':
        try:
            if rol == 'fisioterapista':
                template = 'diagnostico_editar.html'
                diagnostico = DiagnosticoFisioterapia.objects.get(id=id, estado='A')

                subrutinas = Subrutina.objects.filter(rutina=diagnostico.rutina, rutina__estado='A', estado='A')
            elif rol == 'nutricionista':
                template = 'diagnostico_nut_editar.html'
                diagnostico = DiagnosticoNutricion.objects.get(estado='A', id=id)
                dias = {'One': 'Lunes', 'Two': 'Martes', 'Three': 'Miercoles',
                        'Four': 'Jueves', 'Five': 'Viernes', 'Six': 'Sabado'}
                planes_diarios = PlanNutDiario.objects.filter(estado='A', dieta=diagnostico.dieta).order_by('id')
                contexto['planes_diarios'] = planes_diarios
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado consultando diagnostico!')

        try:
            pacientes = Paciente.objects.filter(estado='A', pacientepersonal__estado='A',
                                                pacientepersonal__personal_id=sesion.get('personal__id', 0)) \
                .values('id', 'usuario__nombre', 'usuario__apellido') \
                .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
                .order_by('nombre_completo')
        except Exception, e:
            messages.add_message(request, messages.WARNING, 'Error inesperado consultando pacientes! ' + str(e))

        contexto['diagnostico'] = diagnostico
        contexto['pacientes'] = pacientes
        contexto['subrutinas'] = subrutinas

    return render(request, template_name=template, context=contexto)

'''
Funcion: guardarDiagnostico
Entradas: - request
Salidas: ninguna

Funcion que persiste un Diagnostico en base
'''


@transaction.atomic
def guardarDiagnostico(request):
    diagnostico = None
    sesion = request.session.get('user_sesion', None)
    rol = None

    if sesion:
        rol = sesion.get('rol__tipo', '')

    if request.method == 'POST':
        try:
            if rol == 'fisioterapista':
                diagnostico = DiagnosticoFisioterapia.objects.get(id=request.POST.get('diagnostico_id', 0), estado='A')
                diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
                diagnostico.area_afectada = request.POST.get('areaafectada', '')
                diagnostico.receta = request.POST.get('receta', '')

                cantidad_rutinas = int(request.POST.get('cantidadrutinas', '0'))
                id_rutinas = request.POST.getlist('idaccordion', [])
                nombre_rutinas = request.POST.getlist('nombrerutina', [])
                descripcion_rutinas = request.POST.getlist('descripcionrutina', [])
                repeticiones_rutinas = request.POST.getlist('repeticionesrutina', [])
                veces_rutinas = request.POST.getlist('vecesrutina', [])
                descanso_rutinas = request.POST.getlist('descansorutina', [])
                videoenlace_rutinas = request.POST.getlist('videoenlace', [])

                print cantidad_rutinas, id_rutinas, nombre_rutinas, descripcion_rutinas, repeticiones_rutinas,\
                      veces_rutinas, descanso_rutinas, videoenlace_rutinas

                subrutinas = Subrutina.objects.filter(estado='A', rutina__estado='A', rutina=diagnostico.rutina)\
                    .order_by('id')

                for index, subrutina in enumerate(subrutinas):
                    print index, subrutina
                    subrutina.nombre = nombre_rutinas[index]
                    subrutina.detalle = descripcion_rutinas[index]
                    subrutina.repeticiones = repeticiones_rutinas[index]
                    subrutina.veces = veces_rutinas[index]
                    subrutina.descanso = descanso_rutinas[index]
                    subrutina.link = videoenlace_rutinas[index]
                    subrutina.save()

            elif rol == 'nutricionista':
                diagnostico = DiagnosticoNutricion.objects.get(estado='A',
                                                               id=request.POST.get('diagnostico_id', 0))
                diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
                diagnostico.dieta.descripcion = request.POST.get('dietadescripcion', '')
                diagnostico.dieta.save()

                for key, dia in DIAS:
                    plan_diario = PlanNutDiario.objects.get(estado='A', dia=dia, dieta=diagnostico.dieta)
                    plan_diario.desayuno = request.POST.get(dia + '_Desayuno', '')
                    plan_diario.colacion1 = request.POST.get(dia + '_Colacion1', '')
                    plan_diario.almuerzo = request.POST.get(dia + '_Almuerzo', '')
                    plan_diario.colacion2 = request.POST.get(dia + '_Colacion2', '')
                    plan_diario.cena = request.POST.get(dia + '_Cena', '')
                    plan_diario.save()

            if diagnostico:
                diagnostico.save()
                messages.add_message(request, messages.SUCCESS, 'Diagnostico actualizado satisfactoriamente!')
            else:
                raise Exception
        except Exception, e:
            messages.add_message(request, messages.WARNING, 'Error inesperado al actualizar diagnostico! ' + str(e))

    return redirect('diagnostico:ListarDiagnosticos')

'''
Funcion: detalleDiagnostico
Entradas: requerimiento e Identificador del diagnostico a ser visualizado
Salidas:Template para renderizacion
*Funcion que recibe el id de un diagnostico que debe ser visualizado, y muestra su informacion.*
'''
@login_required
def detalleDiagnostico(request, diagnostico_id):
    contexto = {}
    rol = None
    diagnostico = None
    template = None
    subrutinas = None
    planes_diarios = None
    sesion = request.session.get('user_sesion', None)
    if sesion:
        rol = sesion.get('rol__tipo', None)
    if rol == 'fisioterapista':
        template = 'diagnostico_detalle.html'
        diagnostico = get_object_or_404(DiagnosticoFisioterapia, pk=diagnostico_id)
        subrutinas = Subrutina.objects.filter(rutina=diagnostico.rutina, rutina__estado='A', estado='A')
        contexto['diagnostico'] = diagnostico
        contexto['subrutinas'] = subrutinas
        return render(request, template_name=template, context= contexto )
    elif rol == 'nutricionista':
        template = 'diagnostico_detalleNut.html'
        diagnostico = get_object_or_404(DiagnosticoNutricion, pk=diagnostico_id)
        planes_diarios = PlanNutDiario.objects.filter(estado='A', dieta=diagnostico.dieta).order_by('id')
        contexto['diagnostico'] = diagnostico
        contexto['planes_diarios'] = planes_diarios
        return render(request, template_name=template, context=contexto)







'''
Funcion: reporteTotal
Entradas: paciente_cedula, la cedula del paciente
Salidas: JSON con todos los diagnosticos del paciente
*Funcion que retorna la informacion de los diagnosticos de un paciente la base de datos
en forma de un JSON*
'''
@login_required
def reporteTotal(request, paciente_cedula):
    diagnosticos = DiagnosticoFisioterapia.objects.all()
    subrutinas = []

    for d in diagnosticos:
        if d.paciente.usuario.cedula==paciente_cedula and d.estado=='A': #and paciente.usuario.estado=='A':
            cedula = d.paciente.usuario.cedula
            condiciones_previas = d.condiciones_previas
            area_afectada = d.area_afectada
            nombre = d.paciente.usuario.nombre
            apellido = d.paciente.usuario.apellido
            genero = d.paciente.usuario.genero
            receta = d.receta

            for subrutina in d.rutina.subrutina.all():
                subrutinas.append({"nombre":subrutina.nombre, "detalle":subrutina.detalle, "veces":subrutina.veces, "repeticiones":subrutina.repeticiones, "descanso":subrutina.descanso})

            record = {
                "cedula": cedula,
                "condiciones_previas":condiciones_previas,
                "area_afectada":area_afectada,
                "apellido":apellido,
                "nombre":nombre,
                "genero":genero,
                "receta":receta,
                "subrutinas": subrutinas
            }

            return JsonResponse({"data": record})
'''
Funcion: reportes
Entradas: requerimiento get http
Salidas: Retorna un template de reportes de diagnosticos
'''
@login_required
def reportes(request):
    print "aquiiiii"
    template = 'reportes_diagnostico.html'
    return render(request, template)

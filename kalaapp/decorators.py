from django.http import HttpResponseForbidden


def rol_required(function=None, roles=[]):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            try:
                rol_sesion = request.session['user_sesion']['rol__tipo']

                if rol_sesion:
                    for rol_ in roles:
                        if rol_ == rol_sesion:
                            return view_func(request, *args, **kwargs)
                    return HttpResponseForbidden("No esta autorizado para acceder a este modulo." +
                                                 "<br>Administracion KalaFitnessApp.")
            except Exception, e:
                pass

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


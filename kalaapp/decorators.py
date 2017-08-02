from django.http import HttpResponseForbidden


def rol_required(function=None, roles=[]):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            rol_sesion = None
            sesion = request.session.get('user_sesion', None)

            if sesion:
                rol_sesion = sesion.get('rol__tipo', None)

                for rol_ in roles:
                    if rol_ == rol_sesion:
                        return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No esta autorizado paraa acceder a este modulo." +
                                         "\nAdministracion KalaFitnessApp.")

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


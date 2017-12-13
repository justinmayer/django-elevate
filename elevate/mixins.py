from elevate.decorators import elevate_required


class ElevateMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ElevateMixin, cls).as_view(**initkwargs)
        return elevate_required(view)

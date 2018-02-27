from django.forms.widgets import Textarea


class MiniTextarea(Textarea):
    """
    Vertically shorter version of textarea widget.
    """
    rows = 2

    def __init__(self, attrs=None):
        super(MiniTextarea, self).__init__({'rows': self.rows})

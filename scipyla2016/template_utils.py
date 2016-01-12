from itertools import groupby
from symposion.sponsorship.models import Sponsor


def sponsors(request):
    """Template pre-processor for the sponsor sidebar

    Returns a dict with the all conference sponsors, grouped by level and
    sorted by name.
    """
    sponsors = Sponsor.objects.filter(active=True)
    sponsors = sponsors.select_related('level')
    data = groupby(sponsors, lambda s: s.level)
    data = ((level, sorted(ss, key=lambda s: s.name))
            for level, ss in data)
    data = sorted(data, key=lambda x: x[0].order)
    return {'sponsor_levels': data}

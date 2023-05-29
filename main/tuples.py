from collections import namedtuple

WEBHOOK_TYPES = namedtuple('WEBHOOK_TYPES', 'project service')._make(range(2))
WEBHOOK_TYPE_CHOICES = (
    (WEBHOOK_TYPES.project, 'Project'),
    (WEBHOOK_TYPES.service, 'Service'),
)
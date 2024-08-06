# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging
import os


_ = MessageFactory('imio.scan_logger')
log = logging.getLogger("imio.scan_logger")

if os.environ.get("ZOPE_HOME", ""):
    BLDT_DIR = "/".join(os.getenv("INSTANCE_HOME", "").split("/")[:-2])
else:  # test env
    BLDT_DIR = os.getenv("PWD", "")

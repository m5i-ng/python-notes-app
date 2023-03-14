# Unless explicitly stated otherwise all files in this repository are dual-licensed
# under the Apache 2.0 or BSD3 Licenses.
#
# This product includes software developed at Datadog (https://www.datadoghq.com/)
# Copyright 2022 Datadog, Inc.
from ddtrace import patch; patch(logging=True)
import logging
import time
from ddtrace import tracer

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format=FORMAT)

class NotesHelper:

    def long_running_process(self):
        time.sleep(.3)
        logging.info("Hello from the long running process")
        self.__private_method_1()

    def another_process(self):
        time.sleep(.05)
        logging.info("Hello from the another process")

    def __private_method_1(self):
        time.sleep(.03)
        logging.info("Hello from the private method")

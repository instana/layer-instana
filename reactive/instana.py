#!/usr/bin/env python

# Copyright 2015 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from shlex import split
from subprocess import check_call
from charms.reactive import set_state
from charms.reactive import when, when_any, when_not
from charmhelpers.core import hookenv
from charmhelpers.core.templating import render


@when_not('instana.installed')
def install():
    '''Unpack and put the Instana on the right places.'''
    hookenv.status_set('maintenance', 'Installing Instana Agent.')

    key = hookenv.config('base64_key')
    if key == '':
        hookenv.status_set('blocked', 'Please provide a valid key')
        return

    host = hookenv.config('instana_host')
    port = hookenv.config('instana_port')

    context = {}
    context.update({'BASE64_ENCODED_INSTANA_KEY': key,
                    'INSTANA_HOST': host,
                    'INSTANA_PORT': port})

    render('instana-agent.yaml', '/var/tmp/instana-agent.yaml', context)
    command = '/snap/bin/kubectl apply -f /var/tmp/instana-agent.yaml --validate=false'
    hookenv.log(command)
    check_call(split(command))

    hookenv.status_set('active', 'Instana Agent is Ready')
    set_state('instanas.installed')


# Instana

This charm will deploy [Instana](https://instana.atlassian.net)

## Deployment

This charm is a subordinate of Kubernetes master, therefore you should have a
Kubernetes deployment already in place.

Please take a look at the [Canonical Distribution of Kubernetes](https://jujucharms.com/canonical-kubernetes/) 
or the [Kubernetes core](https://jujucharms.com/kubernetes-core/) bundles for 
examples of complete models of Kubernetes clusters.


To have a deployment going you will need to:

    juju deploy cs:~kos.tsakalozos/instana
    juju add-relation kubernetes-master instana


## Configuration

This charm will need an authkey so you should get it from Instana.
You can also set the Instana endpoint and port
as described [here](https://instana.atlassian.net/wiki/pages/viewpage.action?pageId=15630376#Docker(scheduled)-Kubernetes)


# More information

 - [Kubernetes github project](https://github.com/kubernetes/kubernetes)
 - [Instana](https://instana.atlassian.net)

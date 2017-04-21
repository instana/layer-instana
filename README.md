# Instana

[Instana](https://instana.atlassian.net) is a fully automatic APM solution that is only comprised of two major components: the Agent and the Backend.
This charm will deploy the Agent as soon as it gets related to a kubernetes-master charm.


## Deployment

This charm is a subordinate of Kubernetes master, therefore you should have a
Kubernetes deployment already in place.

Please take a look at the [Canonical Distribution of Kubernetes](https://jujucharms.com/canonical-kubernetes/)
or the [Kubernetes core](https://jujucharms.com/kubernetes-core/) bundles for 
examples of complete models of Kubernetes clusters.

Since the Instana needs priviliged containers you should also make sure this option in enabled in the Kuberneted deployment:

    juju config kubernetes-master allow-privileged=true
    juju config kubernetes-worker allow-privileged=true

Deploying the Instana charm is done with:

    juju deploy cs:~instana-charms/instana
    juju add-relation kubernetes-master instana

At this point the charm should be 'blocked' promptting you to 'Please provide a valid key'. Providing the key is as simple as:

    juju config instana base64_key=`echo "<agent key>" | base64`


## Configuration

This charm will need an agent authkey you should get from Instana.

You can also set the Instana endpoint and port
as described [here](https://instana.atlassian.net/wiki/pages/viewpage.action?pageId=15630376#Docker(scheduled)-Kubernetes)

If you wish to configure the application at deployment time please consult the respective [Juju documentation](https://jujucharms.com/docs/2.1/charms-config)


# More information

 - [Kubernetes github project](https://github.com/kubernetes/kubernetes)
 - [Instana](https://instana.atlassian.net)

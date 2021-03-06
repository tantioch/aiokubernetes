==========
Quickstart
==========

.. currentmodule:: aiokubernetes

Eager to get started? This page gives a good introduction in how to
get started with aiokubernetes.

First, make sure that aiokubernetes is :ref:`installed
<aiokubernetes-installation>` and *up-to-date*

Let's get started with some simple examples.



List all Pods
=============

Begin by importing the aiokubernetes module::

    import aiokubernetes as k8s

Then construct an ``ApiClient`` object via this convenience function::

    api_client = k8s.config.new_client_from_config()

This will look for your ``kubeconfig`` file in ``~/.kube/kubeconfig`` or wherever
the ``KUBECONFIG`` environment variable points to, configure the ``ApiClient``
(cluster address, authentication headers,...) and return it.

Then we need to instantiate the Kubernetes API group that defines Pods, since
we want to list Pods. This happens to be the `CoreAPI v1
<https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#pod-v1-core>`_::

    v1 = k8s.api.CoreV1Api(api_client)

This class is auto-generated by Swagger and it defines a _lot_ of methods
because the Kubernetes core API defines a lot of endpoints. For instance, the
file ``aiokubernetes/api/core_v1_api.py`` for v1.10 of Kubernetes defines 397(!)
methods. Among those is one called ``list_pod_for_all_namespaces``::

    ret = await v1.list_pod_for_all_namespaces()

This will return a ``ApiResponse`` object (just a named tuple with an ``http`` and
``obj`` filed). The ``http`` field contains the HTTP response object from the
`aiohttp <https://docs.aiohttp.org/en/stable/client_quickstart.html>` library.
You can examine it to determine the response code. For instance, Kubernetes
will respond with 200 if all went well::

    assert ret.http.status == 200

To find out what Kubernetes sent us we can decode the raw Json response and find::

    ret_json = await ret.http.json()
    print(ret_json['kind'])  # --> 'PodList'

This is precisely what the
`Kubernetes API documentation
<https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#pod-v1-core>`_
said it would return. You can now parse the Json response and print all pod names::

    for pod in ret_json['items']:
        print(pod['metadata']['name'])

Alternatively, you can get the same result via the Swagger generated
convenience classes::

    for pod in ret.obj:
        print(pod.metadata.name)

The only difference is that you save the ``ret_json = await ret.http.json()``
call, can access the fields directly via the ``.`` operator and that dates will
become ``datetime`` objects.

That was all. For a clean shutdown you should also do::

    await api_client.close()

This will close all open connections and avoids ugly (albeit harmless) error
messages at program exist when you run in `asyncio debug mode
<https://docs.python.org/3/library/asyncio-dev.html>`_.


List Anything
-------------

In the previous example we used
``k8s.api.CoreV1Api(api_client).list_pod_for_all_namespaces()`` to list all pods.
If you want to list anything else defined in the core Api, you just replace
``pod`` with whatever resource you want::

    k8s.api.CoreV1Api(api_client).list_config_map_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_endpoints_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_event_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_limit_range_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_persistent_volume_claim_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_pod_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_pod_template_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_replication_controller_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_resource_quota_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_secret_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_service_account_for_all_namespaces()
    k8s.api.CoreV1Api(api_client).list_service_for_all_namespaces()

Change them the following versions if you are only interested in a specific namespace::

    k8s.api.CoreV1Api(api_client).list_namespaced_config_map(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_event(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_endpoints(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_limit_range(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_persistent_volume_claim(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_pod(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_pod_template(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_replication_controller(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_resource_quota(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_secret(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_service(namespace='foo')
    k8s.api.CoreV1Api(api_client).list_namespaced_service_account(namespace='foo')

Some resources of interest, like deployments, are not defined in the Core Api.
To list those you must first find the correct `Api group in
<https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10>`_. For
deployments this turns out to be ``ExtensionsV1beta1Api`` - no, I also do not
fully understand how Swagger translates that naming scheme.

In any case, to list deployments you would use this::

    k8s.ExtensionsV1beta1Api(api_client).list_deployment_for_all_namespaces()
    k8s.ExtensionsV1beta1Api(api_client).list_namespaced_deployment(namespace=namespace)


Create and Delete Namespaces
============================

.. literalinclude:: ../examples/create_and_delete_namespace.py


Watch Resources
===============

.. literalinclude:: ../examples/watch_resources.py


Multiple Clusters
=================

You need to create one ``ApiClient`` instances for each clusters::

    # Create client API instances to each cluster.
    api_client_a = k8s.config.new_client_from_config('/home/user/.kube/kubeconfig_a)
    api_client_b = k8s.config.new_client_from_config('/home/user/.kube/kubeconfig_b)

Then proceed as you usually would. For instance, to list the pods in both
cluster use::

    ret_a = await k8s.api.CoreV1Api(api_client_a).list_pod_for_all_namespaces()
    ret_b = await k8s.api.CoreV1Api(api_client_b).list_pod_for_all_namespaces()

See `this <https://github.com/olitheolix/aiokubernetes/blob/master/examples/multi_cluster.py>`_
script for a complete example.


Execute Commands in Pod
=======================

Executing commands in a pod is part of the Core Api, and the respective method
is ``connect_get_namespaced_pod_exec``. It takes several arguments to control
the terminal and will return an `aiohttp Websocket context manager
<https://docs.aiohttp.org/en/stable/client_quickstart.html#websockets>`_::

    v1_ws = k8s.CoreV1Api(api_client=api_client)

    websocket = await v1_ws.connect_get_namespaced_pod_exec(
        pod_name, namespace,
        command=['/bin/sh', '-c', 'ls'],
        stderr=True, stdin=False,
        stdout=True, tty=False
    )
    assert isinstance(websocket.http, aiohttp.client._WSRequestContextManager)

To consume it::

    async with websocket.http as ws:
        async for msg in ws:
            print(msg.data)

See `this <https://github.com/olitheolix/aiokubernetes/blob/master/examples/all_in_one.py>`_
script for a complete example.


.. note::

   It is currently not possible to create an interactive session.


TBD
===

Write documentation for these features.

   * Timeout
   * Service account authentication

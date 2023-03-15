# python-notes-app

## General info
The source code is cloned from https://github.com/DataDog/apm-tutorial-python and had been modified to test [auto injection of tracing library](https://docs.datadoghq.com/tracing/trace_collection/library_injection/?tab=kubernetes#configure-instrumentation-libraries-injection)

Note: It only contain the notes_app container mentioned in the [guide](
https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-containers/#install-the-sample-dockerized-python-application)

## Prerequisite
- Check that [Datadog Admission Controller](https://docs.datadoghq.com/containers/cluster_agent/admission_controller/?tab=operator) is setup

## Additional Note
- ubi8 base image is used, you can change to other base image if you like.
- [correlate](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/python/) traces and logs have been setup
- `generate-traffic.sh` is a bash script to generate random traffic load
- sample k8s app deployment included and ready to use (update image if you want to build your own)

## Deploy and run on Kubernetes

```
$ kubectl create -f notes-app-dply.yaml
```

**If you wish to build your own docker image**  

Simply run the build command on the same directory as Dockerfile.
```
$ docker build -t <build_prefix>/<image_name>:<version> .
```

- Check that init container is running

```
$ kubectl describe pod

Look for event
Created container datadog-lib-python-init
Started container datadog-lib-python-init
```

- Check datadog agent that traces are received

```
$ kubectl exec -it <datadog-agent-pod> agent status
```

Look for the APM agent status
```
APM Agent
=========
  Status: Running
  Pid: 1.551948e+06
  Uptime: 179943 seconds
  Mem alloc: 12,213,048 bytes
  Hostname: [Redacted]
  Receiver: 0.0.0.0:8126
  Endpoints:
    https://trace.agent.datadoghq.com

  Receiver (previous minute)
  ==========================
    From python 3.8.13 (CPython), client 1.9.0
      Traces received: 21 (28,792 bytes)
      Spans received: 223

    Priority sampling rate for 'service:notes-app,env:dev': 100.0%
```

- To clean up, delete the deployment

```
$ kubectl delete -f notes-app-dply.yaml
```

And, that is all. Enjoy!

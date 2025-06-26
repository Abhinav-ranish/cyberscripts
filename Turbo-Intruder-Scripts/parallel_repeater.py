def queueRequests(target, wordlists):
    engine = RequestEngine(
        endpoint=target.endpoint,
        concurrentConnections=50,  # <--- parallelism level
        requestsPerConnection=1,
        pipeline=False
    )

    for i in range(50):
        engine.queue(target.req)

def handleResponse(req, interesting):
    table.add(req)
    
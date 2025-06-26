def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=10,
                           pipeline=False
                           )

    for i in range(100):
        engine.queue(target.req)

def handleResponse(req, interesting):
    table.add(req)

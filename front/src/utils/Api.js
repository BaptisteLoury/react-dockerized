function get(url, handleData, context) {
    var jwt = sessionStorage.getItem('jwt')

    fetch(url, {
        headers: {
            'Authorization': 'Bearer ' + jwt
        }
    })
        .then(response => {
            if (!response.ok) {
                throw response.status;
            }
            return response.json();
        })
        .then(data => {
            handleData(data)
        })
        .catch(error => {
            if (error === 401) {
                disconnect(context)
            }
            context.setError(error)
        });
}

function post(url, body, handleData, context, useJwt = true) {
    var headers = {}
    if (useJwt) {
        var jwt = sessionStorage.getItem('jwt')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + jwt
        }
    } else {
        headers = {
            'Content-Type': 'application/json'
        }
    }

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(body)
    })
        .then(response => {
            if (!response.ok) {
                throw response.status;
            }
            return response.json();
        })
        .then(data => {
            handleData(data)
        })
        .catch(error => {
            if (error === 401) {
                disconnect(context)
            }
            context.setError(error)
        });
}

function connect(context, jwt) {
    context.setConnected(true)
    sessionStorage.setItem('jwt', jwt)
}

function disconnect(context) {
    context.setConnected(false)
    sessionStorage.removeItem('jwt')
}

const Api = {
    get: get,
    post: post,
    connect: connect,
    disconnect: disconnect
}

export default Api
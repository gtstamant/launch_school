#!/opt/homebrew/opt/bash

function server () {
    while true
    do
        read method path version
        if [[ $method = 'GET' ]]
        then
            echo 'HTTP/1.1 200 OK'
        else
            echo 'HTTP/1.1 400 Bad Request'
        fi
    done

}

coproc SERVER_PROCESS { server; }

nc -l 2345 -vk <&${SERVER_PROCESS[0]} >&${SERVER_PROCESS[1]}
#!/opt/homebrew/opt/bash

function server () {
    while true
    do
        read method path version
        if [[ $method = 'GET' ]]
        then
            if [[ -f "./www/$path" ]]
            then
                echo -ne "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: $(wc -c <'./www/'$path)\r\n\r\n"
            fi
        else
            echo 'HTTP/1.1 400 Bad Request'
        fi
    done

}

coproc SERVER_PROCESS { server; }

nc -l 2345 -vk <&${SERVER_PROCESS[0]} >&${SERVER_PROCESS[1]}
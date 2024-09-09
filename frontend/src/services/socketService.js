import {authService} from "./authService";
import {w3cwebsocket as W3cwebsocket} from 'websocket'

const baseURL = 'ws://localhost/api'

const socketService = async () => {
    const {data: {token}} = await authService.getSocketToken()
    return {
        announcement: ()=> new  W3cwebsocket(`${baseURL}/announcement/?token=${token}`)
    }
}

export {
    socketService
}